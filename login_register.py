import random
import mysql.connector as sqlcon

def loginRegister(password):

    def register():
        cursor.execute("select user_id from users")
        DBuserID = cursor.fetchall()
        generatedID = ("")
        while generatedID == (""):
            randID = random.randint(100,999)
            if (randID,) not in DBuserID:
                generatedID+=str(randID)

        cursor.execute("select email from users")
        DBemail = cursor.fetchall()
        while True:
            email = input("\nEnter your E-Mail to be registered:")
            if (email,) in DBemail:
                print("-------------------------------------------")
                print("| E-Mail already exists! Try another one! |")
                print("-------------------------------------------")
            else:
                break

        cursor.execute("select username from users")
        DBusername = cursor.fetchall()
        while True:
            username = input("\nCreate a username:")
            if (username,) in DBusername:
                print("\n----------------------------")
                print("| Username already exists! |")
                print("----------------------------")
            else:
                break

        password = input("\nCreate a password:")

        cursor.execute("insert into users values(%s,%s,%s,%s)", (generatedID, username, email, password))
        database.commit()

        print("\n--------------------")
        print("| Account created! |")
        print("--------------------")

        return username


    def login():
        cursor.execute("select email from users")
        DBemail = cursor.fetchall()
        email = input("\nEnter your registered E-mail:")

        if (email,) in DBemail:

            cursor.execute("select username from users")
            DBusername = cursor.fetchall()
            username = input("\nEnter your username:")

            if (username,) in DBusername:

                cursor.execute("select password from users")
                DBpassword = cursor.fetchall()
                password = input("\nEnter your password:")

                if (password,) in DBpassword:
                    print("\n---------------------")
                    print("| Login Successful! |")
                    print("---------------------")
                    return username

                else:
                    print("\n-----------------------")
                    print("| Incorrect password! |")
                    print("-----------------------")
            else:
                print("\n-----------------------")
                print("| Incorrect username! |")
                print("-----------------------")
        else:
            print("\n------------------------------------------------------------------")
            print("| E-mail not found! Please make sure you've registered it first! |")
            print("------------------------------------------------------------------")
            while True:
                print("\n====================")
                print("| 1 -> Register    |")
                print("| 2 -> Retry login |")
                print("| 3 -> Back        |")
                print("====================")
                choice = input("Choice:")
                print("====================")
                if choice == "1":
                    return register()
                elif choice == "2":
                    return login()
                elif choice == "3":
                    return loginRegister()
                else:
                    print("Invalid choice! Try again!")


    database = sqlcon.connect(
        host = "localhost",
        user = "root",
        password = password,
        db = "phonecart"
    )
    cursor = database.cursor()
    cursor.execute("use phonecart")


    
    username = None
    print("\n=====================")
    print("|| SIGN UP / LOGIN ||")
    print("=====================")
    print("|  1 -> Sign up     |")
    print("|  2 -> Log in      |")
    print("|  3 -> Go back     |")
    print("=====================")
    while True:
        choice = input("Choice:")
        print("=====================")
        if choice == "1":
            username = register()
            return username
        elif choice == "2":
            username = login()
            return username
        elif choice == "3":
            return username
        else:
            print("\n--------------------------------")
            print("| Incorrect choice! Try again! |")
            print("--------------------------------")
