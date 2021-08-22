import os
import time
from quizzy_files.main import main
from quizzy_files.intro import show_intro
from quizzy_files.global_functions import clear

if __name__ == '__main__':
    os.system('mode con: cols=101 lines=37')
    show_intro()
    main()
    clear()
    print('\n\n\n\n\n\t\t\tTHANKS FOR PLAY QUIZZY!!!')
    time.sleep(2)
    clear()
