@echo off

@REM set environmental variables
for /f "tokens=*" %%l in ('type %~dp0\env.conf') do set %%l
set lang=Python
set release=3.11.1

@REM iterate through each version, downloading and installing
@REM keep track of exit codes
@REM reject after five in a row errs out
@REM mark when one release errs out but an earlier one does not

@REM if successfully installed
  @REM iterate through each benchmark
    @REM record output in the data/LANG_NAME/BENCHMARK_NAME/ directory
      @REM hyperfine output in TIMESTAMP.json, all regular output in TIMESTAMP.txt
  @REM parse the output data into an excel chart

call %~dp0/install-py.bat

if errorlevel 1 echo %errorlevel%
@REM 216 for incompatible

call %~dp0/benchmark-py.bat

call %~dp0/uninstall-py.bat

@REM uninstall and delete

