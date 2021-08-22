import random
import time
import colorama
from art import tprint
from quizzy_files.global_functions import clear

class Game(object):
    def __init__(self, ALL_QUESTIONS:tuple):
        self.ALL_QUESTIONS = ALL_QUESTIONS
        self.username = ''
        self.available_wildcards = ['phone call','50%','ask crowd','swap Q?']
        self.answer_options = ("a","b","c","d")
        self.used_wildcards = []
        self.questions_made = []
        self.counter_q = 1
    
    def set_question_difficulty(self):
        index_questions = {}
        questions = ('easy', 'medium', 'hard', 'final')
        questions_index = 0
        for line in self.ALL_QUESTIONS:
            if line.startswith('#---#'):
                index_questions[questions[questions_index]] = \
                    self.ALL_QUESTIONS.index(line)
                questions_index += 1
        # find the indexes where different difficulty questions start
        if self.counter_q <= 5:     # EASY Q
            q_difficulty = self.ALL_QUESTIONS[1:index_questions['medium']]
            # set questions in their difficult range for easy questions
            # that means from 1 to avoid the question banner index 
            # to index medium questions start
        elif 6 <= self.counter_q <= 10:     # MEDIUM Q
            q_difficulty = self.ALL_QUESTIONS[index_questions['medium'] + 1: \
                                                index_questions['hard']]
        elif 11 <= self.counter_q <= 15:    # HARD Q
            q_difficulty = self.ALL_QUESTIONS[index_questions['hard'] + 1: \
                                                index_questions['final']]
        elif self.counter_q == 16:      # FINAL Q
            q_difficulty = self.ALL_QUESTIONS[index_questions['final'] + 1:]
        
        return list(q_difficulty)
    
    def select_question(self, question_difficulty:list):
        # the question has always this format:
        # question; wrong_answer; wrong_answer; wrong_answer; right_answer
        selected_q = random.choice(question_difficulty)
        question_difficulty.remove(selected_q)
        selected_q = selected_q.split(';')
        # converting question in a list, chunking it by ;
        correct_answer = selected_q[-1].strip()
        # always last element of the list
        random_sorted_q = [selected_q[0].strip()]
        # adding element question to new random sorted question
        for answer in range(4): # 4 possible answers
            random_answer = random.choice(selected_q[1:])
            random_sorted_q.append(random_answer.strip())
            selected_q.remove(random_answer)
        # adding the 4 possible answers sorted randomly
        del selected_q
        correct_answer = random_sorted_q.index(correct_answer)
        # search the index of right answer in the new randomly sorted question
        # answer index will be in (1, 2, 3, 4), 0 is always index question
        correct_answer = self.answer_options[correct_answer - 1]
        # -1 to make it matches indexes of answer_options ('a','b','c','d')
        # set the value of correct answer a, b, c, or d
        
        return random_sorted_q, correct_answer
    
    def format_question(self, question):
        esp = 0
        for answer in question[1:]:
            if len(answer) > esp:
                esp = len(answer)
        esp = esp + 15
        formatted_q = (
            f'  · {question[0].strip()}\n\n\n' +
            f'\ta) {question[1].strip()}{" "*(esp - len(question[1]))}' +
            f'b) {question[2].strip()}\n\n' +
            f'\tc) {question[3].strip()}{" "*(esp - len(question[3]))}' +
            f'd) {question[4].strip()}'
            )
        
        return formatted_q

    def show_question(self, question):
        print(question)
    
    def check_answer(self, user_answer, correct_answer):
        
        return user_answer == correct_answer

    def show_right_wrong(self, correct_answer, check_value):
        if check_value:
            print(colorama.Fore.LIGHTGREEN_EX+"\n\t\t\t\t\t\t",
                '-------------------\n\t\t\t\t\t\t'
                '| You are RIGHT!! |'
                '\n\t\t\t\t\t\t-------------------',
                colorama.Style.RESET_ALL + '', sep='')
            input('\n\n\n\n\t\tPress ENTER to continue...')
        else:
            print(colorama.Fore.LIGHTRED_EX+"\n\t\t\t\t\t\t",
                '-'*39, '\n\t\t\t\t\t\t'
                '| You are WRONG!! ', colorama.Style.RESET_ALL +
                'correct answer -> ', colorama.Fore.LIGHTGREEN_EX +
                correct_answer, colorama.Fore.LIGHTRED_EX + ' |'
                '\n\t\t\t\t\t\t', '-'*39,
                colorama.Style.RESET_ALL + '', sep='')
            input('\n\n\n\n\t\tPress ENTER to continue...')

    def show_start_game_banner(self):
        print("\n\n\n\n\n\n\t\t\tOk," + colorama.Fore.LIGHTYELLOW_EX +
            f" {self.username} " + colorama.Style.RESET_ALL + 
            "Let's START...\n\n\n\n")
        input('\t\t\tPress ENTER to start...')

    def show_glory_question_intro(self):
        colorama.init(autoreset=True)
        print(f'\n\n\n\n\t\tCONGRATULATIONS {self.username}!!!\n\n'
            f'\t\tYou have reached question 16\n\n\t\t'
            f'NOW for the', colorama.Fore.LIGHTYELLOW_EX + 'GLORY''...')
        colorama.deinit()
        input('\n\n\n\tPress ENTER when you are ready. GOOD LUCK!!!')
    
    def show_banner_glory_question(self):
        print(f'----| ' +
            colorama.Fore.LIGHTYELLOW_EX + 'QUESTION',
            self.counter_q, colorama.Style.RESET_ALL +
            f'|{"-"*5}|', colorama.Fore.LIGHTYELLOW_EX + 
            'FOR THE GLORY', colorama.Style.RESET_ALL +
            f'|{"-"*43}\n\n')

    def show_glory_question_check(self, check):
        for i in range(0, 40):
            clear()
            if i % 2 == 0:
                print(colorama.Fore.LIGHTGREEN_EX + "\n\n\n\n\n\n\n\n\t\t\t"
                    "YOU ARE RIGHT!!!")
                if i < 10:
                    time.sleep(0.04)
                elif i > 9 and i < 25:
                    time.sleep(0.09)
                elif i > 24 and i < 38:
                    time.sleep(0.3)
                else:
                    time.sleep(0.8)
            else:
                print(colorama.Fore.LIGHTRED_EX + "\n\n\n\n\n\n\n\n\t\t\t"
                    "YOU ARE WRONG!!!")
                if i < 10:
                    time.sleep(0.04)
                elif i > 9 and i < 25:
                    time.sleep(0.09)
                elif i > 24 and i < 38:
                    time.sleep(0.3)
                else:
                    time.sleep(0.8)
        if check:   # if question check is true
            for i in range(0, 6):
                clear()
                print(colorama.Fore.LIGHTGREEN_EX + "\n\n\n\n\n\n\n\n\t\t\t"
                    "YOU ARE RIGHT!!!")
                time.sleep(1)
                clear()
                time.sleep(0.2)
            mg = ("    C", "O", "N", "G", "R", "A", "T", "U",
                "L", "A", "T", "I", "O", "N", "S")
            text = ""
            for i in mg:
                clear()
                print(colorama.Fore.LIGHTCYAN_EX + "\n\n\n")
                text += i
                tprint(text, font="drpepper")
                time.sleep(0.2)    
            time.sleep(1)
            print("#"*82) 
            time.sleep(0.8)
            colorama.init(autoreset=True)
            print(
                f"\n\n\n\n\n\t\t"
                f"{colorama.Fore.LIGHTYELLOW_EX + self.username}, ",
                f"you have answered ",
                f"{colorama.Fore.LIGHTYELLOW_EX+'16 QUESTIONS'}"
                f"{colorama.Fore.LIGHTGREEN_EX + ' RIGHT'}", ','
                f'\n\n\t\tso, I just can '
                f"say well done, you are wiser than I thougth\n\n\t\t"
                f"but... next time it will be harder...\n\n", sep=''
                )
            colorama.deinit()
        else:   #if question check false
            colorama.init(autoreset=True)
            for i in range(0, 6):
                clear()
                print(colorama.Fore.LIGHTRED_EX + "\n\n\n\n\n\n\n\n\t\t\t"
                    "YOU ARE WRONG!!!")
                time.sleep(1)
                clear()
                time.sleep(0.2)
            print(
                f"\n\n\n\n\n\t\tOooohhhhhh NOOOO so close!!!\n\n\t\tAnyway, "
                f"{colorama.Fore.LIGHTYELLOW_EX + self.username} ",
                f"well done.\n\n\t\tYou have answered ",
                f"{colorama.Fore.LIGHTYELLOW_EX + '15 QUESTIONS'}",
                f"{colorama.Fore.LIGHTGREEN_EX + ' RIGHT'}","\n\n\t\t"
                f"Good luck for the next try...", sep=''
                )
            colorama.deinit()
        input('\n\n\n\t\tPress ENTER to continue...')
    
    def show_game_resume(self, counter_glory=None):
        s1 = s2 = 's'
        if counter_glory:
            self.counter_q = counter_glory + 1
        if self.counter_q - 1 == 1:
            s1 = ''
        if len(self.used_wildcards) == 1:
            s2 = ''
        clear()
        print(f'\n\n\n{"#"*12} GAME RESUME {"#"*36}\n\n\n')
        print(f'{"-"*61}'
            f'\n\t\t· PLAYER: {self.username}\n'
            f'\n\t\t· SCORE: {self.counter_q - 1} Right Answer{s1}\n'
            f'\n\t\t· WILDCARDS: {len(self.used_wildcards)} Used Wildcard{s2}'
            f'\n{"-"*61}'
            )
        input('\n\n\n\n\t\tPress ENTER to continue...')

    def show_game_over(self):
        timer = ("  G","A","M","E"," ","O","V","E","R")
        text = ""
        for i in timer:
            clear()
            print("\n\n\n\n\n\n")
            text += i
            print(f'\t\t\t{text}')
            time.sleep(0.3)
        time.sleep(1.5)
        clear()
        print(f"\n\n\n\n\n\n\t\t\t-------------")
        print(f"\t\t\t| GAME OVER |")
        print(f"\t\t\t-------------")
        time.sleep(4)

#------------------------------------------------------------------------------
#------------------------- WILDCARDS ------------------------------------------

    def show_wildcards(self):
        print(f'\n\n\n\n{" "*35}', end='')
        for wildcard in self.available_wildcards:
            if wildcard == ' ':
                pass
            else:
                print(f'({self.available_wildcards.index(wildcard) + 1})'
                    f'{wildcard.title()}  ', end='')
        print('\n\n')

    def phone_call(self, correct_answer, wrong_answer_50=None):
        self.used_wildcards.append('1')
        self.available_wildcards.pop(0)
        self.available_wildcards.insert(0,' ')
        if wrong_answer_50:
            call_answer_wrong = wrong_answer_50 
        else:                           
            call_answer_wrong = ''
            while (call_answer_wrong == '' or
                   call_answer_wrong == correct_answer):
                call_answer_wrong = random.choice(self.answer_options)
        fail_percentage = random.randint(0, 10)  
        #  phone call will fail depending on difficulty
        if self.counter_q <= 5:
            if fail_percentage == 0:    # 10% wrong possibilities
                final_call_answer = call_answer_wrong
            else:
                final_call_answer = correct_answer
        elif 6 <= self.counter_q <= 10:    
            if fail_percentage in (0, 1):   # 20% wrong possibilities
                final_call_answer = call_answer_wrong
            else:
                final_call_answer = correct_answer
        elif self.counter_q >= 11:
            if fail_percentage in (0, 1, 2):   # 30% wrong possibilities
                final_call_answer = call_answer_wrong
            else:
                final_call_answer = correct_answer
        people_to_call = (
                    "Yes, I am Einstein, yes I demostrated the theory of "
                    "relativity and yes, I am dead,\n\nso let me rest in pace"
                    " ok, bastard... anyway ->",
                    "Hey I am Donald Duck...Trump, How you going? No idea, "
                    "so...so...so...\n\nWhat are we talking about? "
                    "mmmmmm coin flip ->",
                    "Hiiii!!, I am Pariiiis, rigth now I am very busy taking"
                    " a champagne bath.\n\nHowever I will help you. I would "
                    "say... option 'e', but anyway I will ask my dog,\n\n"
                    "to make sure... ok, it is not option 'e' is ->",
                    )
        make_call = ''
        while make_call not in ('1', '2', '3'):
            clear()
            print(f"\n\n\n\n\n\n\t{'-'*15} WHO WILL YOU CALL? {'-'*15}\n\n\n")
            print(f"\tA. EINSTEIN -> 1    D. TRUMP -> 2    P.HILTON -> 3"
                f"\n\n\n\n\n")
            make_call = input("\t\t\t>> TO CALL -> ").strip()
        timer = ("\t\t\t ·", "-", "·", "-", "·", "-", "·", "-", "·", "-", "·")
        text = ""
        for i in timer:
            clear()
            print(f"\n\n\n\n\n\n\t{'-'*15} OK, CALLING... {'-'*15}\n\n\n")
            text += i
            print(text)
            time.sleep(0.3)
        if make_call == '1':
            person = 'A. EINSTEIN'
            print(f"\n\n\n{person}, on the phone:\n\n")
            print(f"{people_to_call[0]} {final_call_answer}")
        elif make_call == '2':
            person = 'D. TRUMP'
            print(f"\n\n\n{person}, on the phone:\n\n")
            print(f"{people_to_call[1]} {final_call_answer}")
        else:
            person = 'P. HILTON'
            print(f"\n\n\n{person}, on the phone:\n\n")
            print(f"{people_to_call[2]} {final_call_answer}")
        input('\n\n\n\n\tPress ENTER to continue...')
        msg = f'\n{person} thinks correct answer is -> {final_call_answer}\n'

        return msg

    def apply_50(self, question, correct_answer):
        self.used_wildcards.append('2')
        self.available_wildcards.pop(1)
        self.available_wildcards.insert(1,' ')
        timer = ("\t\t\t 5", "0", "%", " ", "5", "0", "%", " ", "5", "0", "%")
        t = ""
        for i in timer:
            clear()
            print(f"\n\n\n\n\n\n\t{'-'*15} OK, APPLYING... {'-'*15}\n\n\n")
            t += i
            print(t)
            time.sleep(0.3)
        wrong_answer_50 = '' 
        while wrong_answer_50 == '' or wrong_answer_50 == correct_answer:                                                                       
            wrong_answer_50 = random.choice(self.answer_options)
        pos_a = question.find('a)')
        pos_b = question.find('b)')
        pos_c = question.find('c)')
        pos_d = question.find('d)')
        if wrong_answer_50 != 'a' and correct_answer != 'a':
            for character in question:
                if character not in ('\n', '\t'):
                    question = question[:pos_a] + \
                        question[pos_a:pos_b].replace(character, ' ') + \
                        question[pos_b:]
        if wrong_answer_50 != 'b' and correct_answer != 'b':
            for character in question[pos_b:pos_c]:
                if character not in ('\n', '\t'):
                    question = question[:pos_b] + \
                        question[pos_b:pos_c].replace(character, ' ') + \
                        question[pos_c:]
        if wrong_answer_50 != 'c' and correct_answer != 'c':
            for character in question[pos_c:pos_d]:
                if character not in ('\n', '\t'):
                    question = question[:pos_c] + \
                        question[pos_c:pos_d].replace(character, ' ') + \
                        question[pos_d:]
        if wrong_answer_50 != 'd' and correct_answer != 'd':
            for character in question[pos_d:]:
                if character not in ('\n', '\t'):
                    question = question[:pos_d] + \
                        question[pos_d:].replace(character, ' ')

        return question, wrong_answer_50

    def ask_crowd(self, correct_answer, wrong_answer_50=None):
        self.used_wildcards.append('3')
        self.available_wildcards.pop(2)
        self.available_wildcards.insert(2,' ')
        timer = ("\t\t\t C", "?", "R", "?", "O", "?", "W", "?", "D", "?")
        t = ""
        for i in timer:
            clear()
            print(f"\n\n\n\n\n\n\t{'-'*15} OK, ASKING... {'-'*15}\n\n\n")
            t += i
            print(t)
            time.sleep(0.3)
        if self.counter_q <= 5:
            value1 = random.randint(9, 18)
            value2 = random.randint(8, 17)
            value3 = random.randint(10, 21)
        elif self.counter_q >= 6 and self.counter_q <= 10:
            value1 = random.randint(12, 26)
            value2 = random.randint(10, 25)
            value3 = random.randint(11, 26)
        elif self.counter_q >= 11:
            value1 = random.randint(12, 30)
            value2 = random.randint(11, 29)
            value3 = random.randint(13, 32)
        values = [value1, value2, value3]
        v_c_answer = 100 - value1 - value2 - value3   
        # value taken by correct answer  
        crowd_opinion = []
        if wrong_answer_50:
            v_w_answer = random.choice(values) + random.randint(8, 18)
            # value taken by wrong answer
            for answer in self.answer_options:
                if answer == correct_answer:
                    op = f'Option {answer}) {"#" * ((100 - v_w_answer)//2)}'+\
                        f' {100 - v_w_answer}%'
                    crowd_opinion.append(op)
                elif answer == wrong_answer_50:
                    op = f'Option {answer}) {"#" * (v_w_answer//2)} ' + \
                        f'{v_w_answer}%'
                    crowd_opinion.append(op)
        else:
            for answer in self.answer_options:
                if answer == correct_answer:
                    op = f'Option {answer}) {"#" * (v_c_answer//2)} ' + \
                        f'{v_c_answer}%'
                else:
                    get_value = random.choice(values)
                    values.remove(get_value)
                    op = f'Option {answer}) {"#" * (get_value//2)} ' + \
                        f'{get_value}%'
                crowd_opinion.append(op)
        
        return crowd_opinion

    def swap_question(self):
        self.used_wildcards.append('4')
        self.available_wildcards.pop(3)
        self.available_wildcards.insert(3,' ')
        timer = ("\t\t\t  ¿", "?","¿", "?","¿", "?","¿", "?","¿", "?", "¿")
        t = ""
        for i in timer:
            clear()
            print(f"\n\n\n\n\n\n\t{'-'*15} OK, SWAPPING... {'-'*15}\n\n\n")
            t += i
            print(t)
            time.sleep(0.3)