#### How to create new thread in Python :
    #Threads in python are an entity within a process that can be scheduled for execution. 
    #In simpler words, a thread is a computation process that is to be performed by a computer. 
    #It is a sequence of such instructions within a program that can be executed independently of other codes.

    #In Python, there are two ways to create a new Thread. 

        ### 1. Creating python threads using class :


            # import the threading module
              import threading

            class thread(threading.Thread):
	            def __init__(self, thread_name, thread_ID):
		            threading.Thread.__init__(self)
		            self.thread_name = thread_name
		            self.thread_ID = thread_ID

		    # helper function to execute the threads
	            def run(self):
		            print(str(self.thread_name) +" "+ str(self.thread_ID));

            thread1 = thread("VAISH", 1000)
            thread2 = thread("CSKWonTheMatch", 2000);

            thread1.start()
            thread2.start()

            print("Exit")

        ### Output :
            VAISH 1000
            CSKWonTheMatch 2000
            Exit

    ### Explanation of the above Code :
         #1. We created a sub-class of the thread class.
         #2.Then we override the __init__ function of the thread class.
         #3.Then we override the run method to define the behavior of the thread.
         #4.The start() method starts a Python thread

        ### 2. Creating python threads using function

            from threading import Thread
            from time import sleep

            # function to create threads
            def threaded_function(arg):
	            for i in range(arg):
                    print("running")
		
		    # wait 1 sec in between each thread
		            sleep(1)


            if __name__ == "__main__":
	            thread = Thread(target = threaded_function, args = (10, ))
	            thread.start()
	            thread.join()
	        print("thread finished...exiting")

        ### Output :
            running
            running
            running
            running
            running
            running
            running
            running
            running
            running
            thread finished...exiting

        ### Explanation of Code :
        #1.We defined a function to create a thread.
        #2.Then we used the threading module to create a thread that invoked the function as its target.
        #3.Then we used start() method to start the Python thread.
