#!/usr/bin/env vpython3
import os
import coreclr
import ctypes

def demo0(clr):
    # Once CoreCLR is initialized, bind to the delegate
    proc = ctypes.CFUNCTYPE(ctypes.c_char_p)()
    clr.bind(
        "manlib",
        "ManLib",
        "Bootstrap",
        ctypes.byref(proc)
    )
    # Call the delegate
    print("Calling ManLib::Bootstrap() through delegate...")
    msg = proc()
    print("ManLib::Bootstrap() returned ", msg)
    #clr.libc.free(msg)  # returned string need to be free-ed but in python causes coredump
    del msg

def demo1(clr):
    def cb(i, l, s, f, d):
        print('callback in python', i, l, s, f, d)
        return True
    # Once CoreCLR is initialized, bind to the delegate
    tcb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_long, ctypes.c_char_p, ctypes.c_float, ctypes.c_double)
    proc = ctypes.CFUNCTYPE(ctypes.c_char_p, tcb)()
    clr.bind(
        "manlib",
        "ManLib",
        "BootstrapCB",
        ctypes.byref(proc)
    )
    # Call the delegate
    print("Calling ManLib::BootstrapCB() through delegate...")
    msg = proc(tcb(cb))
    print("ManLib::BootstrapCB() returned ", msg)
    #clr.libc.free(msg)  # returned string need to be free-ed but in python causes coredump
    del msg

def main():
    app_path = os.getcwd()
    clr = coreclr.NetCore(app_path)
    try:
        demo0(clr)
        demo1(clr)
    finally:
        clr.close()

main()
