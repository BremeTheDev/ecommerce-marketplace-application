import mysql.connector as sqlcon

def verifyDatabase(password):

    database = sqlcon.connect(
        host = "localhost",
        user = "root",
        password = password,
    )

    cursor = database.cursor()
    cursor.execute("show databases")
    existing_databases = cursor.fetchall()

    if ("phonecart",) in existing_databases:
        return

    else:
        print("\n--------------------------")
        print("| Database not found!    |")
        print("--------------------------")
        print("| Creating a database... |")
        print("--------------------------")
        cursor.execute("create database phonecart")
        cursor.execute("use phonecart")

        cursor.execute("create table users(User_ID int not null primary key," \
        "Username varchar(100), Email varchar(50), Password varchar(100))")
        database.commit()

        cursor.execute("create table products(Product_ID int not null primary key," \
        "Product varchar(1000), Units int, Price float, Category varchar(100)," \
        "Description varchar(10000))")
        database.commit()

        cursor.execute("create table cart(Username varchar(100) not null," \
        "Product_ID int not null, Product varchar(100), Price float)")

        cursor.execute("create table orders (Username varchar(1000)," \
        "Product_ID int, Product varchar(1000), Price int)")

        database.commit()