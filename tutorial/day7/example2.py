from mpi4py import MPI

if __name__ == "__main__":

    world_comm = MPI.COMM_WORLD
    world_size = world_comm.Get_size()
    my_rank = world_comm.Get_rank()

    print("World Size: " + str(world_size) + "   " + "Rank: " + str(my_rank))

'''
Execute: mpiexec -n 4 python example1.py
- Communicator may be split into sub-communicators to develop
  a hierarchical
'''
