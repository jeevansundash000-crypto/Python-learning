##file position -seek() and tell() is a built-in IO module are the function that is used to work with file objects and their positions
##tell() it's tells you the current file position 
with open("myfile.txt","r") as m:
    print(m.tell())#it will gives 0 cause it is at top means it's executed first and here python doesn't read anything.
    print(m.read(5))#here in file myfile.txt read reads up to 5 characters means space also calculated
    print(m.tell())#it's gives 5 cause python has just read 5 characters and their position is now at positions 5.
    