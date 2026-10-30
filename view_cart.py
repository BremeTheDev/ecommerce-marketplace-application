import mysql.connector as sqlcon
import random

def viewCart(username, password):



    database = sqlcon.connect(
        host = "localhost",
        user = "root",
        password = password,
        db = "phonecart"
    )
    cursor = database.cursor()
    cursor.execute("use phonecart")

    cursor.execute("select product, price, product_id from cart where username = %s",
                   (username,))
    result_cart = cursor.fetchall()
    cursor.execute("select sum(price) from cart where username = %s",
                   (username,))
    result_total_amount = cursor.fetchone()

    if result_cart == []:
        print("\n--------------------")
        print("| No items in cart |")
        print("--------------------")
        return

    else:

        while True:

            cursor.execute("select product, price, product_id from cart where username = %s",
                           (username,))
            result_cart = cursor.fetchall()

            if result_cart == []:
                return
            
            print("\n=========================")
            print("||        CART         ||")
            print("=========================")
            for product in result_cart:
                print(product[0], "(₹" + str(product[1]) + ")")
            print("Grand Total: ₹" + str(result_total_amount[0]))
            print("=========================")
            print("|| 1 -> Checkout       ||")
            print("|| 2 -> Remove an item ||")
            print("|| 3 -> Back           ||")
            print("=========================")
            choice = input("Choice:")
            print("=========================")

            if choice == "1":

                while True:

                    print("\n===========================")
                    print("||     PAYMENT MODE      ||")
                    print("---------------------------")
                    print("|| 1 -> UPI              ||")
                    print("|| 2 -> Cash on delivery ||")
                    print("|| 3 -> Back             ||")
                    print("===========================")
                    choice = input("Choice:")
                    print("===========================")


                    if choice == "1" or choice == "2":

                        for product in result_cart:
                            
                            cursor.execute("insert into orders values (%s, %s, %s, %s)",
                                        (username, product[2], product[0], product[1]))
                            database.commit()
                            
                            cursor.execute("update products set units = units-1 where product_id = %s",
                                            (product[2],))
                            database.commit()
                            cursor.execute("delete from cart where username = %s",
                                           (username,))
                            database.commit()
                            

                        print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                        print("  Order placed! Thank you for choosing PhoneCart Electronics Store!")
                        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                        print("  Your order will be arriving in", random.randint(1,12), "days.")
                        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                        return

                    elif choice == "3":
                        break

                    else:

                        print("\n-------------------")
                        print("| Invalid choice! |")
                        print("-------------------")



            elif choice == "2":

                while True:

                    print("\n====================================")
                    print("|| SELECT THE ITEM TO REMOVE      ||")
                    print("====================================")
                    number = 1
                    for product in result_cart:
                        print(number, "->", product[0])
                        number += 1
                    print("------------------------------------")
                    print("|| 1 -> Back                      ||")
                    print("------------------------------------")
                    choice = input("Choice:")
                    print("====================================")

                    if choice == "1":
                        break

                    elif choice.isdigit() and 1 <= int(choice) <= len(result_cart):
                        cursor.execute("delete from cart where product_id = %s",
                                        (result_cart[int(choice) - 1][2],))
                        database.commit()
                        break


                    else:
                        print("\n-------------------")
                        print("| Invalid choice! |")
                        print("-------------------")    
                        continue




            elif choice == "3":
                return
                           
                                          

            else:
                print("\n-------------------")
                print("| Invalid choice! |")
                print("-------------------")
