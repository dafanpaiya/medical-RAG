# -*- coding: utf-8 -*-
"""
Optimized OCR Worker Initialization and ONNX CPU Thread Management Module.
Implements:
1. Conservative environment variable clamping (OMP, MKL, OPENBLAS, ORT).
2. Explicit SessionOptions intra-op and inter-op thread clamping for RapidOCR ONNX sessions.
3. Pre-warmed singleton instance lifecycle per worker process to eliminate repeated per-task re-initialization.
"""

import os
import sys
from typing import Optional, Dict, Any

_worker_ocr = None
_worker_init_count = 0
_worker_pid = None
_configured_intra_op = None
_configured_inter_op = None


def configure_conservative_threading(intra_op: int = 1, inter_op: int = 1):
    """
    Sets conservative CPU execution provider threading limits across all supported backends:
    - OpenMP (OMP_NUM_THREADS)
    - Intel MKL (MKL_NUM_THREADS)
    - OpenBLAS (OPENBLAS_NUM_THREADS)
    - ONNXRuntime Environment (ORT_INTRA_OP_NUM_THREADS, ORT_INTER_OP_NUM_THREADS)
    - RapidOCR internal ONNX SessionOptions (intra_op_num_threads, inter_op_num_threads)
    """
    global _configured_intra_op, _configured_inter_op
    _configured_intra_op = intra_op
    _configured_inter_op = inter_op

    # 1. Environment variables (must be set before runtime engine loads)
    os.environ["OMP_NUM_THREADS"] = str(intra_op)
    os.environ["MKL_NUM_THREADS"] = str(intra_op)
    os.environ["OPENBLAS_NUM_THREADS"] = str(intra_op)
    os.environ["ORT_INTRA_OP_NUM_THREADS"] = str(intra_op)
    os.environ["ORT_INTER_OP_NUM_THREADS"] = str(inter_op)

    # 2. Patch SessionOptions inside rapidocr_onnxruntime to strictly clamp intra/inter op threads
    try:
        import rapidocr_onnxruntime.utils as ort_utils
        if not hasattr(ort_utils, "_original_SessionOptions"):
            ort_utils._original_SessionOptions = ort_utils.SessionOptions

        orig_so = ort_utils._original_SessionOptions

        def clamped_session_options():
            opt = orig_so()
            opt.intra_op_num_threads = intra_op
            opt.inter_op_num_threads = inter_op
            return opt

        ort_utils.SessionOptions = clamped_session_options
    except Exception as e:
        # If rapidocr_onnxruntime is not installed or importable, pass safely
        pass


def init_worker(engine_kwargs: Optional[Dict[str, Any]] = None, intra_op: int = 1, inter_op: int = 1):
    """
    Multiprocessing pool initializer.
    Invoked exactly once when each worker process starts up.
    Pre-warms the RapidOCR ONNX inference sessions with conservative thread allocation.
    """
    global _worker_ocr, _worker_init_count, _worker_pid
    _worker_pid = os.getpid()
    _worker_init_count += 1

    configure_conservative_threading(intra_op=intra_op, inter_op=inter_op)

    from rapidocr_onnxruntime import RapidOCR
    kwargs = engine_kwargs or {}
    _worker_ocr = RapidOCR(**kwargs)


def get_worker_ocr(engine_kwargs: Optional[Dict[str, Any]] = None) -> Any:
    """
    Retrieves the worker-process singleton RapidOCR instance.
    If running outside a pooled environment or if uninitialized, performs lazy fallback initialization once.
    """
    global _worker_ocr
    if _worker_ocr is None:
        init_worker(engine_kwargs=engine_kwargs)
    return _worker_ocr


def get_worker_telemetry() -> Dict[str, Any]:
    """
    Returns diagnostic telemetry for the current worker process:
    PID, init count, thread settings, and actual ONNX session thread options.
    """
    global _worker_ocr, _worker_init_count, _worker_pid, _configured_intra_op, _configured_inter_op

    det_intra = None
    det_inter = None
    if _worker_ocr is not None and hasattr(_worker_ocr, "text_detector"):
        infer = getattr(_worker_ocr.text_detector, "infer", None)
        if infer and hasattr(infer, "session"):
            opts = infer.session.get_session_options()
            det_intra = opts.intra_op_num_threads
            det_inter = opts.inter_op_num_threads

    return {
        "pid": os.getpid(),
        "worker_init_count": _worker_init_count,
        "configured_intra_op": _configured_intra_op,
        "configured_inter_op": _configured_inter_op,
        "onnx_detector_intra_op": det_intra,
        "onnx_detector_inter_op": det_inter,
        "env_omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
        "env_mkl_num_threads": os.environ.get("MKL_NUM_THREADS"),
        "env_openblas_num_threads": os.environ.get("OPENBLAS_NUM_THREADS"),
        "env_ort_intra_op_num_threads": os.environ.get("ORT_INTRA_OP_NUM_THREADS"),
    }
