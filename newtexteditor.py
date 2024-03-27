#------------
#neoeditor - a WINDOWS ONLY terminal based text editor written in 420 lines of code
#------------
from os import system
import os
from pystyle import Write, Colors
import time
import pyperclip
import codecs
path1 = (r"C:\Users\xliam\Downloads\neoconfig.txt")
#### CHANGE THIS -----^ TO YOUR USER NAME PLEASE ####
isExisting = os.path.exists(path1)
if isExisting == False:
    with open(path1,'w') as file:
        print("Neoeditor setup")
        print("What would you like your theme to be? (1 = green and white, 2 = white only, 3 = cyan)")
        writing = Write.Input(f"$ ", Colors.green, interval=0.000)
        if writing == "1":
            file.writelines("1234")
        if writing == "2":
            file.writelines("4321")
        if writing == "3":
            file.writelines("5678")
        input("remember, always type h for help in the main menu,\nremember that you copy the newly created file's name on quit,\nand always remember that you can just type the file name\nin the edit or overwrite menu, without the path or anything.\nPress ENTER to continue.")
        x = input("Press ENTER to save, then, restart the program")
        if x == "":
            print("restart program")
        else:
            print("restart program")
else:
    we = 1
    with open(path1, 'rb') as fp:
        v = fp.read()
    v = codecs.decode(v,'base64')
    v = codecs.encode(v, 'hex')
    # if you see this as an error, delete the newly created file in "path1" and start again.
    v = int(v, 16)
    we = (hex(v))

if we == "0xd76df8":
    Write.Print(f"""
                        __________________              
    _____________________________  /__(_)_  /______________
    __  __ \  _ \  __ \  _ \  __  /__  /_  __/  __ \_  ___/
    _  / / /  __/ /_/ /  __/ /_/ / _  / / /_ / /_/ /  /    
    /_/ /_/\___/\____/\___/\__,_/  /_/  \__/ \____//_/                                                                    
                [by xliam1 on discord]
    """, Colors.green, interval=0.000)
    Write.Print(f"\nn = new | e = edit | o = overwrite | h = help | s = settings\n", Colors.green, interval=0.000)
    mainmenutop = Write.Input(f"$ ", Colors.green, interval=0.000)
    if mainmenutop == "n":
        filename = Write.Input(f"what should the file name be?\n$ ", Colors.green, interval=0.000)
        filenahame = filename+".txt"
        with open(filenahame,'w') as file:
            system('cls')
            Write.Print(f"\nEditing: {filename}", Colors.green, interval=0.000)
            Write.Print(f"\nto quit, type -sq on a new line\n", Colors.green, interval=0.000)
            writing = Write.Input(f"/ ", Colors.green, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.green, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.green, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"Saved.", Colors.green, interval=0.000)
                time.sleep(1)


    if mainmenutop == "e":
        file_path = Write.Input(f"paste the desired file's name\n$ ", Colors.green, interval=0.000)
        system('cls')
        Write.Print(f"\nEditing: {file_path}\n", Colors.green, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.green, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.green, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "a") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.green, interval=0.000)
            writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                Write.Print(f"Saving.", Colors.green, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.green, interval=0.000)
                time.sleep(1)

    if mainmenutop == "o":
        file_path = Write.Input(f"paste the desired file's path name\n$ ", Colors.green, interval=0.000)
        system('cls')
        Write.Print(f"\nOverwriting: {file_path}\n", Colors.green, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.green, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.green, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "w") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.green, interval=0.000)
            writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.green, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.green, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.green, interval=0.000)
                time.sleep(1)

    if mainmenutop == "s":
        with open(path1,'w') as file:
            print("Neoeditor setup")
            print("What would you like your theme to be? (1 = green and white, 2 = white only, 3 = cyan)")
            writing = Write.Input(f"$ ", Colors.green, interval=0.000)
            if writing == "1":
                file.writelines("1234")
            if writing == "2":
                file.writelines("4321")
            if writing == "3":
                file.writelines("5678")
            x = input("Press ENTER to save, then, restart the program")
            if x == "":
                print("restart program")
            else:
                print("restart program")
    else:
        with open(path1, 'rb') as fp:
            v = fp.read()
        v = codecs.decode(v,'base64')
        v = codecs.encode(v, 'hex')
        v = int(v, 16)
        we = (hex(v))

    if mainmenutop == "h":
        Write.Print(f"\nNeoeditor 1.0 - by liam\nxliam1 on discord\ntyphoonz0 on github\n", Colors.green, interval=0.000)
        Write.Print(f"\nthe worst help menu...", Colors.green, interval=0.000)
        Write.Print(f"\n\ntype n in the main menu to make a new file,\ngive it a name, and start editing! \nthen, when you are done, type -sq\nand you will save the file to wherever you saved this python program.", Colors.green, interval=0.000)
        Write.Print(f"\n\ntype e in the main menu, paste in your file path\nand make sure it's formatted properly.\nedit your file, type -sq and your file will save", Colors.green, interval=0.000)
        Write.Print(f"\n\ntype o in the main menu, paste in your file path\nand start over writing. then, type -sq to save", Colors.green, interval=0.000)
        mainmenutop = Write.Input(f"\n\n\nn = new | e = edit | o = overwrite | h = help\n$ ", Colors.green, interval=0.000)

# WHIT ONLY THEM
if we == "0xe37db5":
    Write.Print(f"""
                        __________________              
    _____________________________  /__(_)_  /______________
    __  __ \  _ \  __ \  _ \  __  /__  /_  __/  __ \_  ___/
    _  / / /  __/ /_/ /  __/ /_/ / _  / / /_ / /_/ /  /    
    /_/ /_/\___/\____/\___/\__,_/  /_/  \__/ \____//_/                                                                    
                [by xliam1 on discord]
    """, Colors.white, interval=0.000)
    Write.Print(f"\nn = new | e = edit | o = overwrite | h = help | s = settings\n", Colors.white, interval=0.000)
    mainmenutop = Write.Input(f"$ ", Colors.white, interval=0.000)
    if mainmenutop == "n":
        filename = Write.Input(f"what should the file name be?\n$ ", Colors.white, interval=0.000)
        filenahame = filename+".txt"
        with open(filenahame,'w') as file:
            system('cls')
            Write.Print(f"\nEditing: {filename}", Colors.white, interval=0.000)
            Write.Print(f"\nto quit, type -sq on a new line\n", Colors.white, interval=0.000)
            writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.white, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"Saved.", Colors.white, interval=0.000)
                time.sleep(1)


    if mainmenutop == "e":
        file_path = Write.Input(f"paste the desired file's name:\n$ ", Colors.white, interval=0.000)
        system('cls')
        Write.Print(f"\nEditing: {file_path}\n", Colors.white, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.white, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.white, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "a") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.white, interval=0.000)
            writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                Write.Print(f"Saving.", Colors.white, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.white, interval=0.000)
                time.sleep(1)

    if mainmenutop == "o":
        file_path = Write.Input(f"paste the desired file's name:\n$ ", Colors.white, interval=0.000)
        system('cls')
        Write.Print(f"\nOverwriting: {file_path}\n", Colors.white, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.white, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.white, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "w") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.white, interval=0.000)
            writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.white, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.white, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.white, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.white, interval=0.000)
                time.sleep(1)

    if mainmenutop == "s":
        with open(path1,'w') as file:
            print("Neoeditor setup")
            print("What would you like your theme to be? (1 = green and white, 2 = white only, 3 = cyan)")
            writing = Write.Input(f"$ ", Colors.green, interval=0.000)
            if writing == "1":
                file.writelines("1234")
            if writing == "2":
                file.writelines("4321")
            if writing == "3":
                file.writelines("5678")
            x = input("Press ENTER to save, then, restart the program")
            if x == "":
                print("restart program")
            else:
                print("restart program")
    else:
        with open(path1, 'rb') as fp:
            v = fp.read()
        v = codecs.decode(v,'base64')
        v = codecs.encode(v, 'hex')
        v = int(v, 16)
        we = (hex(v))

    if mainmenutop == "h":
        Write.Print(f"\nNeoeditor 1.0 - by liam\nxliam1 on discord\ntyphoonz0 on github\n", Colors.white, interval=0.000)
        Write.Print(f"\nthe worst help menu...", Colors.white, interval=0.000)
        Write.Print(f"\n\ntype n in the main menu to make a new file,\ngive it a name, and start editing! \nthen, when you are done, type -sq\nand you will save the file to wherever you saved this python program.", Colors.green, interval=0.000)
        Write.Print(f"\n\ntype e in the main menu, paste in your file path\nand make sure it's formatted properly.\nedit your file, type -sq and your file will save", Colors.white, interval=0.000)
        Write.Print(f"\n\ntype o in the main menu, paste in your file path\nand start over writing. then, type -sq to save", Colors.white, interval=0.000)
        mainmenutop = Write.Input(f"\n\n\nn = new | e = edit | o = overwrite | h = help\n$ ", Colors.white, interval=0.000)

if we == "0xe7aefc":
    Write.Print(f"""
                        __________________              
    _____________________________  /__(_)_  /______________
    __  __ \  _ \  __ \  _ \  __  /__  /_  __/  __ \_  ___/
    _  / / /  __/ /_/ /  __/ /_/ / _  / / /_ / /_/ /  /    
    /_/ /_/\___/\____/\___/\__,_/  /_/  \__/ \____//_/                                                                    
                [by xliam1 on discord]
    """, Colors.cyan, interval=0.000)
    Write.Print(f"\nn = new | e = edit | o = overwrite | h = help | s = settings\n", Colors.cyan, interval=0.000)
    mainmenutop = Write.Input(f"$ ", Colors.cyan, interval=0.000)
    if mainmenutop == "n":
        filename = Write.Input(f"what should the file name be?\n$ ", Colors.cyan, interval=0.000)
        filenahame = filename+".txt"
        with open(filenahame,'w') as file:
            system('cls')
            Write.Print(f"\nEditing: {filename}", Colors.cyan, interval=0.000)
            Write.Print(f"\nto quit, type -sq on a new line\n", Colors.cyan, interval=0.000)
            writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.cyan, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"Saved.", Colors.cyan, interval=0.000)
                time.sleep(1)


    if mainmenutop == "e":
        file_path = Write.Input(f"paste the desired file's name:\n$ ", Colors.cyan, interval=0.000)
        system('cls')
        Write.Print(f"\nEditing: {file_path}\n", Colors.cyan, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.cyan, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.cyan, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "a") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.cyan, interval=0.000)
            writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            if writing == "-sq":
                Write.Print(f"Saving.", Colors.cyan, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.cyan, interval=0.000)
                time.sleep(1)

    if mainmenutop == "o":
        file_path = Write.Input(f"paste the desired file's name:\n$ ", Colors.white, interval=0.000)
        system('cls')
        Write.Print(f"\nOverwriting: {file_path}\n", Colors.cyan, interval=0.000)
        Write.Print(f"to quit, type -sq on a new line\n\n", Colors.cyan, interval=0.000)
        Write.Print(f"Current File Contents:\n", Colors.cyan, interval=0.000)
        with open(file_path, 'r') as file:
            for line in file:
                print("/", line.strip())
        
        with open(file_path, "w") as file:
            Write.Input(f"Hit ENTER to start writing new content:\n", Colors.cyan, interval=0.000)
            writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            while writing != "-sq":
                file.writelines(writing+"\n")
                writing = Write.Input(f"/ ", Colors.cyan, interval=0.000)
            if writing == "-sq":
                pyperclip.copy(filenahame)
                Write.Print(f"Saving. File path copied to clipboard.", Colors.cyan, interval=0.000)
                time.sleep(1.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.25)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f" .", Colors.cyan, interval=0.000)
                time.sleep(0.5)
                Write.Print(f"\nSaved.", Colors.cyan, interval=0.000)
                time.sleep(1)

    if mainmenutop == "s":
        with open(path1,'w') as file:
            print("Neoeditor setup")
            print("What would you like your theme to be? (1 = green and white, 2 = white only, 3 = cyan)")
            writing = Write.Input(f"$ ", Colors.green, interval=0.000)
            if writing == "1":
                file.writelines("1234")
            if writing == "2":
                file.writelines("4321")
            if writing == "3":
                file.writelines("5678")
            x = input("Press ENTER to save, then, restart the program")
            if x == "":
                print("restart program")
            else:
                print("restart program")
    else:
        with open(path1, 'rb') as fp:
            v = fp.read()
        v = codecs.decode(v,'base64')
        v = codecs.encode(v, 'hex')
        v = int(v, 16)
        we = (hex(v))

    if mainmenutop == "h":
        Write.Print(f"\nNeoeditor 1.0 - by liam\nxliam1 on discord\ntyphoonz0 on github\n", Colors.cyan, interval=0.000)
        Write.Print(f"\nthe worst help menu...", Colors.cyan, interval=0.000)
        Write.Print(f"\n\ntype n in the main menu to make a new file,\ngive it a name, and start editing! \nthen, when you are done, type -sq\nand you will save the file to wherever you saved this python program.", Colors.cyan, interval=0.000)
        Write.Print(f"\n\ntype e in the main menu, paste in your file path\nand make sure it's formatted properly.\nedit your file, type -sq and your file will save", Colors.cyan, interval=0.000)
        Write.Print(f"\n\ntype o in the main menu, paste in your file path\nand start over writing. then, type -sq to save", Colors.cyan, interval=0.000)
        mainmenutop = Write.Input(f"\n\n\nn = new | e = edit | o = overwrite | h = help\n$ ", Colors.cyan, interval=0.000)
