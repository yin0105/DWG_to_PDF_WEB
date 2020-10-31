@echo off

:: cd static\js
REM pushd static\js

REM for %%f in (*.coffee) do (
  REM echo Generating js for %%~nf
  REM coffee -cm %%~nf.coffee 
  REM )

coffee -m -c static\js

:: dir  /od
:: cd ..\..
REM popd
