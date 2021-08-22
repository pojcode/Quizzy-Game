import os
import json
import time
import colorama
from art import tprint

def clear():
    # clear screen function
    if os.name == 'posix':   # linux and mac
        os.system('clear')
    else:                    # windows = 'nt'
        os.system('cls')

def check_os():
    if os.name == 'posix':   # linux and mac
        return 'posix'
    else:                    # windows = 'nt'
        return 'nt'

def show_menu():
    colorama.init(autoreset=True)
    options = ('play', 'records', 'info & credits')
    print('\n\n\n\n')
    tprint(' '*12 + 'QUIZZY', font='avatar')
    print('\t\t\t####', colorama.Fore.LIGHTBLUE_EX + '#', '####|',
        colorama.Fore.LIGHTGREEN_EX + ' MAIN MENU ', '|####',
        colorama.Fore.LIGHTBLUE_EX + '#', '####\n', sep='')
    for element in options:
        print(f'\t\t\t\t({options.index(element) + 1}) {element.upper()}')
    print(f'\t\t\t\t(0) EXIT')
    colorama.deinit()

def show_menu_play():
    colorama.init(autoreset=True)
    options = ('retry', 'change user', 'main menu')
    print('\n\n\n\n')
    tprint(' '*12 + 'QUIZZY', font='avatar')
    print('\t\t\t####', colorama.Fore.LIGHTGREEN_EX + '#', '####|',
        colorama.Fore.LIGHTBLUE_EX + ' PLAY MENU ', '|####',
        colorama.Fore.LIGHTGREEN_EX + '#', '####\n', sep='')
    for element in options:
        print(f'\t\t\t\t({options.index(element) + 1}) {element.upper()}')
    colorama.deinit()

def set_username():
    username = ''
    while len(username) == 0 or len(username) > 20:
        clear()
        print('\n\n\n\n\n\n\n\n\t\t\t--------| TYPE YOUR NAME |--------')
        username = input(f'\n\n\t\t\t'+ 
                        colorama.Fore.LIGHTMAGENTA_EX + '   >>' +
                        colorama.Style.RESET_ALL + " PLAYER NAME: "
                        ).lower().strip()
        if len(username) == 0:
            print('\n\n\tInvalid name!!')
            time.sleep(1)
        elif len(username) > 20:
            print('\n\n\tInvalid username!!  (Max-lenght = 20)')
            time.sleep(1.3)
    
    return username

def load_files():
    platform = check_os()
    if platform == 'posix':  # for linux/mac
        filename = 'quizzy_data/quizzy_questions.txt'
    else:   # for windows
        filename = 'quizzy_data\quizzy_questions.txt'
    ALL_QUESTIONS = []
    try:
        with open(filename, 'r') as file_object:
            for question in file_object:
                if question.count(';') == 4 or question.startswith('#---#'):
                # Avoid not correct format questions ;=4 because q;wa;wa;wa;ca
                # include separators #---# to manage question difficuly later
                    ALL_QUESTIONS.append(question)
    except FileNotFoundError:
        print('\n\n\n\tThe file quizzy_questions.txt was not found\n'
            '\tMAKE SURE the file is located in the same folder where\n'
            '\tQuizzy.py is located and restart the program again\n\n\n\n')
        input('\tPress ENTER to exit...')
        exit()
    else:
        if platform == 'posix':
            filename = 'quizzy_data/quizzy_records.json'
        else:
            filename = 'quizzy_data\quizzy_records.json'
        records_players = []
        records_scores = []
        try:
            with open(filename, 'r') as file_object:
                records = json.load(file_object)
        except FileNotFoundError:
            pass
        else:
            for element in records:
                records_players.append(element[0])
                records_scores.append(element[1])
                # each record is a tuple of player name and score
        
        return tuple(ALL_QUESTIONS), records_players, records_scores