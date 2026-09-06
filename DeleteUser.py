import sqlite3
from Utils import decorator_func

# Delete User
@decorator_func("Delete User")
def Delete_User():

    db = sqlite3.connect("app.db")
    cr = db.cursor()

    username = input("Enter username to delete: ")


    cr.execute("SELECT id, user_name, email FROM users WHERE user_name =?", (username,))
    result = cr.fetchone()

    if not result:
        print("\nNo user found with this username")
        db.close()
        return
        
    print("\n" + "=" * 30)
    print(f"ID : {result[0]}")
    print(f"Username : {result[1]}")
    print(f"Email : {result[2]}")
    print("=" * 30)

   
    confirm = input(f"\nAre you sure you want to delete this user? [y/n]: ").lower()

    if confirm == 'y':
        cr.execute("DELETE FROM users WHERE user_name =?", (username,))
        db.commit()
        print(f"\nUser '{username}' deleted successfully")
    else:
        print("\nDelete cancelled")

    db.close()