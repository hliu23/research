@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python

set /a incompatible=0

setlocal ENABLEDELAYEDEXPANSION

for /f "tokens=*" %%t in ('type %TEMP_DATA_PATH%\%lang%\releases.txt') do (
  set release=%%t
  echo %%t
  call %~dp0/install-py.bat
  call %~dp0/benchmark-py.bat
  call %~dp0/uninstall-py.bat
  
  if errorlevel 1 echo %errorlevel%



  @REM if %errorlevel% 1 (
  @REM   echo Release %%t is incompatible
  @REM   set /a incompatible=incompatible+1
  @REM   if (%incompatible%) GEQ 5 (

      
  @REM   )


  @REM )
  
)
endlocal


@REM @REM 216 for incompatible


@REM @REM uninstall and delete