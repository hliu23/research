@echo off

for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python

call py %~dp0/download-py.py %RAW_DATA_PATH%\%lang% %TEMP_DATA_PATH%\%lang% %COMPILED_DATA_PATH%\%lang% %DOWNLOAD_PATH%\%lang% 