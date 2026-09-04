from colorama import Fore,Style,init
init()
from Utils import decorator_func
import sqlite3
import re


# User Class
class User :
    def __init__(self,user_name,email,password,phone_number):
        self.user_name = user_name 
        self.email = email 
        self.password = password 
        self.phone_number = phone_number


def is_valid_username(username):
    
    pattern1 = r'^[A-Za-z][A-Za-z0-9._]{2,19}$'
    
    pattern2 = r'[._]$'
    
    pattern3 = r'[._]{2}'
    
    if not re.match(pattern1, username):
        return False
    if re.search(pattern2, username):
        return False  
    if re.search(pattern3, username):
        return False
        
    return True
    
def is_valid_phone_number(phone_number):
	pattern1 = r'^[0-9]{2} [0-9]{3} [0-9]{3}$'
	
	pattern2 = r'[A-Za-z.@#$_&-]'
	
	if not re.match(pattern1,phone_number):
		return False
		
	if re.search(pattern2,phone_number):
		return False
		
	return True

def is_valid_password(password):
    
    pattern1 = r'^[A-Za-z0-9@$#&*!%]{8,20}$'
    
    
    pattern2 = r' |([A-Za-z0-9])\1\1'
    
    if not re.match(pattern1, password):
        return False
        
    if re.search(pattern2, password): 
        return False
        
    return True	

def is_valid_email(email):
    
    pattern1 = r'^[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    
    
    pattern2 = r'^\.'
    
      
    pattern3 = r'\.$'
    
    
    pattern4 = r'\.\.'
    
    if not re.match(pattern1, email):
        return False
        
    if re.search(pattern2, email): 
        return False
        
    if re.search(pattern3, email): 
        return False
        
    if re.search(pattern4, email):  
        return False
        
    return True

# Register
@decorator_func("Register")
def Register():
    
    
    while True:
        user_name = input("Enter Name: ")
                
        if not is_valid_username(user_name):
            print(f"{Fore.RED}Incorrect user name{Style.RESET_ALL}")
                
        else :
            break
    while True:
        phone_number = input("Enter Phone Number: ")
    
        if not is_valid_phone_number(phone_number):
            print(f"{Fore.RED}Incorrect phone number{Style.RESET_ALL}")
        
        else:
            break
        
    while True:
        email = input("Enter Email: ")
    
        if not is_valid_email(email):
            print(f"{Fore.RED}Incorrect email{Style.RESET_ALL}")
            
        else:
            break
        
    while True:
        password = input("Enter Password: ")
    
        if not is_valid_password(password):
            print(f"{Fore.RED}Incorrect password{Style.RESET_ALL}")
        
        else:
            break   
        
        
    
    user = User(user_name,email,password,phone_number) 
    
    database_Function(user)

def database_Function(user):
    
    db = sqlite3.connect("app.db")
    
    cr = db.cursor()
    
    cr.execute(
    "create table if not exists users (id INTEGER PRIMARY KEY, user_name text , email text , password text , phone_number text)")
    
    
    cr.execute(
    "SELECT user_name FROM users WHERE user_name = ?",
    (user.user_name,)
)

    result = cr.fetchone()

    if result:
        print("\n❌ This username is already used")
        db.close()
        return
    
    
    cr.execute(
    "SELECT email FROM users WHERE email = ?",
    (user.email,)
)

    result = cr.fetchone()

    if result:
        print("\n❌ This email is already used")
        db.close()
        return
    
    
    cr.execute(
    "SELECT phone_number FROM users WHERE phone_number = ?",
    (user.phone_number,)
)

    result = cr.fetchone()

    if result:
        print("\n❌ This phone number is already used")
        db.close()
        return
    
    
    cr.execute(
    "INSERT INTO users (user_name, email, password, phone_number) VALUES (?, ?, ?, ?)",
    (user.user_name, user.email, user.password, user.phone_number)
)
    
    print("\n✅ Account Created Successfully")
    
    db.commit()
    
    db.close()
