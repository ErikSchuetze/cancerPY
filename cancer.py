import os
from random import randint
from shutil import copyfile

link = 'https://thumbs.dreamstime.com/b/bandeira-de-china-com-cara-de-mao-zedong-58366447.jpg'
arquivo= "angela.jpg"
if os.name == "nt":
    import webbrowser
    from wget import download
    download(link, arquivo)
    webbrowser.open("https://youtu.be/uHgt8giw1LY?si=khDbHHpMKIfyGjZW")
else:
    os.system("firefox https://youtu.be/uHgt8giw1LY?si=khDbHHpMKIfyGjZW")
    os.system(f"wget -O {arquivo} {link}")
i = 0
ii = randint(27,100)
while True:
    copyfile("angela.jpg", os.path.join(f"angela({i}).jpg"))
    i = i+1
    if i==ii:
        #os.remove("cancer.py")
        break
