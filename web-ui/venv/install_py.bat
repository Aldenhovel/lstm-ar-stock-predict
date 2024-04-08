@echo off

set PYTHON_VERSION=3.7.5
set INSTALL_DIR=%~dp0py
set REQUIREMENTS_FILE=requirements.txt

echo Creating installation directory %INSTALL_DIR%...
mkdir %INSTALL_DIR%
cd %INSTALL_DIR%

echo Downloading Python %PYTHON_VERSION%...
curl -LO https://mirrors.huaweicloud.com/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe 

echo Installing Python %PYTHON_VERSION%...
start /wait python-%PYTHON_VERSION%-amd64.exe TargetDir=%INSTALL_DIR% InstallAllUsers=0 PrependPath=0
%INSTALL_DIR%\python.exe -m pip install --upgrade pip

echo Installing required packages from %REQUIREMENTS_FILE%...
%INSTALL_DIR%\python.exe -m pip install -r %~dp0%REQUIREMENTS_FILE% -i https://mirrors.aliyun.com/pypi/simple/ --no-warn-script-location

echo DONE

pause