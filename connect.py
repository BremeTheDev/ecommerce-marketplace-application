import mysql.connector as sqlcon
def connectDB():
    while True:
        try:

            password = input("\nEnter your MySQL database password:")
            database = sqlcon.connect(
                host = "localhost",
                user = "root",
                password = password,
            )
            return password

        except:

            print("\n----------------------------------")
            print("| Incorrect Password! Try again! |")
            print("----------------------------------")