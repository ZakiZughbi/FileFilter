import os
# os py module that gives the necessary tools for file manipulation

#THIS PROGRAM: Filters the same file. It takes dir1 files looks in dir2 to see if it repeats then deletes that repeat file in dir1. It filters dir1 for any existing files in dir2.

#variables that hold path of dir1 and dir2
dir1 = '/Users/admin/Desktop/Dir1'
dir2 = '/Users/admin/Desktop/Dir2'

# Grabs all file names in dir1 and puts it in "fileList" array as strings.
#   list of all the files that is needed to iterate through from dir1.
fileList = []
for root, dirs, files in os.walk(dir1):
   print(files)
   fileList.append(files)

fileList = fileList[0]

# Grabs all roots directories in dir2 and puts it in "rootList" array as strings.
#   list of all the root directories from dir2.
rootList = []
for root, dirs, files in os.walk(dir2):
   print(root)
   rootList.append(rootList) #make sure its not root

#Number of files deleted
delFileNum = 0

#Filter
#   this program takes a file runs through all possible roots in dir2 that file can be in. If it finds a existing identical file in dir2 runs one small test to see if it is in dir1 again. Then deltes that repeat file. If that files is not existant is dir2 than it skipps to test the next file (in dir1).
for file in fileList:
    for root in rootList:
        os.chdir(root)
        if os.path.isfile(file) == True:
            print('true')
            print(file)
            print(root)
            os.chdir(dir1)
            if os.path.isfile(file) == True:
                print('deleted')
                print('in:', os.getcwd())
                delFileNum += 1
                print(delFileNum)
            else:
                print('not found')
                print('***** in:', os.getcwd())
            os.remove(file)
            print('----------------------------------------')

#Changes the program back to the desired directory after program completed its task
os.chdir('/Users/admin/Google Drive/Programming/Scripts/Python/FileChecker')

#I dont know but this might work better (it needs to be tested):
for file in fileList:
    for root in rootList:
        os.chdir(root)
        if os.path.isfile(file) == True:
            print('true')
            print(file)
            print(root)
            os.chdir(dir1)
            if os.path.isfile(file) == True:
                print('deleted')
                print('in:', os.getcwd())
                delFileNum += 1
                print(delFileNum)
                # I put os.remove() here beacuse I can find if this file still exists in dir1
                os.remove(file)
            else:
                print('not found')
                print('***** in:', os.getcwd())
            # here I remove the os.remove(), I get alot of problems when its here because if the file name appears more than once it says I cannot delete a file that doesnt exist anymore.
            print('----------------------------------------')
