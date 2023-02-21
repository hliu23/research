echo Installing %lang% %release% at %INSTALL_PATH%\%lang%...
if not exist %INSTALL_PATH%\%lang% mkdir %INSTALL_PATH%\%lang% 
%DOWNLOAD_PATH%\%lang%\%release%.exe /passive TargetDir=%INSTALL_PATH%\%lang% Shortcuts=0 Include_doc=0 Include_pip=0 Include_tcltk=0 Include_test=0 Include_tools=0

exit /b %errorlevel%