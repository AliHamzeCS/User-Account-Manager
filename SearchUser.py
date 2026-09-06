import sqlite3
from Utils import decorator_func

# Search User
@decorator_func("Search User")
def Search_User(): 
    username = input("Enter username to search: ")

    db = sqlite3.connect("app.db")
    cr = db.cursor()

    cr.execute("SELECT id, user_name, email, phone_number FROM users WHERE user_name =?", (username,))

    result = cr.fetchone()

    if not result:
        print("\nNo users found")
    else:
        print("=" * 25)
        print(f"ID : {result[0]}")
        print(f"Username : {result[1]}")
        print(f"Email : {result[2]}")
        print(f"Phone Number : {result[3]}")
        print("=" * 25)

    db.close()