set udate=%date:~4%
set utime=%time:~1,-3%
set timestamp=%udate:/=_%__%utime::=_%

set dpath=%RAW_DATA_PATH%\%lang%\%release%

echo %BENCHMARKS%
for %%b in (%BENCHMARKS%) do (
  if not exist %dpath%\%%b mkdir %dpath%\%%b
  
  echo Executing Benchmark %%b...
  %HYPERFINE_PATH% --warmup %NUM_OF_WARMUP_RUNS% --runs %NUM_OF_RUNS% --show-output --export-json %dpath%\%%b\%timestamp%.json "%INSTALL_PATH%\python\python.exe %BENCHMARKS_PATH%\%lang%\harness.py %%b %NUM_OF_ITERATIONS% %NUM_OF_INVOCATIONS%" >> %dpath%\%%b\%timestamp%.log
)
