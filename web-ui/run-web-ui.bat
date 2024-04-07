@echo off
REM setup
SET "ENV_PATH=./venv/py/"
SET "PYTHON_EXEC=%ENV_PATH%/python.exe"
SET "SCRIPT_PATH=./run-web-ui.py"

REM check
IF NOT EXIST "%PYTHON_EXEC%" (
    ECHO Python executable not found in %ENV_PATH%
    PAUSE
    EXIT /B 1
)

REM run
"%PYTHON_EXEC%" "%SCRIPT_PATH%"

pause