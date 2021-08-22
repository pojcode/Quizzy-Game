import time
import colorama
from quizzy_files.game_functions import *
from quizzy_files.global_functions import clear, set_username
from quizzy_files.records_functions import save_update_records

def game_core(ALL_QUESTIONS, records_players, records_scores, player=''):
    my_game = Game(ALL_QUESTIONS)
    if player:
        my_game.username = player
    else:
        my_game.username = set_username()
    clear()
    my_game.show_start_game_banner()
    play = True
    while play:  # MAIN game loop
        if my_game.counter_q in (1, 6, 11, 16):
            q_difficulty = my_game.set_question_difficulty()
            # set range of questions to show according difficulty
            # difficulty changes every 5 questions
        question, correct_answer = my_game.select_question(q_difficulty)
        # select the question in that range of difficulty
        question = my_game.format_question(question)
        # format the question to show it to the player
        if my_game.counter_q == 16:
            # last special question with special events
            clear()
            my_game.show_glory_question_intro()
            while True:
                clear()
                my_game.show_banner_glory_question()
                my_game.show_question(question)
                print(f'\n\n\n\n{" "*35}Wildcards not available in GLORY Q?\n')
                user_answer = input(f'\n\n\t'+ 
                                    colorama.Fore.LIGHTMAGENTA_EX + '>>' +
                                    colorama.Style.RESET_ALL + " ANSWER: "
                                    ).lower().strip().replace(')', '')
                if user_answer in ('a', 'b', 'c', 'd'):
                    break
                else:
                    print('\n\n\tInvalid option!!')
                    time.sleep(1)
            check_value = my_game.check_answer(user_answer, correct_answer)
            my_game.show_glory_question_check(check_value)
            if check_value:
                records_players, records_scores = \
                    save_update_records(my_game.username, 
                                        my_game.counter_q,  # 16
                                        records_players, records_scores)
                my_game.show_game_resume(counter_glory=16)
            else:
                records_players, records_scores = \
                    save_update_records(my_game.username, 
                                        my_game.counter_q - 1,  # 15
                                        records_players, records_scores)
                my_game.show_game_resume()
            my_game.show_game_over()
            break
        using_50 = using_phone_call = using_crowd = False
        user_answering = True
        while user_answering:   # Loop for wildcards and check user_answers
            clear()
            print(f'----| QUESTION {my_game.counter_q} |{"-"*68}\n\n')
            if using_50:
                my_game.show_question(question_50)
            else:
                my_game.show_question(question)
            my_game.show_wildcards()
            if using_phone_call:
                print(call_answer)
            if using_crowd:
                print(f'\n{"-" * 5} CROWD OPINION {"-" * 50}')
                for opinion in crowd_opinion:
                    print(f'\n{opinion}')
                print(f'\n{"-" * 70}')
            user_answer = input(f'\n\n\t'+
                                colorama.Fore.LIGHTMAGENTA_EX + '>>' +
                                colorama.Style.RESET_ALL + " ANSWER: "
                                ).lower().strip().replace(')', '')
            # '1' = wildcard phone call
            if (user_answer == '1' and \
                user_answer not in my_game.used_wildcards):   
                if using_50:
                    call_answer = my_game.phone_call(correct_answer, 
                                                     wrong_answer_50)
                else:
                    call_answer = my_game.phone_call(correct_answer)
                using_crowd = False
                using_phone_call = True
                continue
            # '2' = wildcard 50%
            elif (user_answer == '2' and \
                user_answer not in my_game.used_wildcards):    
                question_50, wrong_answer_50 = \
                    my_game.apply_50(question, correct_answer)
                using_phone_call = using_crowd = False
                using_50 = True
                continue
            # '3' = wildcard ask crowd
            elif (user_answer == '3' and \
                user_answer not in my_game.used_wildcards):
                if using_50:
                    crowd_opinion = my_game.ask_crowd(correct_answer, 
                                                      wrong_answer_50)
                else:
                    crowd_opinion = my_game.ask_crowd(correct_answer)
                using_phone_call = False
                using_crowd = True
                continue
            # '4' = wildcard swap question
            elif (user_answer == '4' and \
                user_answer not in my_game.used_wildcards):
                my_game.swap_question()
                user_answering = False
            elif user_answer in my_game.answer_options:
                # user_answer a,b,c, or d
                if using_50:
                    if user_answer not in (correct_answer, wrong_answer_50):
                        print('\n\n\tInvalid option!!')
                        time.sleep(1)
                        continue
                check_value = my_game.check_answer(user_answer,correct_answer)
                my_game.show_right_wrong(correct_answer, check_value)
                if check_value:
                    my_game.counter_q += 1
                    user_answering = False
                else:
                    records_players, records_scores = \
                         save_update_records(my_game.username, 
                                            my_game.counter_q - 1,
                                            records_players, records_scores)
                    my_game.show_game_resume()
                    my_game.show_game_over()
                    user_answering = False
                    play = False
            else:
                print('\n\n\tInvalid option!!')
                time.sleep(1)

    return my_game.username