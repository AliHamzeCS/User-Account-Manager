import sqlite3
from Utils import decorator_func

# Show Users
@decorator_func("Show Users")
def Show_Users():

    db = sqlite3.connect("app.db")

    cr = db.cursor()

    cr.execute("SELECT id, user_name, email, phone_number FROM users")

    result = cr.fetchall()

    if not result:
        print("\nNo users found")

    else:
        for user in result:
            print("=" * 25, end="\n\n")
            print(f"ID : {user[0]}")
            print(f"Username : {user[1]}")
            print(f"Email : {user[2]}")
            print(f"Phone Number : {user[3]}\n")
            print("=" * 25, end="\n\n")

    db.close()