import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player Application")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer,font="Helvetica 12 bold",bg='yellow',selectmode=tkr.SINGLE)
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

play_button = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text='PLAY',command=play,bg='purple',fg='white')
exit_button = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text='EXIT',command=ExitMusicPlayer,bg='light blue',fg='black')
pause_button = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text='PAUSE',command=pause,bg='purple',fg='white')
unpause_button = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text='UNPAUSE',command=unpause,bg='light blue',fg='black')

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)

songtitle.pack()
play_button.pack(fill="x")
exit_button.pack(fill="x")
pause_button.pack(fill="x")
unpause_button.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()

