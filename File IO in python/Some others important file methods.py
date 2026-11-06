##Here are some additional methods worth knowing e.g read(),readline(),readlines(),write(),writelines(),close(),tell(),seek(),flush(),readable(),writable(),seekable() let's learn last 4 with e.g
with open("myfile.txt","r") as f:
    print(f.readable())#checks weather reading is supported
    print(f.writable())#checks weather writing is supported
    print(f.seekable())#checks weather moving the position is supported.
    #it gives True or False in output and here first and last True but second is False due to we open file for reading not for writing 
    
    