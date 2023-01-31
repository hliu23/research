set date=%date:~4%
set time=%time:~0,-3%
set timestamp=%date:/=_%__%time::=_%

set dpath=%DATA_PATH%\%lang%\%release%


for %%b in (%BENCHMARKS%) do (
  if not exist %dpath%\%%b mkdir %dpath%\%%b
  
  echo Executing Benchmark %%b...
  %HYPERFINE% --warmup %NUM_OF_WARMUP_RUNS% --runs %NUM_OF_RUNS% --time-unit millisecond --show-output --export-json %dpath%\%%b\%timestamp%.json "%INSTALL_PATH%\python\python.exe %BENCHMARKS_PATH%\%lang%\harness.py %%b %NUM_OF_ITERATIONS% %NUM_OF_INVOCATIONS%" >> %dpath%\%%b\%timestamp%.log
)