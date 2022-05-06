#### Threading in programming :
    It is a lightweight process that executes code sequence and all the data supporting structures such as opened resources, memory map, stack, etc. In case you want to run the code in parallel, making programming easy. It takes benefit from the architectures of multi-CPU.

#### Threading in Python :
    Threading in python is used to run multiple threads (tasks, function calls) at the same time. Note that this does not mean that they are executed on different CPUs. Python threads will NOT make your program faster if it already uses 100 % CPU time.

#### Multithreading in Python :
    Multithreading is a threading technique in Python programming to run multiple threads concurrently by rapidly switching between threads with a CPU help (called context switching). Besides, it allows sharing of its data space with the main threads inside a process that share information and communication with other threads easier than individual processes. Multithreading aims to perform multiple tasks simultaneously, which increases performance, speed and improves the rendering of the application.

#### How multi threading is achieved in Python :
    It is achieved using Module threading. We need to import it.
    Before using this module we need to install anaconda environment using the installation command.

        conda install -c conda-forge tbb 

    After installing the anaconda environment . We need to import the following modules in a program for implementing the threading process.

        import threading 
        from threading import *

#### async and await in Python :
    ### async : 
                Asynchronous programming is a type of programming in which we can execute more than one task without blocking the Main task (function). In Python, there are many ways to execute more than one function concurrently, one of the ways is by using asyncio.
    ### await : 
                When you call await, the function you're in gets suspended while whatever you asked to wait on happens, and then when it's finished, the event loop will wake the function up again and resume it from the await call, passing any result out




