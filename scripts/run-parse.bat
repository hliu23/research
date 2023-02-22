@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python
set release=3.11.2

call python %~dp0/parse.py %RAW_DATA_PATH%\%lang%\%release% %TEMP_DATA_PATH%\%lang%\%release%