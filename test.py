#!/usr/bin/env python

print(" start call so file\n ")

from ctypes import *

test = cdll.LoadLibrary("./libtest.so")

test.test()
add = test.add
add.argtypes = [c_float, c_float]
add.restype = c_float
print( add(1.3, 13.4) )
