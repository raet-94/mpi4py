# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 08:44:43 2018

@author: python
"""

from mpi4py import MPI
import numpy


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a_size = 1
senddata = (rank+1)*numpy.arange(size,dtype=int)
recvdata = numpy.empty(size*a_size,dtype=int)
comm.Alltoall(senddata,recvdata)


print(" process %s sending %s receiving %s"\
%(rank , senddata , recvdata))