def show_info_credits():
    credits = {
        'game name' : 'Quizzy',
        'version' : 'v2.0',
        'author' : 'Pablo Ortega',
        'year' : '2021',
        'code lenguage' : 'Python',
        }
    info = {
        'questions' : (
            'You can add your own questions editing the quizzy_questions.txt.'
            '\n\tTo do it just add your question and answer with the following'
            ' format:\n\n\tquestion; wrong_answer; wrong_answer; wrong_answer;'
            ' correct_answer\n\n\tOne question per line. Save the file. Enjoy!!'
            ),
        'files' : (
            'QUIZZY, quizzy_files and quizzy_data '
            'MUST BE in the SAME directory.'
            )
        }
    print(f'{"#"*16}| INFO & CREDITS |{"#"*16}\n\n')
    print(f'--- CREDITS {"-"*40}\n')
    for k, v in credits.items():
        print(f'\t· {k.capitalize()} ---- {v}\n')
    print(f'\n--- INFO {"-"*43}\n')
    for k, v in info.items():
        print(f'· {k.capitalize()}:\n\n\t{v}\n\n')
    input('\n\n\tPress ENTER to exit...')