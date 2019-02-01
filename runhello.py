import subprocess
expout=b"Hello world!"
cmd ="helloworld.cpp"
print("py test script running")
subprocess.call(["g++",cmd]) #For Compiling
process = subprocess.Popen(["./a.out"],stdout=subprocess.PIPE)
stdout = process.communicate()[0]
#print(stdout)
#print(expout)
#print(stdout==expout)
if stdout==expout:
	print("tests ok")
else:
	print("error in commit")
