import sqlite3
from Utils import decorator_func

# Login
@decorator_func("Login")
def login():
    db = sqlite3.connect("app.db")
    cr = db.cursor()

    user_name = input("Enter Username: ")
    password = input("Enter password: ")

    cr.execute("SELECT user_name FROM users WHERE user_name =? AND password =?", (user_name, password))

    result = cr.fetchone()

    db.close()

    if result:
        print("\n✅ Login successful! Welcome", result[0])
        return True
    else:
        print("\n❌ Invalid username or password")
        return False
    
