@echo off
setlocal

:: Define variables
set "REMOTE_USER=arvypi"
set "REMOTE_HOST=raspberrypi.local"
set "REMOTE_PATH=/home/arvypi/Desktop/invest-scp"

:: Clean the remote directory
echo Cleaning remote directory...
ssh %REMOTE_USER%@%REMOTE_HOST% "rm -rf %REMOTE_PATH%/*"
if %ERRORLEVEL% neq 0 (
    echo Failed to clean remote directory.
    exit /b 1
)

:: Create tarball and transfer files from the current directory
echo Transferring files...
tar --exclude-vcs -czf - -C . . | ssh %REMOTE_USER%@%REMOTE_HOST% "tar -xzvf - -C %REMOTE_PATH%"
if %ERRORLEVEL% neq 0 (
    echo Failed to transfer and extract files.
    exit /b 1
)

echo Files transferred and extracted successfully.

endlocal
