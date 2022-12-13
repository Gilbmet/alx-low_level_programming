from ctypes import *
so_file = "/Users/root/putshack.so"

putshack.so = CDLL(so_file)
print(type(my_functions))

<class 'ctypes.CDLL'>

print(putshack.ct == 0)
