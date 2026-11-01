@echo off
chcp 65001 >nul 2>&1
setlocal EnableExtensions EnableDelayedExpansion
title 医药RAG 演示 - 停止

rem ============================================================
rem  医药知识问答 Demo - 停止服务
rem  只停止由 启动项目.bat 启动的后端进程（基于 PID + 命令行精确归属校验）
rem  绝对不误杀其他 Python、Node 或无关系统的任何进程
rem ============================================================

set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
cd /d "%ROOT%"
set "LOGDIR=%ROOT%\logs"
set "PIDFILE=%LOGDIR%\backend.pid"

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

echo ============================================================
echo   医药知识问答 Demo - 停止服务
echo ============================================================
echo   项目目录 : %ROOT%
echo   服务地址 : %BASEURL%
echo.

if not exist "%PIDFILE%" (
  echo [未找到 PID 文件] %PIDFILE% 不存在。
  echo [安全防护] 本脚本仅停止由 启动项目.bat 启动并记录 PID 的服务。
  powershell -NoProfile -Command "try { $r = Invoke-WebRequest -Uri '%BASEURL%/' -UseBasicParsing -TimeoutSec 3; if ($r.Content -match '/static/evidence.js') { 'RUNNING' } else { 'OTHER' } } catch { 'STOPPED' }" > "%LOGDIR%\stop_probe.txt" 2>nul
  set "ST="
  set /p ST=<"%LOGDIR%\stop_probe.txt"
  del /q "%LOGDIR%\stop_probe.txt" >nul 2>&1
  if /i "!ST!"=="RUNNING" (
    echo [提示] 端口 %APP_PORT% 上仍有本项目服务在运行，但不是由本脚本启动。
    echo        请在启动该服务的终端窗口按 Ctrl+C 手动停止。
  )
  if /i "!ST!"=="OTHER" echo [提示] 端口 %APP_PORT% 上为其他外部程序，本脚本不做处理。
  if /i "!ST!"=="STOPPED" echo [状态] 未检测到本项目服务在运行。
  goto :end
)

set "BACKEND_PID="
set /p BACKEND_PID=<"%PIDFILE%"
echo !BACKEND_PID!|findstr /R "^[0-9][0-9]*$" >nul 2>&1
if errorlevel 1 (
  echo [错误] PID 文件内容格式无效：%BACKEND_PID%
  echo [说明] 为避免误杀无关进程，脚本拒绝继续操作。
  goto :end
)

echo [1/3] 校验进程所有权（PID !BACKEND_PID!）...
powershell -NoProfile -Command "$p = Get-CimInstance Win32_Process -Filter ('ProcessId=' + %BACKEND_PID%) -ErrorAction SilentlyContinue; if (-not $p) { 'GONE' } elseif (($p.CommandLine -match 'uvicorn') -and ($p.CommandLine -match 'src\.app:app')) { 'OWNED' } else { 'NOTOURS' }" > "%LOGDIR%\stop_probe.txt" 2>nul
set "OWN="
set /p OWN=<"%LOGDIR%\stop_probe.txt"
del /q "%LOGDIR%\stop_probe.txt" >nul 2>&1

if /i "!OWN!"=="GONE" (
  echo   [状态] 进程 !BACKEND_PID! 已退出，服务当前未在运行。
  del /q "%PIDFILE%" >nul 2>&1
  goto :end
)
if /i "!OWN!"=="NOTOURS" (
  echo   [拒绝] 进程 !BACKEND_PID! 正在运行，但其命令行不属于本项目（PID 已被系统复用）。
  echo   [安全防护] 为防止误杀其他程序，停止操作已中止，PID 文件被保留。
  goto :end
)
if /i not "!OWN!"=="OWNED" (
  echo   [错误] 进程所有权核验未通过（核验状态：!OWN!）。
  goto :end
)
echo   OK - 已确认进程属于本项目（FastAPI / uvicorn src.app:app）

echo [2/3] 优雅停止进程与子进程 ...
taskkill /PID !BACKEND_PID! /T /F >nul 2>&1
if errorlevel 1 (
  echo   [错误] 停止进程失败（PID !BACKEND_PID!）。
  echo   [提示] 可能需要管理员权限或进程已处于终止状态。
  goto :end
)
echo   OK - 进程已终止（PID !BACKEND_PID!）

echo [3/3] 清理状态与验证端口 ...
del /q "%PIDFILE%" >nul 2>&1
ping 127.0.0.1 -n 2 >nul
powershell -NoProfile -Command "if (Get-NetTCPConnection -LocalPort %APP_PORT% -State Listen -ErrorAction SilentlyContinue) { 'BUSY' } else { 'FREE' }" > "%LOGDIR%\port.txt" 2>nul
set "PB="
set /p PB=<"%LOGDIR%\port.txt"
del /q "%LOGDIR%\port.txt" >nul 2>&1

if /i "!PB!"=="FREE" (
  echo   OK - 端口 %APP_PORT% 已成功释放，服务已完全停止。
) else (
  echo   [提示] 端口 %APP_PORT% 仍有连接或监听，可能存在其他程序使用。
)

:end
echo.
echo 按任意键关闭此窗口 ...
pause >nul
exit /b 0