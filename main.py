import time
import colorama
from quizzy_files.info_credits_functions import show_info_credits
from quizzy_files.records_functions import show_records
from quizzy_files.game_core import game_core
from quizzy_files.global_functions import *

def main():
    colorama.init()
    clear()
    ALL_QUESTIONS, records_players, records_scores = load_files()
    PLAY, RECORDS, INFO, EXIT = '1', '2', '3', '0'
    main_menu = True
    while main_menu:
        clear()
        show_menu()
        menu_option = input(f'\n\n\t\t\t\t'+
                            colorama.Fore.LIGHTMAGENTA_EX + '>>' +
                            colorama.Style.RESET_ALL + " SELECT: "
                            ).strip()
        if menu_option == PLAY:  # option start new game
            first_game = True
            play_menu = True
            while play_menu:
                # submenu after finish the first game
                # dont get into the first time
                clear()
                show_menu_play()
                if first_game:
                    menu_play_option = '2'
                    first_game = False
                    # start game and always be asked for input username
                    # option 2 does it exactly
                else:
                    menu_play_option = input(f'\n\n\t\t\t\t'+
                                        colorama.Fore.LIGHTMAGENTA_EX + '>>' +
                                        colorama.Style.RESET_ALL + " SELECT: "
                                        ).strip()
                if menu_play_option == '1':   # RETRY same username
                    username = game_core(ALL_QUESTIONS, records_players, 
                                        records_scores, player=username)
                    clear()
                    show_records(records_players, records_scores)
                elif menu_play_option == '2':  # CHANGE username, keep playing
                    username = game_core(ALL_QUESTIONS, records_players,
                                         records_scores)
                    # game_core() will ask for username because is not given
                    clear()
                    show_records(records_players, records_scores)
                elif menu_play_option == '3':  # MAIN menu
                    play_menu = False
                else:
                    print('\n\n\t\t\tInvalid option!!')
                    time.sleep(1.2)
        elif menu_option == RECORDS:  # option show RECORDS
            clear()
            show_records(records_players, records_scores)
        elif menu_option == INFO:  # option show info & credits
            clear()
            show_info_credits()
        elif menu_option == EXIT:  # exit program
            main_menu = False
        else:
            print('\n\n\t\t\tInvalid option!!')
            time.sleep(1.2)
        colorama.deinit()