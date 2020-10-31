@echo off
set LOG_FOLDER=a:\inetpub\logs\LogFiles\W3SVC1

:: pushd D:\a
pushd %LOG_FOLDER%
for /f "tokens=*" %%a in ('dir /b /od') do set newest=%%a
echo Newest file: "%newest%" 
echo.
:: tail -n 20 "%newest%" | grep -v "livereload"

tail -n 200 "%newest%" | grep -v /livereload | tail -n 20 

tail -n 200 "%newest%" | grep -v /livereload | tail -n 20 | cut -f 1-5,9-10,12,15 -d " "

echo.
popd
