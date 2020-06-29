# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 08:44:01 2018

@author: python
"""

from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2
data = comm.gather(data, root=0)

if rank == 0:
    print ("rank = %s " %rank +\
           "...receiving data to other process")

    
    for i in range(1,size):
        data[i] = (i+1)**2
        value = data[i]
print(" process %s receiving %s from process %s" %(rank , value , i))