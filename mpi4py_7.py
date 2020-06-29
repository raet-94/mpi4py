# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 08:43:22 2018

@author: python
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [(i+1)**2 for i in range(size)]
    print(data)
else:
    data = None

data = comm.scatter(data, root=0)
print("process = %d" %rank + " recvbuf = %s " %data)