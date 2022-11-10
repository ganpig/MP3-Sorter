import os

from easygui import diropenbox
from mutagen.mp3 import MP3

a = diropenbox()
for dir in os.listdir(a):
    dir = a+'/'+dir
    if os.path.isdir(dir):
        for i in os.listdir(dir):
            if i.endswith('.mp3'):
                new = MP3(dir+'/'+i)['TRCK'].text[0].zfill(2)+' '+i
                os.rename(dir+'/'+i, dir+'/'+new)
                print(dir+'/'+new)
