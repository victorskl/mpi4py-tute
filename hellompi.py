from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

print("Hello World! I am process %d of %d.\n" % (rank, size))