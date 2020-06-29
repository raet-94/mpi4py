# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:19:02 2018

@author: python
"""

#Message Passing Interface

from mpi4py import MPI

comm = MPI.COMM_WORLD
#todos los procesadores trabajando
rank =comm.Get_rank()
# numero de procesador que se comunican

print("hello world from process",rank)