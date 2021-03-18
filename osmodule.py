import os
from datetime import datetime

#print(dir(os))
#print (os.getcwd() + " is the current working directory")

#navigate to new location
os.chdir('/home/akafle/')
print("The current working directory is " + os.getcwd())

#to list files and folders of current working directory
print(os.listdir())

#create a new folder
#os.mkdir('Os-demo-2')

#also creates a parent directory, so good to always use it
#os.makedirs('Os-demo-3/subdir1')

#delete the folders

#os.rmdir('Os-demo-2')
#os.removedirs('Os-demo-3/subdir1')

print(os.listdir())
os.chdir('/home/akafle/python-practice')
print("Current working directory is "+ os.getcwd())

#return various stats related to a file

# to get the time modified of a file
mod_time = (os.stat('main.py').st_mtime)
print(datetime.fromtimestamp(mod_time))


#traverses a directory tree of a file, goes inside each directory within and finds all files and folder over there

for dirpath, dirnames, filenames in os.walk('/home/akafle/Documents'):
 print('Current path', dirpath)
 print('Directories', dirnames)
 print('Files', filenames)
 print()


#get environment variables

print('Home enviroment variable is ' + os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt')) #grab the file name of any path we are working
print(os.path.dirname('/tmp/test.txt')) #it grabs the directory name of any path we are working on

#split directory name and base name
print(os.path.split('/tmp/test.txt'))

#to check if the path exists or not
print(os.path.exists('/tmp/test.txt'))

#to check if it is directory or file
print(os.path.isdir('/home/akafle'))
print(os.path.isfile(('/home/akafle/test.txt')))

#separate file and extension
print(os.path.splitext('/tmp/test.txt'))


print(dir(os.path))

