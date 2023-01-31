echo Installing %lang% %release% at %INSTALL_PATH%\%lang%...
%TEMP_EXE% /passive TargetDir=%INSTALL_PATH%\%lang% Shortcuts=0 Include_doc=0 Include_pip=0 Include_tcltk=0 Include_test=0 Include_tools=0

if errorlevel 1 echo %errorlevel%
exit /b %errorlevel%