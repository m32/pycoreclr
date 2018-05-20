#!/usr/bin/env python2
import os
import ctypes, ctypes.util
import coreclr

def main():
    libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
    tpa = []
    for fname in os.listdir(coreclr.coredlltop):
        fqname = os.path.join(coreclr.coredlltop, fname)
        if not os.path.isfile(fqname) or 'dll' != fname.split('.')[-1]:
            continue
        tpa.append(fqname)
    tpa = ':'.join(tpa)
    app_path = os.getcwd()

    property_keys = [
        "APP_PATHS",
        "TRUSTED_PLATFORM_ASSEMBLIES",
    ]
    property_values = [
        app_path,
        tpa,
    ]

    b = ctypes.c_char_p * len(property_keys)
    cproperty_keys = b(*property_keys)
    cproperty_values = b(*property_values)

    coreclr_handle = ctypes.c_void_p()
    domain_id = ctypes.c_uint()

    print("Initializing CoreCLR...")
    ret = coreclr.coreclr_initialize(
        app_path,                       # exePath
        "host",                         # appDomainFriendlyName
        len(property_values),           # propertyCount
        cproperty_keys,                 # propertyKeys
        cproperty_values,               # propertyValues
        ctypes.byref(coreclr_handle),   # hostHandle
        ctypes.byref(domain_id)         # domainId
    )
    if ret < 0:
        print("failed to initialize coreclr. cerr = ", ret)
        return

    proc = ctypes.CFUNCTYPE(ctypes.c_char_p)()
    # Once CoreCLR is initialized, bind to the delegate
    print("Creating delegate...")
    ret = coreclr.coreclr_create_delegate(
        coreclr_handle,
        domain_id,
        "manlib",
        "ManLib",
        "Bootstrap",
        ctypes.byref(proc)
    )
    if ret < 0:
        print("couldn't create delegate. err = ", ret)
        return

    # Call the delegate
    print("Calling ManLib::Bootstrap() through delegate...")
    msg = proc()
    print("ManLib::Bootstrap() returned ", msg)
    #libc.free(msg)  # returned string need to be free-ed but in python causes coredump
    del msg

    coreclr.coreclr_shutdown(
        coreclr_handle,
        domain_id
    )
    del coreclr_handle, domain_id
    del cproperty_keys, cproperty_values

main()
