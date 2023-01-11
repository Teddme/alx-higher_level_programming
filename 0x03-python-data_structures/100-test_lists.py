import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
lb = ['hello', 'World']
lib.print_python_list_info(lb)
del lb[1]
lib.print_python_list_info(lb)
lb = lb + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(lb)
lb = []
lib.print_python_list_info(lb)
lb.append(0)
lib.print_python_list_info(lb)
lb.append(1)
lb.append(2)
lb.append(3)
lb.append(4)
lib.print_python_list_info(lb)
lb.pop()
lib.print_python_list_info(lb)
