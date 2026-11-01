@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions EnableDelayedExpansion
title 医药RAG 演示 - 启动

rem ============================================================
rem  医药知识问答 Demo - 一键启动
rem  后端：FastAPI (src/app.py) + uvicorn，单进程同时提供前端静态页面
rem  前端：由后端同进程提供（GET / 与 /static），无需单独启动
rem  本脚本只做启动与检查，不修改任何项目代码、配置或数据
rem ============================================================

rem ---- 以脚本自身位置解析项目根目录（不依赖当前工作目录） ----
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
cd /d "%ROOT%"
set "LOGDIR=%ROOT%\logs"
if not exist "%LOGDIR%" mkdir "%LOGDIR%" >nul 2>&1

echo ============================================================
echo   医药知识问答 Demo - 一键启动
echo ============================================================
echo   项目目录 : %ROOT%
echo   日志目录 : %LOGDIR%
echo.

rem ------------------------------------------------------------
rem 步骤 1/6：检查关键文件与配置
rem ------------------------------------------------------------
echo [1/6] 检查关键文件与配置 ...
set "MISSING="
for %%F in (
  ".env"
  "src\app.py"
  "src\unified_qa_engine.py"
  "src\secure_qa_engine.py"
  "static\index.html"
  "static\evidence.js"
  "data\enterprise_regulatory_kb.json"
  "data\staging\phase54_ocr_repair\unified_kb_candidate_phase54.json"
  "data\staging\phase54_ocr_repair\page_and_metadata_conflicts.json"
) do (
  if not exist "%ROOT%\%%~F" set "MISSING=!MISSING!  %%~F"
)
if not "!MISSING!"=="" (
  echo   [错误] 缺少启动所需文件：!MISSING!
  echo   [提示] 请确认项目完整，且未删除配置文件或候选知识库。
  goto :fail
)
echo   OK - 关键文件与配置齐全

rem ------------------------------------------------------------
rem 步骤 2/6：检查 Python 运行环境
rem ------------------------------------------------------------
echo [2/6] 检查 Python 运行环境 ...
set "PY="
set "PYSRC="

rem 优先 1：检查是否已有激活的虚拟环境
if defined VIRTUAL_ENV if exist "%VIRTUAL_ENV%\Scripts\python.exe" (
  set "PY=%VIRTUAL_ENV%\Scripts\python.exe"
  set "PYSRC=当前已激活虚拟环境 (!VIRTUAL_ENV!)"
)

rem 优先 2：检查项目根目录下 .venv 并激活
if not defined PY if exist "%ROOT%\.venv\Scripts\activate.bat" (
  call "%ROOT%\.venv\Scripts\activate.bat"
  set "PY=%ROOT%\.venv\Scripts\python.exe"
  set "PYSRC=项目虚拟环境 (.venv)"
)

rem 优先 3：检查项目根目录下 venv 并激活
if not defined PY if exist "%ROOT%\venv\Scripts\activate.bat" (
  call "%ROOT%\venv\Scripts\activate.bat"
  set "PY=%ROOT%\venv\Scripts\python.exe"
  set "PYSRC=项目虚拟环境 (venv)"
)

rem 优先 4：检查项目既有配置的默认 Python
if not defined PY if exist "D:\python\python.exe" (
  set "PY=D:\python\python.exe"
  set "PYSRC=项目配置解释器 (D:\python\python.exe)"
)

rem 优先 5：搜索系统 PATH 中的 Python
if not defined PY (
  for /f "usebackq delims=" %%I in (`where python 2^>nul`) do (
    if not defined PY if exist "%%I" (
      set "PY=%%I"
      set "PYSRC=系统 PATH (%%I)"
    )
  )
)

if not defined PY (
  echo   [错误] 未找到 Python 解释器。
  echo   [提示] 本项目默认使用 D:\python\python.exe，或在项目根目录创建并激活虚拟环境。
  goto :fail
)

"%PY%" -c "import sys;print(sys.version.split()[0])" > "%LOGDIR%\pyver.txt" 2>nul
set "PYVER="
set /p PYVER=<"%LOGDIR%\pyver.txt"
del /q "%LOGDIR%\pyver.txt" >nul 2>&1
if not defined PYVER (
  echo   [错误] Python 解释器无法运行：%PY%
  goto :fail
)

"%PY%" -c "import sys;sys.exit(0 if sys.version_info>=(3,10) else 1)" >nul 2>&1
if errorlevel 1 (
  echo   [错误] Python 版本过低：%PYVER%（建议 3.10 或更高，项目已验证 3.13）
  goto :fail
)
echo   OK - %PY% （版本 %PYVER%，%PYSRC%）

rem ------------------------------------------------------------
rem 步骤 3/6：检查核心运行依赖（只检查，不执行安装或升级）
rem ------------------------------------------------------------
echo [3/6] 检查核心运行依赖（只检查，不执行安装或升级）...
"%PY%" -c "import fastapi,uvicorn,pydantic,dotenv" >nul 2>"%LOGDIR%\dependency_check.log"
if errorlevel 1 (
  echo   [错误] 缺少运行所需关键库（fastapi / uvicorn / pydantic / python-dotenv）。
  echo   [提示] 请参照 requirements.txt 安装依赖后重试。本脚本遵循只读原则，不会自动安装或改动环境。
  echo   ---- 详细错误信息 ----
  type "%LOGDIR%\dependency_check.log"
  goto :fail
)
del /q "%LOGDIR%\dependency_check.log" >nul 2>&1

"%PY%" -c "import src.unified_qa_engine" >nul 2>"%LOGDIR%\import_check.log"
if errorlevel 1 (
  echo   [错误] 项目模块加载失败，请检查项目文件完整性。
  echo   ---- 详细错误信息 ----
  type "%LOGDIR%\import_check.log"
  goto :fail
)
del /q "%LOGDIR%\import_check.log" >nul 2>&1
echo   OK - 核心依赖与项目模块验证通过
set "OPT_MISSING="
"%PY%" -c "import sentence_transformers" >nul 2>&1
if errorlevel 1 set "OPT_MISSING=!OPT_MISSING! sentence-transformers"
"%PY%" -c "import tiktoken" >nul 2>&1
if errorlevel 1 set "OPT_MISSING=!OPT_MISSING! tiktoken"
if not "!OPT_MISSING!"=="" (
  echo   [说明] requirements.txt 中声明但未安装：!OPT_MISSING!
  echo          当前运行时不需要它们（检索使用内置哈希向量），无需安装。
)

rem ------------------------------------------------------------
rem 步骤 4/6：确定端口，检查是否已在运行 / 端口是否被占用
rem ------------------------------------------------------------
echo [4/6] 检查服务状态与端口占用 ...
set "APP_PORT=8000"
if not defined PORT (
  if exist "%ROOT%\.env" (
    for /f "usebackq tokens=1,2 delims==" %%A in ("%ROOT%\.env") do (
      if /i "%%A"=="PORT" set "APP_PORT=%%B"
    )
  )
)
if defined PORT set "APP_PORT=%PORT%"
set "BASEURL=http://127.0.0.1:%APP_PORT%"

set "PROBE="
powershell -NoProfile -Command "try { $r = Invoke-WebRequest -Uri '%BASEURL%/' -UseBasicParsing -TimeoutSec 3; if ($r.Content -match '/static/evidence.js') { 'OURS' } else { 'OTHER' } } catch { 'FREE' }" > "%LOGDIR%\probe.txt" 2>nul
set /p PROBE=<"%LOGDIR%\probe.txt"
del /q "%LOGDIR%\probe.txt" >nul 2>&1

if /i "!PROBE!"=="OURS" (
  echo   OK - 本项目服务已在运行中，避免重复启动。
  echo.
  echo   访问地址 : %BASEURL%/
  echo   前端架构 : 由 FastAPI 后端内置托管（GET / 与 /static）
  echo   日志目录 : %LOGDIR%
  echo   停止服务 : 双击 停止项目.bat
  echo.
  echo   正在打开浏览器 ...
  start "" "%BASEURL%/"
  goto :done
)

if /i "!PROBE!"=="OTHER" (
  echo   [错误] 端口 %APP_PORT% 已被其他程序占用，且响应的不是本项目。
  echo   [提示] 为确保安全，本脚本不会关闭外部无关进程。
  echo          请释放该端口，或在 .env / 环境变量中指定 PORT 后重试。
  goto :fail
)

set "PORTBUSY="
powershell -NoProfile -Command "if (Get-NetTCPConnection -LocalPort %APP_PORT% -State Listen -ErrorAction SilentlyContinue) { 'BUSY' } else { 'FREE' }" > "%LOGDIR%\port.txt" 2>nul
set /p PORTBUSY=<"%LOGDIR%\port.txt"
del /q "%LOGDIR%\port.txt" >nul 2>&1

if /i "!PORTBUSY!"=="BUSY" (
  echo   [错误] 端口 %APP_PORT% 处于监听状态，但未响应 HTTP。
  echo   [提示] 为避免冲突，请关闭占用该端口的程序，或更改端口配置。
  goto :fail
)
echo   OK - 端口 %APP_PORT% 可用

rem ------------------------------------------------------------
rem 步骤 5/6：启动后端（后台运行，输出写入日志文件）
rem ------------------------------------------------------------
echo [5/6] 启动后端服务 ...
echo   [说明] 前端界面由 FastAPI 原生挂载 (/static 与 /)，单进程提供，无需额外前端进程。
if exist "%LOGDIR%\backend.err.log" move /y "%LOGDIR%\backend.err.log" "%LOGDIR%\backend.prev.err.log" >nul 2>&1
if exist "%LOGDIR%\backend.out.log" move /y "%LOGDIR%\backend.out.log" "%LOGDIR%\backend.prev.out.log" >nul 2>&1
if exist "%LOGDIR%\backend.pid" del /q "%LOGDIR%\backend.pid" >nul 2>&1

powershell -NoProfile -ExecutionPolicy Bypass -Command "$env:PYTHONIOENCODING='utf-8'; $env:PYTHONUNBUFFERED='1'; $p = Start-Process -FilePath '%PY%' -ArgumentList @('-m','uvicorn','src.app:app','--host','127.0.0.1','--port','%APP_PORT%') -WorkingDirectory '%ROOT%' -RedirectStandardOutput '%LOGDIR%\backend.out.log' -RedirectStandardError '%LOGDIR%\backend.err.log' -PassThru -WindowStyle Hidden; Set-Content -Path '%LOGDIR%\backend.pid' -Value $p.Id -Encoding ASCII"

set "BACKEND_PID="
if exist "%LOGDIR%\backend.pid" set /p BACKEND_PID=<"%LOGDIR%\backend.pid"
if not defined BACKEND_PID (
  echo   [错误] 后端进程创建失败（未能获取进程号）。
  goto :fail
)
echo   OK - 后端服务进程已启动（PID: !BACKEND_PID!）

rem ------------------------------------------------------------
rem 步骤 6/6：等待服务就绪
rem ------------------------------------------------------------
echo [6/6] 等待服务就绪（最多 90 秒）...
set /a WAITED=0
:waitloop
set "READY="
powershell -NoProfile -Command "try { $r = Invoke-WebRequest -Uri '%BASEURL%/' -UseBasicParsing -TimeoutSec 3; if ($r.Content -match '/static/evidence.js') { 'READY' } else { 'WAIT' } } catch { 'WAIT' }" > "%LOGDIR%\probe.txt" 2>nul
set /p READY=<"%LOGDIR%\probe.txt"
del /q "%LOGDIR%\probe.txt" >nul 2>&1

if /i "!READY!"=="READY" goto :ready

tasklist /FI "PID eq !BACKEND_PID!" 2>nul | findstr /C:"!BACKEND_PID!" >nul 2>&1
if errorlevel 1 (
  echo   [错误] 后端进程意外退出，服务未能启动。
  echo   ---- 后端错误日志（末尾 30 行）----
  powershell -NoProfile -Command "if (Test-Path '%LOGDIR%\backend.err.log') { Get-Content -Path '%LOGDIR%\backend.err.log' -Tail 30 }"
  goto :fail
)

ping 127.0.0.1 -n 3 >nul
set /a WAITED+=2
if !WAITED! GEQ 90 (
  echo   [错误] 服务启动超时（90 秒未就绪）。
  echo   ---- 后端错误日志（末尾 30 行）----
  powershell -NoProfile -Command "if (Test-Path '%LOGDIR%\backend.err.log') { Get-Content -Path '%LOGDIR%\backend.err.log' -Tail 30 }"
  goto :fail
)
goto :waitloop

:ready
echo   OK - 服务就绪（HTTP 200，前端页面可用）
echo.
echo ============================================================
echo   启动成功！
echo ============================================================
echo   访问地址 : %BASEURL%/
echo   前端架构 : FastAPI 内置静态托管（同进程）
echo   后端进程 : PID !BACKEND_PID!
echo   日志文件 : %LOGDIR%\backend.err.log
echo              %LOGDIR%\backend.out.log
echo   停止服务 : 双击 停止项目.bat
echo.
echo   正在自动打开浏览器 ...
start "" "%BASEURL%/"
goto :done

:fail
echo.
echo ============================================================
echo   启动失败 - 请查看上述错误提示与日志进行排查
echo ============================================================
echo   日志目录 : %LOGDIR%
echo   日志文件 : %LOGDIR%\backend.err.log
echo.
echo 按任意键关闭此窗口 ...
pause >nul
exit /b 1

:done
echo.
echo 按任意键关闭此窗口（关闭窗口不会终止已启动的后台服务）...
pause >nul
exit /b 0