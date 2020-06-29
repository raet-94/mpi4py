# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 08:45:35 2018

@author: python
"""

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD


size = comm.size
rank = comm.rank

array_size = 3
recvdata =numpy.zeros(array_size,dtype=numpy.int)
senddata = (rank+1)*numpy.arange(a_size,dtype=numpy.int)


print(" process %s sending %s " %(rank , senddata))
comm.Reduce(senddata,recvdata,root=0,op=MPI.SUM)

print ('on task',rank,'after Reduce:  data = ',recvdata)