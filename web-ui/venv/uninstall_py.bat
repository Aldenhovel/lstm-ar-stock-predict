@echo off

set PYTHON_VERSION=3.7.5
set INSTALL_DIR=%~dp0py
set REQUIREMENTS_FILE=requirements.txt

echo Creating installation directory %INSTALL_DIR%...
mkdir %INSTALL_DIR%
cd %INSTALL_DIR%
echo Installing Python %PYTHON_VERSION%...
start /wait python-%PYTHON_VERSION%-amd64.exe TargetDir=%INSTALL_DIR% InstallAllUsers=0 PrependPath=0

echo Cleaning up temporary files...
del python-%PYTHON_VERSION%-amd64.exe


@echo off

REM 检查文件夹是否存在
IF EXIST "%INSTALL_DIR%" (
    REM 删除文件夹及其所有内容
    rmdir /S /Q "%INSTALL_DIR%"
    echo Folder "%INSTALL_DIR%" has been deleted.
) ELSE (
    echo Folder "%INSTALL_DIR%" does not exist.
)

pause