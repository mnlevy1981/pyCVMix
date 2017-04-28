#!/usr/bin/env python

from ctypes import *

"""
$ nm libfort.so
0000000000000de4 T ___fortran_MOD_print_hello
                 U __gfortran_st_write
                 U __gfortran_st_write_done
                 U __gfortran_transfer_character_write
0000000000000e57 T _print_hello_
                 U dyld_stub_binder
"""
libadd = cdll.LoadLibrary("libfort.so")

libadd.print_hello_(None)
libadd.__fortran_MOD_print_hello(None)

