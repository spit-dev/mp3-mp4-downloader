import os, argparse,time
from colorama import Fore, init
from random import choice

mp3_mode = False
emojis = ["🔮", "☔", "🍇", "💜", "🍄", "🌸"]

def getcommand(song):
    if mp3_mode == True:
        return f'yt-dlp.exe --embed-thumbnail --quiet --no-warnings --extract-audio --audio-format mp3 {song}'
    else:
        return f'yt-dlp.exe --no-warnings --quiet -f mp4 {song}'

init()

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def clog(text):
    print(f"{Fore.LIGHTMAGENTA_EX}[{choice(emojis)}]{Fore.RESET} {text}")

def cinput(text):
    xa = input(f"{Fore.MAGENTA}[{choice(emojis)}]{Fore.RESET} {text} {Fore.LIGHTMAGENTA_EX}")
    print(Fore.RESET)
    return xa

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
    {Fore.LIGHTMAGENTA_EX}2. {Fore.RESET}No (mp3)""")
    slx = str(cinput(f"Opción >"))
    if slx == "1":
        mp3_mode = False
    elif slx == "2":
        mp3_mode = True
    else:
        main()
    with open(cinput(f"Nombre de la lista >"), "r") as f:
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
    main()

def single_download():
    cls()
    global mp3_mode
    print(f"""{Fore.LIGHTMAGENTA_EX}Descargar videos?
    1. {Fore.RESET}Sí (mp4)
    {Fore.LIGHTMAGENTA_EX}2. {Fore.RESET}No (mp3)""")
    slx = str(cinput(f"Opción >"))
    if slx == "1":
        mp3_mode = False
    elif slx == "2":
        mp3_mode = True
    else:
        main()

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
        time.sleep(5)

    except:
        None
    main()

def main():
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
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)
    exit(1)

if __name__ == '__main__':
    main()