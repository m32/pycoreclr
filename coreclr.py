import os
from ctypes import *

String = c_char_p
coredlltop = '/devel/bin/dotnet-2.1.105/shared/Microsoft.NETCore.App/2.0.7'
libcoreclr = CDLL(os.path.join(coredlltop, 'libcoreclr.so'))

coreclr_initialize = libcoreclr.coreclr_initialize
coreclr_initialize.argtypes = [String, String, c_int, POINTER(c_char_p), POINTER(c_char_p), POINTER(POINTER(None)), POINTER(c_uint)]
coreclr_initialize.restype = c_int

coreclr_shutdown = libcoreclr.coreclr_shutdown
coreclr_shutdown.argtypes = [POINTER(None), c_uint]
coreclr_shutdown.restype = c_int

coreclr_shutdown_2 = libcoreclr.coreclr_shutdown_2
coreclr_shutdown_2.argtypes = [POINTER(None), c_uint, POINTER(c_int)]
coreclr_shutdown_2.restype = c_int

coreclr_create_delegate = libcoreclr.coreclr_create_delegate
coreclr_create_delegate.argtypes = [POINTER(None), c_uint, String, String, String, c_void_p]
coreclr_create_delegate.restype = c_int

coreclr_execute_assembly = libcoreclr.coreclr_execute_assembly
coreclr_execute_assembly.argtypes = [POINTER(None), c_uint, c_int, POINTER(POINTER(c_char)), String, POINTER(c_uint)]
coreclr_execute_assembly.restype = c_int
