# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:13:02 2018

@author: python
"""

from mpi4py import MPI
 
comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)

if rank==1:
    data_send= "a"     
    destination_process = 5
    source_process = 5
    data_received=comm.sendrecv(data_send,dest=destination_process,source =source_process)
    print("my rank is : "+ str(rank)  +  " and "+ str(source_process) + " send me :" + data_received)
    #para evitar que se bloque un dato por enviarlo , utilizas sendrecv en lugar de send y/o recv 
    #i.e. generas un canal bidireccional

if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    data_received=comm.sendrecv(data_send,dest=destination_process,source=source_process)
    print("my rank is : "+ str(rank)  +  " and "+ str(source_process) + " send me :" + data_received)