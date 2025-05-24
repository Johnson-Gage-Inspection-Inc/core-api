@echo off
REM activate your venv (adjust path as needed)
call C:\Users\Jeff\Desktop\core-api\venv\Scripts\activate.bat
cd /d C:\Users\Jeff\Desktop\core-api
REM start Flask via python, append output to a log
py app.py >> C:\Users\Jeff\Desktop\core-api\api.log 2>&1
