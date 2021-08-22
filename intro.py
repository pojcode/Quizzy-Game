import time
import random
from colorama import Fore, Style, init, deinit
from art import tprint
from keyboard import wait
from quizzy_files.global_functions import clear

def show_intro():
    init()
    colors = (Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTBLUE_EX, 
            Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX,
            Fore.LIGHTCYAN_EX)
    color_used = None
    for i in range(0, 60):
        clear()
        color_ramdon = random.choice(colors)
        while color_used == color_ramdon:
            color_ramdon = random.choice(colors)
        print(color_ramdon + "")
        tprint("  QUIZZY", font = "rand-xlarge")
        if i < 4:
            time.sleep(0.6)
        elif 3 < i < 10:
            time.sleep(0.3)
        elif 9 < i < 20:
            time.sleep(0.1)
        else:
            time.sleep(0.02)
        color_used = color_ramdon
    clear()
    time.sleep(1)
    init()
    print("\n\n\n\n\n\n\n" + Fore.LIGHTBLUE_EX + '='*100)
    print(Style.RESET_ALL + "="*100)
    time.sleep(0.6)
    print("\n\n\n\n\n\n\n\n" + '='*100 + Fore.LIGHTBLUE_EX + "")
    print("="*100)
    time.sleep(1.2)
    clear()
    print("\n\n\n\n\n\n\n" + Fore.LIGHTBLUE_EX + '='*100)
    print(Style.RESET_ALL + "="*100)
    print(Fore.LIGHTGREEN_EX + "")
    tprint("               QUIZZY", font = "avatar")
    print(Style.RESET_ALL + "="*100)
    print(Fore.LIGHTBLUE_EX + '='*100)
    time.sleep(1.5)
    print(Fore.LIGHTGREEN_EX + "\n\n\n\n\n")
    print("\t\t\t\tP R E S S   S P A C E   B A R")
    print(Style.RESET_ALL + "\n\n\n\n\n\n")
    time.sleep(0.6)
    print(f"{' '*95}|POJ|")
    wait("space")    
    clear()
    print('\n\n\n\n\n\t\t' + Fore.LIGHTCYAN_EX + 
        '        WELCOME TO QUIZZY!!!\n\n\t\t' + Style.RESET_ALL +
        '15 questions, 4 wildcards, no errors\n\n\t\t'
        "    EASY, don't you? let's see...\n\n\n\n\n")
    input('\t\t     Press ENTER to QUIZZING!!!')
    deinit()