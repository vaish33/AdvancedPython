import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")

# Output:
    calculate square numbers
    calculate cube of numbers
    cube: 8
    square: 4
    square: 9
    cube: 27
    cube: 512
    square: 64
    square: 81
    cube: 729
    done in :  4.036760568618774
    Hah... I am done with all my work now!
