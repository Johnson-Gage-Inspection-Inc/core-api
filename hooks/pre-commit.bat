@echo off
C:\Users\JeffHall\git\api\venv\Scripts\python.exe -m pre_commit run --hook-stage commit
if ERRORLEVEL 1 exit /b 1
