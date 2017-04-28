#!/usr/bin/env python

from ctypes import *

libadd = cdll.LoadLibrary("libfort.so")

class TestParams(Structure):
  _fields_ = [("array", c_double*10)]

  def __init__(self):
    for i in range(0,10):
      self.array[i] = c_double(i)
      print self.array[i]

Test = TestParams()
libadd.__fortran_MOD_print_array(Test.array)

