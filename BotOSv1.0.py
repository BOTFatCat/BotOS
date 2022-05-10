#Created by u/BOT_FatCat


#Some require to be directed to a file, simply replace the ones with "Instert file" with yours
#Example: /Users/User/Desktop/BotOSv1.0/your file here

#Some of the commands require you install bash modules like jp2a for the logo,
#You can look up how to install it or delete the line

#THIS SCRIPT ONLY WORKS ON PYTHON 3.10 or newer, IT WILL NOT WORK ON OLDER VERSIONS

import time
import subprocess
from playsound import playsound

#Starup screen
subprocess.call(["clear"])
time.sleep(1)
subprocess.call(["jp2a", "/Desktop/BotOSv1.0/Neco_shoes.jpg", "--color", "--height=32", "--width=32"])
time.sleep(1)
print("Welcome to BotOS v1.0")
time.sleep(1)
print("Copyright ©2022 BOTNET Corporation All rights reserved")
playsound("Startup_beep.mp3")
System_Active = True
time.sleep(1)

#Fuctions list
#You can make your own fuctions here

def funny_cat():
    subprocess.call(["jp2a", "/Desktop/BotOSv1.0/Neco_shoes.jpg", "--color", "--clear"])
    print("Wow, those are some cool shoes")
    
def help():
    print("Command list:")
    print(" ")
    print("funny cat = prints out a funny cat")
    print("quit = Exit Terminal")
    print("web = Opens a website to your default browser. EX: Https://www.google.com")
    print("asciify = turns a .jpg photo into ASCII characters with the option of color!")
    print("clear = clears the screen")
    
def web():
    website = input("What website?: ")
    print("Opening website to your default browser")
    time.sleep(2)
    subprocess.call(["open", website])
    print("Website Opened")
    
def asciify():
    image =  input("Instert image: ")
    color =  input("Do you want color? y/n?: ")
    if color == "y":
        subprocess.call(["jp2a", image, "--color"])
    else:
        subprocess.call(["jp2a", image])

def clear_screen():
    subprocess.call(["clear"])


#Waits for input from user
#Loops input until a command is recieved
while System_Active:
    try:
        User_input = input("> ")
    except ValueError:
        continue
    else:
        if User_input == "help":
            help()
            continue
        if User_input == "quit":
            subprocess.call(["clear"])
            print("Closing Terminal")
            time.sleep(2)
            playsound("Startup_beep.mp3")
            print("Terminal Closed")
            break
        if User_input == "funny cat":
            funny_cat()
            continue
        if User_input == "web":
            web()
            continue
        if User_input == "asciify":
            asciify()
            continue
        if User_input == "clear":
            clear_screen()
            continue