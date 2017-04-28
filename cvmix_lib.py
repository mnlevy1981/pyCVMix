#!/usr/bin/env python

from ctypes import *
import numpy as np

max_nlev = 30
max_nlev_p1 = max_nlev + 1

# General CVMix data type
class CVMix_vars_type(Structure):
    _fields_ = [("nlev", c_int),
                ("max_nlev", c_int),
                ("Mdiff_iface", c_double*max_nlev_p1),
                ("Tdiff_iface", c_double*max_nlev_p1),
                ("zw_iface", c_double * max_nlev_p1)]

    def __init__(self, nlev):
        self.nlev = nlev
        self.max_nlev = max_nlev
        ocn_depth = 5250
        self.zw_iface[0] = 0.
        for i in range(1,max_nlev_p1):
            self.zw_iface[i] = self.zw_iface[i-1] - float(ocn_depth)/float(max_nlev)

# CVMix parameters that are independent of mixing type
class CVMix_global_params_type(object):
    _fields_ = [("max_nlev", c_int),
                ("Gravity", c_double),
                ("prandtl", c_double),
                ("FreshWaterDensity", c_double),
                ("SaltWaterDensity", c_double)]

    def __init__(self):
        self.max_nlev = max_nlev
        self.Gravity = c_double(9.80616)
        self.prandtl = c_double(1)

# CVMix parameters for background mixing
# (Going to assume Bryan-Lewis mixing for now)
class cvmix_bkgnd_params_type(Structure):
    _fields_ = [("static_Mdiff", c_double*max_nlev_p1),
                ("static_Tdiff", c_double*max_nlev_p1),
                ("handle_old_vals", c_int),
                ("lvary_vertical", c_int),
                ("lvary_horizontal", c_int)]

    def __init__(self, bl1, bl2, bl3, bl4, zw, Prandtl):
        pi = np.arccos(0.)*2.

        self.handle_old_vals = 0
        self.lvary_horizontal = 0
        self.lvary_vertical = 1
        for i in range(0,max_nlev_p1):
            self.static_Tdiff[i] = c_double(bl1 + (bl2/pi) * np.arctan(bl3*(-zw[i]-bl4)))
            self.static_Mdiff[i] = c_double(self.static_Tdiff[i] * Prandtl.value)

class CVMix_lib_class(object):

    def __init__(self, bl1, bl2, bl3, bl4, nlev=max_nlev):
        self._fortran = cdll.LoadLibrary("CVMix/lib/libcvmix-dyn.so")
        self.CVMix_vars = CVMix_vars_type(nlev)
        self.CVMix_global_params = CVMix_global_params_type()
        self.CVMix_BL_params = cvmix_bkgnd_params_type(bl1,
                                                       bl2,
                                                       bl3,
                                                       bl4,
                                                       self.CVMix_vars.zw_iface,
                                                       self.CVMix_global_params.prandtl)

    def cvmix_background_BL(self):
        test(self._fortran, self.CVMix_vars, self.CVMix_BL_params)

def test(libname, CVMix_vars, CVMix_BL_params):
    libname.__cvmix_background_MOD_cvmix_coeffs_bkgnd_low(CVMix_vars.Mdiff_iface,
                                                          CVMix_vars.Tdiff_iface,
                                                          max_nlev,
                                                          max_nlev,
                                                          1,
                                                          CVMix_BL_params,
                                                          None)
    for i in range(0,max_nlev_p1):
        print i, CVMix_vars.zw[i], CVMix_vars.Tdiff_iface[i]

