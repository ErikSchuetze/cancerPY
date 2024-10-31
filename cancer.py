import os
from random import randint
from shutil import copyfile

link = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-VkUY9Gta3Aj6B6-rzBiT0YR2Y4fxMqMoG5JoJlU7T6HVUS9a54zAnIzDL6TNZmPITAIOqomleh-cED9i2zIgFQjCOVvuyhEwInTWnZmPEe1R9vz03F_Jb4Iki66QJyUEfnsUJBR8AI4/s1600/0-8ffBcVdballs-BRa.jpg'
arquivo= "angela.jpg"
if os.name == "nt":
    import webbrowser
    import ctypes
    from wget import download
    ctypes.windll.kernel32.FreeConsole()
    download(link, arquivo)
    webbrowser.open("https://youtu.be/uHgt8giw1LY?si=khDbHHpMKIfyGjZW")
else:
    os.system("firefox https://youtu.be/uHgt8giw1LY?si=khDbHHpMKIfyGjZW")
    os.system(f"wget -O {arquivo} {link}")
i = 0
ii = randint(27,100)
while True:
    copyfile(arquivo, os.path.join(f"copy({i}).jpg"))
    i = i+1
    if i==ii:
        os.remove(arquivo)
        break
