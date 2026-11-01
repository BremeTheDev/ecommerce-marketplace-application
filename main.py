print("=================================")
print("|| Welcome to PhoneCart!       ||")
print("|| Your Electronics Store      ||")
print("=================================")



from connect import connectDB
from verify_database import verifyDatabase
from verify_tables import verifyTables
from login_register import loginRegister
from browse_products import browseProducts
from view_cart import viewCart
from order_history import orderHistory



password = connectDB()
verifyDatabase(password)
verifyTables(password)

while True:

    try:

        print("\n=================================================")
        print("||       PhoneCart ELECTRONICS STORE           ||")
        print("=================================================")
        print("|   1 -> Register / Login / Switch accounts     |")
        print("|   2 -> Browse Products                        |")
        print("|   3 -> View Cart                              |")
        print("|   4 -> Place Order                            |")
        print("|   5 -> Order History                          |")
        print("=================================================")
        choice_main = input("Choice:")
        print("=================================================")



        with open("login_verification.txt", "r") as file:
            verification = file.read()




        if verification == "False":

            if choice_main == "1":

                username_verification = loginRegister(password)

                if username_verification != None:

                    while True:
                        print("\n----------------------------------------")
                        print("| Do you want to stay logged in? (Y/N) |")
                        print("----------------------------------------")
                        choice_save_login = input("Choice:")
                        print("----------------------------------------")
                        if choice_save_login in "Yy":
                            with open("saved_accounts.txt", "a") as file:
                                file.write(username_verification + "\n")
                            with open("current_account.txt", "w") as file:
                                file.write(username_verification)
                            break
                        elif choice_save_login in "Nn":
                            with open("current_account.txt", "w") as file:
                                file.write(username_verification)                        
                            break
                        else:
                            print("\n-------------------")
                            print("| Invalid choice! |")
                            print("-------------------")

                if username_verification != None:
                    with open("login_verification.txt", "w") as file:
                        file.write("True")
                    with open("current_account.txt", "w") as file:
                        file.write(username_verification)
            

            else:
                print("\n-------------------------------------------------------------")
                print("| Please sign-in/log-in to continue using this application! |")
                print("-------------------------------------------------------------")




        else:

            with open("saved_accounts.txt", "r") as file:
                accounts = file.readlines()

            with open("current_account.txt", "r") as file:
                username = file.read()


            print("\n____________________________")
            print("")
            print(" Current account:", username.strip())
            print("____________________________")


            if choice_main == "1":

                if len(accounts)>1:

                    while True:
                        
                        print("\n--------------------------------------")
                        print("| 1 -> Switch accounts               |") 
                        print("| 2 -> Login/Sign-in another account |")
                        print("| 3 -> Back                          |")
                        print("--------------------------------------")
                        choice = input("Choice:")
                        print("--------------------------------------")

                        if choice == "1":

                            while True:

                                with open("saved_accounts.txt", "r") as file:
                                    accounts = file.readlines()
                                print("\n----------------------")
                                print("| Logged in accounts |")
                                print("----------------------")
                                number = 1
                                for account in accounts:
                                    print(number, "->", account[:len(account)-1])
                                    number += 1
                                print("----------------------")
                                choice = input("Choose your account:")
                                print("----------------------")
                                if choice.isdigit():
                                    if int(choice) > 0 and int(choice) <= len(accounts):
                                        username = accounts[int(choice) - 1]
                                        with open("current_account.txt", "w") as file:
                                            file.write(username)
                                            break
                                    else:
                                        print("\n-------------------")
                                        print("| Invalid choice! |")
                                        print("-------------------")
                                else:
                                    print("\n-------------------")
                                    print("| Invalid choice! |")
                                    print("-------------------")
                            break

                        elif choice == "2":

                            username_new = loginRegister(password)
                            if username_new != None:
                                username = username_new
                                while True:
                                    print("\n----------------------------------------")
                                    print("| Do you want to stay logged in? (Y/N) |")
                                    print("----------------------------------------")
                                    choice_save_login = input("Choice:")
                                    print("----------------------------------------")
                                    if choice_save_login in "Yy":
                                        with open("saved_accounts.txt", "a") as file:
                                            file.write(username + "\n")
                                        with open("current_account.txt", "w") as file:
                                            file.write(username)
                                        break
                                    elif choice_save_login in "Nn":
                                        with open("current_account.txt", "w") as file:
                                            file.write(username)
                                        break
                                    else:
                                        print("\n-------------------")
                                        print("| Invalid choice! |")
                                        print("-------------------")

                        elif choice == "3":
                            break
                        

                        else:
                            print("\n-------------------")
                            print("| Invalid choice! |")
                            print("-------------------")



                else:

                    username_new = loginRegister(password)

                    if username_new != None:
                        username = username_new
                        while True:
                            print("\n----------------------------------------")
                            print("| Do you want to stay logged in? (Y/N) |")
                            print("----------------------------------------")
                            choice_save_login = input("Choice:")
                            print("----------------------------------------")
                            if choice_save_login in "Yy":
                                with open("saved_accounts.txt", "a") as file:
                                    file.write(username + "\n")
                                with open("current_account.txt", "w") as file:
                                    file.write(username)
                                break
                            elif choice_save_login in "Nn":
                                break
                            else:
                                print("\n-------------------")
                                print("| Invalid choice! |")
                                print("-------------------")




            elif choice_main == "2":
                browseProducts(username, password)

            elif choice_main == "3":
                viewCart(username, password)

            elif choice_main == "4":
                viewCart(username, password)

            elif choice_main == "5":
                orderHistory(username, password)


            else:
                print("\n-------------------")
                print("| Invalid choice! |")
                print("-------------------")
                continue




    except:
        print("\n-------------------")
        print("| Invalid choice! |")
        print("-------------------")
        continue
