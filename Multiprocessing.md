### Multiprocessing in Generic terms :
     Multiprocessing refers to the ability of a system to support more than one processor at the same time. 
    Applications in a multiprocessing system are broken to smaller routines that run independently. 
    The operating system allocates these threads to the processors improving performance of the system.

### When Multiprocessing comes into picture :
    Consider a computer system with a single processor. If it is assigned several processes at the same time, 
    it will have to interrupt each task and switch briefly to another, to keep all of the processes going.
    This situation is just like a chef working in a kitchen alone. He has to do several tasks like baking, 
    stirring, kneading dough, etc.
    So the gist is that: The more tasks you must do at once, the more difficult it gets to keep 
    track of them all, and keeping the timing right becomes more of a challenge.
    This is where the concept of multiprocessing arises!

### Multiprocessing in Python :
     In Python, the multiprocessing module includes 
     a very simple and intuitive API for dividing work between multiple processes.

     Multiprocessing is a package that supports spawning processes using an API similar to the threading module. 
     The multiprocessing package offers both local and remote concurrency, effectively side-stepping 
     the Global Interpreter Lock by using subprocesses instead of threads. 
     Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors 
     on a given machine. It runs on both Unix and Windows.



