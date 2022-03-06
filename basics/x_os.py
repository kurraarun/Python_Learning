import os
print()

print(os.name)
print('This program to get the current Directory')
print(os.getcwd())

os.mkdir('Hello')
os.rmdir('Hello')

new_path = os.path.join(os.getcwd(),'..\..\..\..\Desktop')
print(new_path)

print(os.getcwd())

os.chdir(new_path)
print(os.getcwd())

os.mkdir('P')

os.rename('P','Program_Folder')
new_path = os.path.join(os.getcwd(),'Program_Folder')

os.chdir(new_path)
os.makedirs('a/b/c/d/e')
print(os.getcwd())

new_path = os.path.join(os.getcwd(),'..')

os.chdir(new_path)
try:
    os.mkdir('arunfolder')
    print('We are trying to create another folder with same name')
    os.mkdir('arunfolder')
except Exception as e:
    print('Exception was raised while trying to create duplicate folder')   


os.chdir('/Users/akurra/Desktop/')
print(os.getcwd())
#print(os.listdir())

file_new = open('Arun_Python.txt','w')
file_new.write(str('Hello boss how are you'))
file_new.close()

print("To know the stats of any file in the directory")

print(os.stat('Arun_Python.txt'))
print(os.stat('Arun_Python.txt').st_size)


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Directory path : ', dirpath)
#    print('Directory Names ', dirnames)
#    print('Files under this Direcotry ', filenames)

print()
print(os.environ)
print(os.environ.get('HOME'))

print(dir(os.path))