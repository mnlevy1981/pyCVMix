#!/usr/bin/env python

from ctypes import *

libadd = cdll.LoadLibrary("libfort.so")

class TestDerivedType(Structure):
  _fields_ = [("one_val", c_double),
              ("two_vals", c_double*2),
              ("n_vals", c_double*3)]

  def __init__(self):
      self.one_val = c_double(1)

      self.two_vals[0] = c_double(2)
      self.two_vals[1] = c_double(3)

      self.n_vals[0] = c_double(4)
      self.n_vals[1] = c_double(5)
      self.n_vals[2] = c_double(6)

Test = TestDerivedType()
# Uncommenting either of the below lines results in seg fault
#print Test.one_val
#print Test.two_vals[0], Test.two_vals[1]
libadd.__fortran_MOD_print_type(Test)

