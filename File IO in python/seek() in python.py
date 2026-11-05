##seek() moves the file postition to a particular location e.g
with open("myfile.txt","r") as l:
    print(l.read(3))#read the first 5 characters and space also a characters
    l.seek(0)#we don't need to print cause it's just moves the position not showing results and seek(0) means moves the file postition to 0 place means at the beginning
    print(l.read())#read all the file characters.
    