# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:21:38 2018

@author: python
"""

from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
 #broadcast genera un canal unidireccional de un processo a muchos procesos

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

print("process = %d" %rank + " variable shared  = %s " \
      %variable_to_share)
print("After broadcast") 

variable_to_share = comm.bcast(variable_to_share, root=0)
print("process = %d" %rank + " variable shared  = %d " \
%variable_to_share)