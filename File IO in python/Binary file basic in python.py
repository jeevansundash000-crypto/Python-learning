#Until now we've worked with text file but computer also store other file types such as images(.jpg)(.png),video(.mp4),audio(.mp3),PDFs(.pdf) and many more related to binary.
#we use mode "b" for binary file handling e.g 
with open("image.png","rb") as f:#here r means read and b means binary file mode
    data = f.read() #we store it in bytes not a normal text string
with open("video.mp4", "wb") as m:
    m.write("hello")
    
    