# File IO means how to open file,handle it,write it,append the text file and if it wasn't a text file it was another file binary file bin. In python the methods for file handling is all are built-in e.g
# f = open("myfile.txt", "r")  # here myfile.txt means the file that we want to open and txt means the type of file normally we know or see and "r" means we can read our file and "w" means write the file,append it by "a","x" create new file,"r+" read and write file,"w+" write and read file,"a+" append and read file,"x+" create new file and read it.
# print(f)#using this we can call it or
# text = f  # now f is store in variables text so we can use text for various operation
# print(text)  # displays it
# read(),readline() and readlines()
# print(text.read())  # this also same
# print(text.read(5))  # this reads the first 5 characters means 5 alphabets of the file
print(
    f.readline()
)  # this reads the first line of the file and again if we print this same code for another next line it shows result in a whitespace due to readline() usually includes the newline character \n at the end of a line and print() adds the another newline
print(f.readline().strip())  # this can remove that whitespace line
print(f.readlines())  # this can returns all the lines but as a list.
# write() if we make a file and read it and again write the same file then the previous contents of that file will be deleted so we should make a separate file for it or we can use mode "r+" for read and write same file
# j = open("myfile.txt","w")
# j.write("hello")
h = open(
    "myfile.txt", "a"
)  # here we are adding addition or new information in our file without deleting the old contents.
# h.write("\nI am adding new information")#this will added just down line of our previous file contents using \n and we are append means adding new line so we use write to add
h.writelines(
    "Apple\n", "Banana\n", "mango\n"
)  # here we are adding multiple lines and writelines()doesn't automatically make out information to next lines so we use \n to send it another lines.
file = open("newmyfile.txt", "x")  # creating new file but it shouldn't be exist before
# file.write("newmyfile.txt")#this can create a new file named newmyfile.txt
f.close()  # close the file and this should be included everyfile handling operation at the end
##close() operation after every file handling is boring so python provides an easier and safer method-with open()e.g
with open("myfile.txt", "r") as g:  # here g means fiile object the variable name g.
    content = g.read()
    print(
        content
    )  # we don't need to call close() everytime python automatically close it even any error occur and we can use this for write and every file handling operation

##Understanding r+,w+ and a+ e.g
#r+ means read and write boths with save our file initially contents.
#w+ means write and read boths and if there is any existing contents in our file before we used w+ on that file then that contents will erase.
#a+ means boths read and write it's save our old existing contents and in append mode when we add new contents then it's will be in last line not in first even we use seek()