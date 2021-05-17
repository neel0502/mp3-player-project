
from tkinter import *
from tkinter import filedialog

import pygame

root = Tk()

frame1 = Frame(root,bg="#26867d")
menu = Menu(frame1)
root.config(menu=menu)
root.config(bg="#26867d")
root.geometry("600x300")
root.title("MP3 player V1.0")


#flag variables
root.filename=""
root.playlist = []
root.pauseFlag = False
root.songAdded = False
root.i = 0
root.songlist=len(root.playlist)
listbox = Listbox(root,width=200,bg="#40e0d0")
listbox.pack()

def openFiles():
    root.songAdded = True
    songs = filedialog.askopenfilenames(initialdir='/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    for root.filename in songs:
        root.playlist.append(root.filename)
        listbox.insert(END,root.filename)



def openFile():
     try:
        root.songAdded = True
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select SONGS",filetypes = (("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
        root.playlist.append(root.filename)
        listbox.insert(END,root.filename)
        print(" Added " + root.filename)

     except:
        print("Cannot load the music")

def playMusic():
    if(root.songAdded == False):
        root.screenMessage.set("no music")
    else:
        try:
            if(root.pauseFlag == True):
                    pygame.mixer.music.unpause()
                    root.pauseFlag == False
                    root.screenMessage.set("Playing " + root.playlist[root.i])
            elif(root.pauseFlag=="stop"):
                    pygame.mixer.music.load(root.playlist[root.i])
                    pygame.mixer.music.play()
                    root.screenMessage.set("Playing " + root.playlist[root.i])

            else:
                print("Playing")
                pygame.mixer.init()
                pygame.mixer.music.load(root.playlist[root.i])
                pygame.mixer.music.play()
                root.screenMessage.set("Playing " + root.playlist[root.i])
        except:
            print("Could not play the music")
            pygame.mixer.music.fadeout(600)
            root.screenMessage.set("End of Playback, Please add more songs")


def pauseMusic():
    if(root.songAdded == False):
        root.screenMessage.set("no music!")
    else:
        try:
            pygame.mixer.music.pause()
            root.pauseFlag = True
            root.screenMessage.set("Paused")
        except:
            print("Cannot Pause the Music")

def stopMusic():
    if(root.songAdded == False):
        root.screenMessage.set("no music!")
    else:
        root.pauseFlag = "stop"
        pygame.mixer.music.fadeout(600)
        root.screenMessage.set("End of Playback!")

def prevMusic():
    if(root.songAdded == False):
        root.screenMessage.set("no music!")
    else:
        try:
            if(root.playlist[root.i - 1]):
                root.i -= 1
                root.pauseFlag = "stop"
                playMusic()
            else:
                print("No previous songs")
                root.screenMessage.set("No previous songs")
        except:
            stopMusic()
            print("No previous songs")

def nextMusic():
    if(root.songAdded == False):
        root.screenMessage.set("no music!")
    else:
        try:

            if(root.playlist[root.i]):
                root.i += 1
                print(root.i,"after pause")
                root.pauseFlag = "stop"
                playMusic()
            else:
              #  root.i -= 1
              pass

        except:
            pygame.mixer.music.fadeout(600)
            root.screenMessage.set("End of Playback, Please add more songs")
def end():
    exit()


#Creating Menus
subMenu = Menu(menu)
menu.add_cascade(label=" Click to SELECT Media",menu=subMenu)
subMenu.add_command(label="Open File", command=openFile)
subMenu.add_separator()
subMenu.add_command(label="Open Files ", command=openFiles)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

contactMenu = Menu(menu)



#lables
one = Label(root, text="MP3 player Controls",width=300,bg="#33b3a6",fg="black")
one.pack(fill=X)
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#buttons
image1= PhotoImage(file= r"C:\Users\neeli\Downloads\previous.png")
pimage1= image1.subsample(6,6)
button1 = Button(topFrame, text="Previous",bg="#2d9d92", fg="white", image=pimage1, command=prevMusic) #Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT,padx=5,pady=20)
image2= PhotoImage(file= r"C:\Users\neeli\Downloads\play.png")
pimage2= image2.subsample(6,6)
button2 = Button(topFrame, text="Play",bg="#2d9d92",fg="white",image=pimage2, command=playMusic)
button2.pack(side=LEFT,padx=5,pady=20)
image3= PhotoImage(file= r"C:\Users\neeli\Downloads\pause.png")
pimage3= image3.subsample(6,6)
button3 = Button(topFrame, text="Pause",bg="#2d9d92",fg="white",image=pimage3, command=pauseMusic)
button3.pack(side=LEFT,padx=5,pady=20)
image5= PhotoImage(file= r"C:\Users\neeli\Downloads\stop.png")
pimage5= image5.subsample(6,6)
button5 = Button(topFrame, text="Stop",bg="#2d9d92",fg="white",image=pimage5, command=stopMusic)
button5.pack(side=LEFT,padx=5,pady=20)
image4= PhotoImage(file= r"C:\Users\neeli\Downloads\next.png")
pimage4= image4.subsample(6,6)
button4 = Button(topFrame, text="Next",bg="#2d9d92",fg="white",image=pimage4, command=nextMusic)
button4.pack(side=LEFT,padx=5,pady=20)

#The status Bar
root.screenMessage = StringVar()
label = Message( root, width=200,textvariable=root.screenMessage, relief=RAISED )
root.screenMessage.set("Designed and Developed by Neelesh,Aditya,Mridul")
label.pack(side=BOTTOM,fill=X)
root.mainloop()
#refreshing the window so that it stays on the screen
