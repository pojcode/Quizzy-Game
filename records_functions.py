import json
import colorama
from quizzy_files.global_functions import check_os

def save_update_records(player, score, records_players, records_scores):
    platform = check_os()
    if platform == 'posix':  # for linux/mac
        filename = 'quizzy_data/quizzy_records.json'
    else:   # for windows
        filename = 'quizzy_data\quizzy_records.json'
    records_scores.append(int(score))   # it is an int but just to make sure
    records_scores = sorted(records_scores, reverse=True)
    index_score = records_scores.index(score)
    records_players.insert(index_score, player)
    if len(records_players) > 10:
        del records_players[10:]
        del records_scores[10:]
    if score in records_scores:
        records_to_file = []
        for i in range(len(records_players)):
            records_to_file.append((records_players[i], records_scores[i]))
        with open(filename, 'w') as file_object:
            json.dump(records_to_file, file_object)
    
    return records_players, records_scores

def show_records(records_players, records_scores):
    records_scores = sorted(records_scores, reverse=True) 
    max_lenght = 6
    for name in records_players:
        if len(name) > max_lenght:
            max_lenght = len(name)
    # max_lenght adaptable espace between player_name and score
    x = 0
    if max_lenght > 6:
        x = max_lenght / 2 - 3
    esp = (9 - int(x)) * ' '
    # esp autocenter player records regarding records banner
    # x = value to change autocenter 
    colorama.init(autoreset=True)
    print(f'\t{"#"*13}|', colorama.Fore.LIGHTYELLOW_EX + ' RECORDS ', 
        f'|{"#"*13}\n\n', sep='')
    if len(records_players) == 0:
        print("\n\t\tNo RECORDS to display!!\n\n\t\tLet's PLAY...")
    else:
        print(f'\t{esp}RANK{" "*2}PLAYER{" "*(max_lenght - 4)}SCORE\n')
        for i in range(len(records_players)):
            if records_scores[i] == 16:
                print(f'\t{esp}', colorama.Back.LIGHTYELLOW_EX + 
                    colorama.Fore.BLACK + f'#{i + 1}#',
                    f'{" "*(4 - len(str(i + 1)))}'
                    f'{records_players[i]}'
                    f'{" "*(max_lenght - len(records_players[i]))}   ',
                    colorama.Fore.LIGHTYELLOW_EX + f'{records_scores[i]}\n',
                    sep='')
            else: 
                if i == 0:
                    print(f'\t{esp}', colorama.Back.LIGHTWHITE_EX + 
                    colorama.Fore.BLACK + f'#{i + 1}#',
                    f'{" "*(4 - len(str(i + 1)))}'
                    f'{records_players[i]}'
                    f'{" "*(max_lenght - len(records_players[i]))}   ',
                    colorama.Fore.LIGHTYELLOW_EX + f'{records_scores[i]}\n',
                    sep='')
                elif i != 0 and records_scores[i] == 15:
                    print(f'\t{esp}', colorama.Back.LIGHTWHITE_EX + 
                        colorama.Fore.BLACK + f'#{i + 1}#',
                        f'{" "*(4 - len(str(i + 1)))}'
                        f'{records_players[i]}'
                        f'{" "*(max_lenght - len(records_players[i]))}   ',
                        f'{records_scores[i]}\n', sep='')
                else:
                    print(f'\t{esp}#{i + 1}#{" "*(4 - len(str(i + 1)))}'
                        f'{records_players[i]}'
                        f'{" "*(max_lenght - len(records_players[i]))}   '
                        f'{records_scores[i]}\n'
                        )
    colorama.deinit()
    input('\n\n\n\n\t\tPress ENTER to exit...')