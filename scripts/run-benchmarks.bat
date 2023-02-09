@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python

for /f "tokens=*" %% in ('type %TEMP_DATA_PATH%\%lang%\releases.txt') do set %%l
@REM call %~dp0/install-py.bat

@REM if errorlevel 1 echo %errorlevel%
@REM @REM 216 for incompatible

@REM call %~dp0/benchmark-py.bat

@REM call %~dp0/uninstall-py.bat

@REM @REM uninstall and delete