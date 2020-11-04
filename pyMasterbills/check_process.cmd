@echo off

wmic process where (name="python.exe") get commandline | findstr /i /c:"pyMasterbills.py"  > NUL && (echo %DATE% %TIME% pyMasterbills running >> processes.log && exit /b 1)

ruby notify_pyMasterbill_down.rb
