##Handling erroers in file IO sometimes our programs may said- file doesn't exist,you don't have permission to access it,the file is already present when using "x",you try to read from a file that is not open for reading. so we use try and except we already discuss about it in previous e.g
try:
    with open("myfil.txt","r") as q:
        print(5)
except FileExistsError:
    print("file is found")
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you don't have to access this file")
except Exception as e:
    print('something went wrong:',e)#for this kinds of error we use try and except without causing other code line.
    