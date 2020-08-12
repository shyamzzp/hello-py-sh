import os
#taking user input from the console.
userInput = int(input("Please enter the number of Hello-name scripts you'd like to create: "))
name=""
#loop through the size provided by the user and taking input as the name from the user.
for i in range(userInput):
	# input name string from the user inside the loop
	name = input("Please enter name number "+str(i+1)+">> ")
	#creating a file object and create a file if it doesnt exist
	f = open(name+".sh", "w+")
	#printing on the console the information.
	print("Creating "+name+".sh")
	#writing into the file whatever is mentioned for the scripts.
	f.write("#!/bin/bash\n")
	f.write("echo Hello "+name)
	#closing the file object pointer.
	f.close()
	#finally printing the information to the console.
	print("..."+name+".sh is now executable")
print("Listing contents of last Hello-name file created:")
file1 = open(name+'.sh', 'r')
Lines = file1.readlines()
print("---------------Contents of "+name+".sh ------------------")
for i in Lines:
	print(i.split("\n")[0])
print("---------------Contents of "+name+".sh ------------------")
print("Director listing of Shell Scripts in the current directory")
os.system("ls *.sh")