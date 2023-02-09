@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python
set release=3.11.1


call %~dp0/install-py.bat

if errorlevel 1 echo %errorlevel%
@REM 216 for incompatible

call %~dp0/benchmark-py.bat

call %~dp0/uninstall-py.bat

@REM uninstall and delete