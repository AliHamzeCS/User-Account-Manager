import sqlite3
from Utils import decorator_func

# Update User
@decorator_func("Update User")
def Update_User():
    
    db = sqlite3.connect("app.db") 
    cr = db.cursor()
    
    username = input("Enter username: ")
    
    
    cr.execute("SELECT id FROM users WHERE user_name = ?", (username,))
    if not cr.fetchone():
        print("\nUser not found")
        db.close()
        return
    
    while True :
        print("\n1. Username")
        print("2. Email")
        print("3. Password")
        print("4. Phone Number")
        print("5. Back\n")
        
        try :
            choice = int(input("choice: ")) 
        except ValueError :
            print("Please enter only number of choice")
            continue 
            
        if choice == 1:
            new_username = input("Enter new username: ")
            cr.execute("UPDATE users SET user_name = ? WHERE user_name = ?", (new_username, username))
            db.commit() 
            print(f"\nUsername is updated to {new_username}")
            username = new_username 
            
        elif choice == 2:
            new_email = input("Enter new email: ")
            cr.execute("UPDATE users SET email = ? WHERE user_name = ?", (new_email, username))
            db.commit()
            print(f"\nEmail is updated to {new_email}")
            
        elif choice == 3:
            new_password = input("Enter new password: ")
            cr.execute("UPDATE users SET password = ? WHERE user_name = ?", (new_password, username))
            db.commit()
            print("\nPassword is updated")
            
        elif choice == 4:
            new_phone = input("Enter new phone number: ")
            cr.execute("UPDATE users SET phone_number = ? WHERE user_name = ?", (new_phone, username))
            db.commit()
            print(f"\nPhone Number is updated to {new_phone}")
            
        elif choice == 5:
            print("Back to main menu")
            break
            
        else:
            print("Invalid choice, please try again")
            
    db.close()