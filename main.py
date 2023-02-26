import os, time
from colorama import Fore, init
from random import choice
import wget
import zipfile
import shutil
import glob

mp3_mode = False
emojis = ["🔮", "☔", "🍇", "💜", "🍄", "🌸"]
reqfiles = ["ffmpeg", "ffprobe", "yt-dlp"]

def mover():
    filelist=glob.glob("./*.mp3") #mp3
    for single_file in filelist:
        shutil.move(single_file,"./Descargadas/")
    filelist=glob.glob("./*.mp4") #mp4
    for single_file in filelist:
        shutil.move(single_file,"./Descargadas/") 

def getcommand(song):
    if mp3_mode == True:
        return f'yt-dlp --embed-thumbnail --quiet --no-warnings --extract-audio --audio-format mp3 {song}'
    else:
        return f'yt-dlp --no-warnings --quiet -f mp4 {song}'

init()

def cls():
    os.system("cls && title MP3-4 Downloader by Spit" if os.name == "nt" else "clear")

def clog(text):
    print(f"{Fore.LIGHTMAGENTA_EX}[{choice(emojis)}]{Fore.RESET} {text}")



def cinput(text):
    xa = input(f"{Fore.MAGENTA}[{choice(emojis)}]{Fore.RESET} {text} {Fore.LIGHTMAGENTA_EX}")
    print(Fore.RESET)
    return xa

def check_reqfiles():
    cls()
    clog("Si ves esto me debes una galleta!")
    notfindfiles = []
    if not os.path.exists("./Descargadas/"):
        os.mkdir("./Descargadas")
    for file in reqfiles:
        if not os.path.exists(f"{file}.exe"):
            if 'yt-dlp' in file:
                if not os.path.exists(f"yt-dlp_linux"):
                    notfindfiles.append(file)
            if 'ffmpeg' in file or 'ffprobe' in file:
                if not os.path.exists(f"{file}"):
                    notfindfiles.append(file)
    if len(notfindfiles) > 0:
        cls()
        clog(f"Archivos faltantes: {notfindfiles}\n")
        clog("Al parecer no se encuentran los archivos necesarios para que el programa funcione, quieres descargarlos?\n\n1. Sí\n2. No\n")
        xt = str(cinput("Opción >"))
        if xt == "2":
            salir()
        elif xt == "1":
            clog("Descargando")
            if 'ffmpeg' in notfindfiles or 'ffprobe' in notfindfiles:
                if os.name == "nt":
                    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
                    wget.download(url)
                    print()
                    clog("Extrayendo...")
                    with zipfile.ZipFile("ffmpeg-master-latest-win64-gpl.zip", 'r') as zip_ref:
                        zip_ref.extractall("./")
                    clog("Moviendo archivos...")
                    shutil.move("./ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe", "./")
                    shutil.move("./ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe", "./")
                    clog("Limpiando...")
                    shutil.rmtree('./ffmpeg-master-latest-win64-gpl', ignore_errors=True)
                    os.remove("ffmpeg-master-latest-win64-gpl.zip")
                    clog("Archivo descargado!")
                    time.sleep(3)
                else:
                    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz"
                    wget.download(url)

            if 'yt-dlp' in notfindfiles:
                if os.name == "nt":
                    url = "https://github.com/yt-dlp/yt-dlp/releases/download/2023.02.17/yt-dlp.exe"
                    wget.download(url)
                    print()
                    clog("Archivo descargado!")
                    time.sleep(3)
                else:
                    url = "https://github.com/yt-dlp/yt-dlp/releases/download/2023.02.17/yt-dlp_linux"
                    wget.download(url)
                    print()
                    clog("Archivo descargado!")
                    time.sleep(3)
                
        else:
            check_reqfiles()
    else:
        cls()

def salir():
    cls()
    clog("Muchas gracias por usar el programa, que tengas un bonito día.")
    time.sleep(5)
    cls()
    exit()




def prompt():
    print (f"""{Fore.LIGHTMAGENTA_EX}︵‿︵‿୨♡୧‿︵‿︵
  Selecciona:{Fore.RESET}

{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}1{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Descargar canción de un link
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}2{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Descargar canciones de una lista de links
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}3{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Salir""")
    choice = cinput(f"Opción > ")
    return str(choice)

def list_download():
    cls()
    global mp3_mode
    print(f"""{Fore.LIGHTMAGENTA_EX}Descargar videos?
    1. {Fore.RESET}Sí (mp4)
    {Fore.LIGHTMAGENTA_EX}2. {Fore.RESET}No (mp3)
    {Fore.LIGHTMAGENTA_EX}3. {Fore.RESET}Volver""")
    slx = str(cinput(f"Opción >"))
    if slx == "1":
        mp3_mode = False
    elif slx == "2":
        mp3_mode = True
    elif slx == "3":
        main()
    else:
        list_download()
    xe = cinput(f"Nombre de la lista >")
    if not os.path.exists(xe):
        clog("Ese archivo no existe, digita uno válido!")
        time.sleep(5)
        list_download()
        return None
    with open(xe, "r") as f:
        for song in f.readlines():
            cls()
            command = getcommand(song)
            if "youtube.com/" not in song:
                clog(f"({song}) no es un link válido")
                time.sleep(5)
                continue
            clog("Descargando tu canción, espera...")
            try:
                os.system(command)
                cls()
                clog("Tu canción ha sido descargada!")
            except:
                cls()
                clog(f"Error al descargar ({song})...")
            clog("Continuando con los otros links...")
            time.sleep(3)
        f.close()
        mover()
    main()

def single_download(song=None):
    cls()
    global mp3_mode
    print(f"""{Fore.LIGHTMAGENTA_EX}Descargar videos?
    1. {Fore.RESET}Sí (mp4)
    {Fore.LIGHTMAGENTA_EX}2. {Fore.RESET}No (mp3)
    {Fore.LIGHTMAGENTA_EX}3. {Fore.RESET}Volver""")
    slx = str(cinput(f"Opción >"))
    if slx == "1":
        mp3_mode = False
    elif slx == "2":
        mp3_mode = True
    elif slx == "3":
        main()
    else:
        single_download()

    if not(song):
        clog("Ingresa el link de la canción.")
        song = cinput('Link >')

    if "youtube.com/" not in song:
        clog("Error, ingresa un link válido")
        time.sleep(5)
    else:
        command = getcommand(song)

    try:
        cls()
        clog("Descargando tu canción...")
        os.system(command)
        cls()
        clog("Tu canción ha sido descargada!")
        mover()
        time.sleep(5)

    except:
        None
    main()

def main():
    check_reqfiles()
    cls()
    try:
        cls()
        choice = prompt()
        try:
            if choice == '1':
                single_download()
            elif choice == '2':
                list_download()
            elif choice == '3':
                salir()
            else:
                main()
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)
    exit(1)

if __name__ == '__main__':
    main()