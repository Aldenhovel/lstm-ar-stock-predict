@echo off

set PYTHON_VERSION=3.7.5
set INSTALL_DIR=%~dp0py
cd %INSTALL_DIR%

IF EXIST "%INSTALL_DIR%" (

    cd %INSTALL_DIR%

    echo Uninstalling Python %PYTHON_VERSION%...
    start /wait python-%PYTHON_VERSION%-amd64.exe TargetDir=%INSTALL_DIR% InstallAllUsers=0 PrependPath=0

    echo Cleaning up temporary files...
    del python-%PYTHON_VERSION%-amd64.exe
    cd ..

    rmdir /S /Q "%INSTALL_DIR%"
    echo env "%INSTALL_DIR%" has been deleted.
) ELSE (
    echo env "%INSTALL_DIR%" does not exist.
)

echo DONE

pause