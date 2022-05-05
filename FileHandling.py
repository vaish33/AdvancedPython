#Before performing any operation on the file like read or write, 
# first we have to open that file. For this, we should use Python’s inbuilt function open()
#But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

#f = open(filename, mode)

#following modes are supported:

#r: open an existing file for a read operation.
#w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
#a:  open an existing file for append operation. It won’t override existing data.
#r+:  To read and write data into the file. The previous data in the file will not be deleted.
#w+: To write and read data. It will override existing data.
#a+: To append and read data from the file. It won’t override existing data.

# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print (each)

#The open command will open the file in the read mode and the for loop will print each line present in the file.
 
# # Python code to illustrate read() mode
file = open("file.txt", "r")
print (file.read())

# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))

# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#The close() command terminates all the resources in use and frees the system of this particular program.

# Python code to illustrate append() mode
file = open('geek.txt','a')
file.write("This will add this line")
file.close()

#rstrip(): This function strips each line of a file off spaces from the right-hand side.
#lstrip(): This function strips each line of a file off spaces from the left-hand side.

# Python code to illustrate with()
with open("file.txt") as file:
	data = file.read()
# do something with data
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
	f.write("Hello World!!!")

# Python code to illustrate split() function
with open("file.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)


 