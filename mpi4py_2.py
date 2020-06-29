# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:32:05 2018

@author: python
"""
## si da error de rango ejecutar como "mpiexec -n 4 python3 mpi4py_2.py"
#comunicacin punto a punto 
from mpi4py import MPI

comm=MPI.COMM_WORLD

size = comm.Get_size()

rank=comm.Get_rank()
print(rank)
print(size)
if rank ==0:
    msg ='Hello, world '
    comm.send(msg,dest=1)
elif rank ==1:
    s =comm.recv()
    print ("rank %d:%s"%(rank,s))    