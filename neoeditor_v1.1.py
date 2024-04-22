#-----------------------------------------------------#
#neoeditor - a WINDOWS ONLY terminal based text editor#
#-----------------------------------------------------#
from os import system
import os
from pystyle import Write, Colors
import pystyle
import time
import pyperclip

def print_styled(message):
    theme = read_theme()
    if theme == 'white' or theme == '':
        print(message)
    elif theme in ['blue', 'green', 'red']:
        color = getattr(pystyle.Colors, theme.lower())
        print(f"{color}{message}")

def read_theme():
    try:
        with open("neotheme.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ''

def save_theme(theme):
    with open("neotheme.txt", "w") as file:
        file.write(theme)
def main():    
    print_styled(f"""
                        __________________              
    _____________________________  /__(_)_  /______________
    __  __ \  _ \  __ \  _ \  __  /__  /_  __/  __ \_  ___/
    _  / / /  __/ /_/ /  __/ /_/ / _  / / /_ / /_/ /  /    
    /_/ /_/\___/\____/\___/\__,_/  /_/  \__/ \____//_/                                                                    
                [v1.1 | by typhoonz0]
    """)
    print_styled(f"\nn = new | e = edit | o = overwrite | d = delete | h = help | s = settings \n")
    mainmenutop = input(f"$ ")
    if mainmenutop == "n":
        filename = input(f"what should the file name be?\n$ ")
        filenahame = filename+".txt"
        with open(filenahame,'w') as file:
            system('cls')
            print_styled(f"\nEditing: {filename}")
            print_styled(f"\nto quit, type -sq on a new line\n")
            writing = input(f"/ ")
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = input(f"/ ")
            if writing == "-sq":
                pyperclip.copy(filenahame)
                print_styled(f"Saving. File path copied to clipboard.")
                time.sleep(1.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f"Saved.")
                time.sleep(1)
                main()


    if mainmenutop == "e":
        file_path = input(f"paste the desired file's name\n$ ")
        system('cls')
        print_styled(f"\nEditing: {file_path}\n")
        print_styled(f"to quit, type -sq on a new line\n\n")
        print_styled(f"Current File Contents:\n")
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "a") as file:
            input(f"Hit ENTER to start writing new content:\n")
            writing = input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                print_styled(f"Saving.")
                time.sleep(1.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f"\nSaved.")
                time.sleep(1)
                main()

    if mainmenutop == "o":
        file_path = input(f"paste the desired file's path name\n$ ")
        system('cls')
        print_styled(f"\nOverwriting: {file_path}\n")
        print_styled(f"to quit, type -sq on a new line\n\n")
        print_styled(f"Current File Contents:\n")
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "w") as file:
            input(f"Hit ENTER to start writing new content:\n")
            writing = input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                print_styled(f"Saving. File path copied to clipboard.")
                time.sleep(1.5)
                print_styled(f" .")
                time.sleep(0.25)
                print_styled(f" .")
                time.sleep(0.25)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f" .")
                time.sleep(0.5)
                print_styled(f"\nSaved.")
                time.sleep(1)
                main()

    if mainmenutop == "s":
        theme_choice = input("Enter theme (blue, green, red, white, cyan) > ").lower()
        if theme_choice in ['blue', 'green', 'red', 'white', 'cyan']:
            save_theme(theme_choice)
            print_styled(f"Theme changed to {theme_choice}.")
            system("pause")
            main()
        else:
            print_styled("Invalid theme. Please try again.")
            system("pause")
            main()

    if mainmenutop == "h":
        print_styled(f"\nNeoeditor 1.0 - by liam\nxliam1 on discord\ntyphoonz0 on github\n")
        print_styled(f"\nthe worst help menu...")
        print_styled(f"\n\ntype n in the main menu to make a new file,\ngive it a name, and start editing! \nthen, when you are done, type -sq\nand you will save the file to wherever you saved this python program.")
        print_styled(f"\n\ntype e in the main menu, paste in your file path\nand make sure it's formatted properly.\nedit your file, type -sq and your file will save")
        print_styled(f"\n\ntype o in the main menu, paste in your file path\nand start over writing. then, type -sq to save")
        system("pause")
        main()

    if mainmenutop == "d":
        system("cls")
        dele = input(f"\nwhich file do you want to delete?")
        os.remove(dele)
        print_styled(f"\nFile was deleted.")
        system("pause")


if __name__ == "__main__":
    main()
