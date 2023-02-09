@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python
set release=3.11.1

call py %~dp0/python.py %RAW_DATA_PATH%\%lang% %TEMP_DATA_PATH%\%lang% %COMPILED_DATA_PATH%\%lang% %DOWNLOAD_PATH%\%lang% 

@REM call %~dp0/install-py.bat

if errorlevel 1 echo %errorlevel%
@REM 216 for incompatible

@REM call %~dp0/benchmark-py.bat

@REM call %~dp0/uninstall-py.bat

@REM uninstall and delete

@REM set temp_exe