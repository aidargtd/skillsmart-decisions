import ctypes

A = (3 * ctypes.py_object)()
A[0] = 1024
A[1] = '1024'
A[2] = 10.24
for i in A:
    print(i)