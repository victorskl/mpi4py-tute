@echo off
mpiexec.exe -n 4 python hellompi.py
mpiexec.exe -n 4 python broadcast.py
mpiexec.exe -n 4 python scatter-gather.py