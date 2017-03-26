### mpi4py Setup on Windows 

1. Using [Intel® Distribution for Python](https://software.intel.com/en-us/intel-distribution-for-python) in conjunction with [Intel® Parallel Studio XE Cluster Edition](https://software.intel.com/en-us/intel-parallel-studio-xe). Both have [Free for Student](https://software.intel.com/en-us/qualify-for-free-software/student) copy. After installation, add `C:\IntelPython27` to PATH environment variable so that it can access from `cmd.exe`. Then just simply run `mpiexec.exe -n 4 python hellompi.py`, note: `mpirun` is old version and no longer available in Intel compiler suite.

2. Cygwin with OpenMPI and build mpi4py. May loose using Windows based IDE like PyCharm, probably just goes with command line based development. But it is free.


### Reference

* https://github.com/jbornschein/mpi4py-examples/