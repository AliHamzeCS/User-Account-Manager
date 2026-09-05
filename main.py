from colorama import Fore, Style, init
init()
import time
import os
import Register
import Login

# Sleep Function
def sleep():
    time.sleep(1)

# Clear Screen Function    
def clear_screen():
    os.system('clear')
    
def clear__and_sleap():
    clear_screen()
    sleep()
    
# Options Function    
def View_Options(*options):
    index = 1
    for option in options:
        print(f'{Fore.CYAN}{index}{Style.RESET_ALL}. {option}')
        index += 1
    
clear_screen()

# Main While
while True:
    #TICKET BOOKING SYSTEM 
    TBS = '🔐 User Account Manager'
    print('='*40)
    print(TBS.center(40,' '))
    print('='*40, end = '\n\n')
    
    View_Options(
        'Register',
        'Login',
        'Show Users',
        'Search User',
        'Update User',
        'Delete User',
        'Statistics',
        'Settings',
        'Help',
        'Exit'
    )
    
    try:
        choice = int(input('\nChoice : '))
        
    except ValueError:
        print('\nError: Please enter a number.')
        sleep()
        clear_screen()
        continue
    
    if choice == 1:
        
        clear__and_sleap()
        Register.Register()
        clear__and_sleap()
        
    elif choice == 2:
       
        clear__and_sleap()
        Login.login()    
        clear__and_sleap() 
       
    elif choice == 3:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 4:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 5:
           
        clear__and_sleap()
           
        clear__and_sleap()
                
    elif choice == 6:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 7:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 8:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 9:
           
        clear__and_sleap()
           
        clear__and_sleap()
           
    elif choice == 10:
           
        clear__and_sleap()
        break