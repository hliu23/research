echo Installing %lang% %release% at %INSTALL_PATH%\%lang%...
C:\Users\codin\Documents\personal\projects\research\artifacts\downloads\Python\3.11.1.exe TargetDir=%INSTALL_PATH%\%lang% 
@REM Shortcuts=0 Include_doc=0 Include_pip=0 Include_tcltk=0 Include_test=0 Include_tools=0
@REM %DOWNLOAD_PATH%\%lang%\%release%.exe
if errorlevel 1 echo %errorlevel%
exit /b %errorlevel%