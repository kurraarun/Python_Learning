
# Here discussing how to open a file
print()
f = open("hello.txt", "rt")
print(f.read())


x = open("C:\AKURRA\ABC.txt","r")

print(x.read())
print()
y = open("C:\AKURRA\ACC.txt","r")

# This is to print first line of the file which is reading 

print(y.readline())
y.close()  # to close the file

# to append the content into existing file 

z =  open("C:\AKURRA\ACC.txt","a")

z.write(" Writing lines from Python code to existin text file")

z.close()

f = open ("C:\AKURRA\ACC.txt","r")
print(f.read())

# To Overwrite the content to existing file

f = open("C:\AKURRA\ADD.txt","w")
f.write("Woops! I have deleted the content! i overwritten the data ")
f.close()

f11 = open("C:\AKURRA\ADD.txt","r")

print(f11.read())

# To create new file in the specified path

f = open("C:\AKURRA\myfile_arun2.txt","x")

f2 = open("C:\AKURRA\myfile_arun2.txt","w")

f2.write("Hello this is the first file which created directly from Python code")
f2.close()

f3 = open("C:\AKURRA\myfile_arun2.txt","r")

print(f3.read())
