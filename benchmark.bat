@echo off
cd system
if not exist are-we-fast-yet\ git clone --depth 1 https://github.com/smarr/are-we-fast-yet.git
cd are-we-fast-yet

cd benchmarks/Python
py harness.py Richards 5 20
py harness.py Bounce 5 20
py harness.py DeltaBlue 5 20