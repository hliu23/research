@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python
set release=3.9.12

@REM set /a incompatible=0

@REM setlocal ENABLEDELAYEDEXPANSION

call %~dp0/install-py.bat
@REM call %~dp0/benchmark-py.bat
@REM call %~dp0/uninstall-py.bat

@REM for /f "tokens=*" %%t in ('type %TEMP_DATA_PATH%\%lang%\releases.txt') do (
@REM   set release=%%t
@REM   echo %%t
@REM   call %~dp0/install-py.bat
@REM   call %~dp0/benchmark-py.bat
@REM   call %~dp0/uninstall-py.bat

@REM   if errorlevel 1 echo %errorlevel%



  @REM if %errorlevel% 1 (
  @REM   echo Release %%t is incompatible
  @REM   set /a incompatible=incompatible+1
  @REM   if (%incompatible%) GEQ 5 (

      
  @REM   )


  @REM )
  
@REM )
@REM endlocal


@REM @REM 216 for incompatible


@REM @REM uninstall and delete