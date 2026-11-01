import os
import sys
from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.runtime_config import log_engine_selection
from src.translator import RegulatoryTranslator

app = FastAPI(title="Enterprise Pharmaceutical & Medical Device RAG System")

ENTERPRISE_KB_MODE = "ENTERPRISE_REGULATORY_KB"
UNIFIED_KB_MODE = "UNIFIED_KB_CANDIDATE"


def _build_engine():
    # The approved Phase 54 unified enterprise + ChP 2025 knowledge base is the only
    # startup path. UnifiedQAEngine enforces startup integrity (candidate SHA-256,
    # composition counts, enterprise baseline identity, conflict report presence) and
    # refuses to start on any mismatch; there is no fallback corpus and no switch.
    from src.unified_qa_engine import UnifiedQAEngine
    engine = UnifiedQAEngine()
    log_engine_selection(engine, UNIFIED_KB_MODE)
    return engine


engine = _build_engine()
translator = RegulatoryTranslator()

class QueryRequest(BaseModel):
    query: str
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    model: Optional[str] = None
    top_k: Optional[int] = 6
    top_n: Optional[int] = 3
    expansion_mode: Optional[str] = "BASELINE"
    score_threshold: Optional[float] = None

class TranslateRequest(BaseModel):
    text: str
    target_lang: str = "English"
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    model: Optional[str] = None

class EscalateRequest(BaseModel):
    query: str
    user_notes: Optional[str] = ""

class FeedbackRequest(BaseModel):
    query: str
    rating: str  # "UP" or "DOWN"
    feedback_tag: Optional[str] = None
    comment: Optional[str] = ""

class ResolveTicketRequest(BaseModel):
    ticket_id: str
    query: str
    expert_answer: str
    expert_name: str
    doc_references: Optional[list] = []

# Serve static directory
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)

@app.post("/api/query")
async def handle_query(req: QueryRequest, request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    requested_expansion = (req.expansion_mode or "BASELINE").upper()
    safe_expansion_mode = requested_expansion if requested_expansion in ("BASELINE", "CONSERVATIVE", "LEGACY") else "BASELINE"
    result = engine.answer_query(
        query=req.query,
        client_id=client_ip,
        api_key=req.api_key,
        api_base=req.api_base,
        model=req.model,
        top_k=req.top_k or 6,
        top_n=req.top_n or 3,
        expansion_mode=safe_expansion_mode,
        score_threshold=req.score_threshold,
        staging_mode=False
    )
    return result

@app.post("/api/translate")
async def handle_translate(req: TranslateRequest):
    return translator.translate(
        text=req.text,
        target_lang=req.target_lang,
        api_key=req.api_key,
        api_base=req.api_base,
        model=req.model
    )

@app.post("/api/escalate-to-human")
async def handle_escalation(req: EscalateRequest, request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    result = engine.escalate_to_human(
        query=req.query,
        user_notes=req.user_notes or "",
        user_id=f"user_{client_ip}"
    )
    return result

@app.post("/api/feedback")
async def handle_feedback(req: FeedbackRequest, request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    return engine.record_user_feedback(
        query=req.query,
        rating=req.rating,
        feedback_tag=req.feedback_tag,
        comment=req.comment or "",
        user_id=f"user_{client_ip}"
    )

@app.post("/api/resolve-ticket")
async def handle_ticket_resolution(req: ResolveTicketRequest):
    return engine.resolve_and_index_specialist_ticket(
        ticket_id=req.ticket_id,
        query=req.query,
        expert_answer=req.expert_answer,
        expert_name=req.expert_name,
        doc_references=req.doc_references
    )

@app.get("/api/feedback-metrics")
async def get_feedback_metrics():
    return engine.feedback_manager.get_feedback_metrics()

@app.get("/api/audit-logs")
async def get_audit_logs():
    log_path = r"d:\医药RAG\data\audit_trail.jsonl"
    if not os.path.exists(log_path):
        return {"logs": []}

    logs = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    import json
                    logs.append(json.loads(line))
                except Exception:
                    pass
    return {"logs": logs[-20:]}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("src.app:app", host="127.0.0.1", port=port, reload=False)
