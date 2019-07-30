from mpi4py import MPI
import numpy as np

# Adjusting the workload of CPUs and memory footprint

if __name__ == "__main__":

    # get basic information about the MPI communicator
    world_comm = MPI.COMM_WORLD
    world_size = world_comm.Get_size()
    my_rank = world_comm.Get_rank()

    N = 10000000

    # determine the workload of each rank
    workloads = [ N // world_size for i in range(world_size) ]
    for i in range( N % world_size ):
        workloads[i] += 1
    my_start = 0
    for i in range( my_rank ):
        my_start += workloads[i]
    my_end = my_start + workloads[my_rank]

    # initialize a
    start_time = MPI.Wtime()
    a = np.ones( N )
    end_time = MPI.Wtime()
    if my_rank == 0:
        print("Initialize a time: " + str(end_time-start_time))

    # initialize b
    start_time = MPI.Wtime()
    b = np.zeros( N )
    for i in range( my_start, my_end ):
        b[i] = 1.0 + i
    end_time = MPI.Wtime()
    if my_rank == 0:
        print("Initialize b time: " + str(end_time-start_time))

    # add the two arrays
    start_time = MPI.Wtime()
    for i in range( N ):
        a[i] = a[i] + b[i]
    end_time = MPI.Wtime()
    if my_rank == 0:
        print("Add arrays time: " + str(end_time-start_time))

    # average the result
    start_time = MPI.Wtime()
    sum = 0.0
    for i in range( my_start, my_end ):
        sum += a[i]
        
    if my_rank == 0:
        world_sum = sum
        for i in range( 1, world_size ):
            sum_np = np.empty( 1 )
            world_comm.Recv( [sum_np, MPI.DOUBLE], source=i, tag=77 )
            world_sum += sum_np[0]
        average = world_sum / N
    else:
        sum_np = np.array( [sum] )
        world_comm.Send( [sum_np, MPI.DOUBLE], dest=0, tag=77 )

    end_time = MPI.Wtime()
    if my_rank == 0:
        print("Average result time: " + str(end_time-start_time))
        print("Average: " + str(average))

# Execute: mpirun -n 4 python example4.py
