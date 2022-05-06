#The Python GIL stands for Global Interpreter Lock.  In simple words, is a mutex (or a lock) 
# that allows only one thread to hold the control of the Python interpreter.
#This means that only one thread can be in a state of execution at any point in time. 
# The impact of the GIL isn’t visible to developers who execute single-threaded programs, 
# but it can be a performance bottleneck in CPU-bound and multi-threaded code.
#That's the GIL allows only one thread to execute at a time even in a multi-threaded architecture with 
# more than one CPU core.

#GIL only ensures that only one cpython bytecode instruction will run at any given time. 
# It does not care about which CPU core runs the instruction. That is the job of the OS kernel.

#GIL is just a piece of code. The CPython Virtual machine is the process which first compiles the code to 
# Cpython bytecode but it's normal job is to interpret the CPython bytecode.
#  GIL is a piece of code that ensures a single line of bytecode runs at a time no matter how many
#  threads are running. Cpython Bytecode instructions is what constitutes the virtual machine stack. 
# So in a way, GIL will ensure that only one thread holds the GIL at any given point of time. 
# (also that it keeps releasing the GIL for other threads and not starve them.)
