import mysql.connector as sqlcon


def orderHistory(username, password):

    database = sqlcon.connect(
        host = "localhost",
        user = "root",
        password = password,
        db = "phonecart"
    )
    cursor = database.cursor()
    cursor.execute("use phonecart")    

    cursor.execute("select product, price from orders where username = %s",
                   (username,))
    order_details = cursor.fetchall()

    if order_details == []:
        print("\n------------------------------------------------")
        print("| Looks like you haven't ordered anything yet! |")
        print("------------------------------------------------")
        return
    
    print("\n=================")
    print("| Order History |")
    print("=================")
    for order in order_details:
        print(order[0])
    print("-----------------")
    print("| 1 -> Back     |")
    print("-----------------")
    choice = input("Choice:")
    print("=================")

    if choice == "1":
        return

    else:
        print("-------------------")
        print("| Invalid choice! |")
        print("-------------------")