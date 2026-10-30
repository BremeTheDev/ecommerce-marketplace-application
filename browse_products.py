import mysql.connector as sqlcon
import random




def browse(brand, product, category, username):

    while True:

        cursor.execute("select product_id, product, units, price, description from products where product like %s and category = %s",
                       (product+"%", category))
        products = cursor.fetchall()

        while True:

            try:

                design = ""
                for characters in range(len("|| " + brand + " " + category + "s" + " ||")):
                    design += "="

                
                print("\n" + design)
                print("|| " + brand + " " + category + "s" + " ||")
                print(design)
                number = 1
                for product_tuple in products:
                    print(number, "->", product_tuple[1], "(₹"+str(product_tuple[3])+")")
                    number+=1
                print(number+1, "-> Back")
                print("===================")
                choice = input("Choice:")
                print("===================")

                if int(choice) == number+1:
                    return "continue in same section"

                index = int(choice)-1
                units = []
                description_raw = products[index][4].split(",")
                description_processed = ""
                for description in description_raw:
                    description_processed += "\n-" + str(description)

                if products[index][2] == 0:
                    units.append("Out of stock")
                else:
                    units.append(products[index][2])

                design_2_equal = ""
                design_2_minus = ""
                for design in range(len((products[index][1]))):
                    design_2_equal += "="
                    design_2_minus += "-"
                    
                print("\n" + design_2_equal)
                print(products[index][1])
                print(design_2_minus)
                print("Description:", description_processed)
                print("Price:", "₹" + str(products[index][3]))
                print("Available Units:", units[0])

            except:
                print("\n-------------------")
                print("| Invalid choice! |")
                print("-------------------")
                continue

            print("======================")
            print("|| 1 -> Buy now     ||")
            print("||------------------||")
            print("|| 2 -> Add to cart ||")
            print("||------------------||")
            print("|| 3 -> Back        ||")
            print("======================")
            choice_order = input("Choice:")
            print("======================")


            if choice_order == "1":

                if units[0] == "Out of stock":
                    print("\n----------------------------------")
                    print("| Selected item is out of stock! |")
                    print("----------------------------------")
                    break

                else:

                    while True:

                        print("\n===========================")
                        print("||     PAYMENT MODE      ||")
                        print("---------------------------")
                        print("|| 1 -> UPI              ||")
                        print("|| 2 -> Cash on delivery ||")
                        print("===========================")
                        choice = input("Choice:")
                        print("===========================")


                        if choice == "1" or choice == "2":

                            
                            cursor.execute("insert into orders values (%s, %s, %s, %s)",
                                        (username, products[index][0], products[index][1], products[index][3]))
                            database.commit()
                            cursor.execute("update products set units = units-1 where product_id = %s",
                                            (products[index][0],))
                            database.commit()

                            print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                            print("  Order placed! Thank you for choosing PhoneCart Electronics Store!")
                            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                            print("  Your order will be arriving in", random.randint(1,12), "days.")
                            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                            
                            while True:

                                print("\n-------------------------------------------------")
                                choice = input("Do you want to continue shopping? (Y/N):")
                                print("-------------------------------------------------")

                                if choice in "Yy":
                                    return "continue"

                                elif choice in "Nn":
                                    return "exit"

                                else:
                                    print("\n-------------------")
                                    print("| Invalid choice! |")
                                    print("-------------------")
                                    continue
                        
                        else:
                            print("\n-------------------")
                            print("| Invalid choice! |")
                            print("-------------------")
                            continue





            elif choice_order == "2":

                if units[0] == "Out of stock":
                    print("\n----------------------------------")
                    print("| Selected item is out of stock! |")
                    print("----------------------------------")
                    break

                else:
                    
                    cursor.execute("insert into cart values (%s, %s, %s, %s)", (
                        username, products[index][0], products[index][1],
                        products[index][3]
                    ))
                    database.commit()

                    print("\n-----------------------")
                    print("| Item added to cart! |")
                    print("-----------------------")

                    while True:

                        print("\n-------------------------------------------------")
                        choice = input("Do you want to continue shopping? (Y/N):")
                        print("-------------------------------------------------")

                        if choice in "Yy":
                            return "continue"
                        
                        elif choice in "Nn":
                            return "exit"
                        
                        else:
                            print("\n-------------------")
                            print("| Invalid choice! |")
                            print("-------------------")
                            continue



            elif choice_order == "3":
                return "continue in same section"


            else:
                print("\n-------------------")
                print("| Invalid choice! |")    
                print("-------------------")
                continue
























def browseProducts(username, password):


    database = sqlcon.connect(
        host = "localhost",
        user = "root",
        password = password,
        db = "phonecart"
    )
    cursor = database.cursor()
    cursor.execute("use phonecart")



    while True:

        print("\n=======================")
        print("||  BROWSE PRODUCTS  ||")
        print("=======================")
        print("| 1 -> Laptops        |")
        print("| 2 -> Smartphones    |")
        print("| 3 -> Headphones     |")
        print("| 4 -> Monitors       |")
        print("| 5 -> Graphics Cards |")
        print("| 6 -> Back           |")
        print("=======================")
        choice = input("Choice:")
        print("=======================")






        if choice == "1":

            while True:
                    
                print("\n=====================")
                print("||  LAPTOP BRANDS  ||")
                print("=====================")
                print("|   1 -> Apple      |")
                print("|   2 -> Dell       |")
                print("|   3 -> Lenovo     |")
                print("|   4 -> ASUS       |")
                print("|   5 -> Back       |")
                print("=====================")
                choice = input("Choice:")
                print("=====================")

                #laptops
                if choice == "1":

                    result = browse("Apple", "macbook", "Laptop", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue
                    elif result == "continue":
                        break

                elif choice == "2":

                    result = browse("Dell", "dell", "Laptop", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break                                        

                elif choice == "3":

                    result = browse("Lenovo", "lenovo", "Laptop", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break                    

                elif choice == "4":

                    result = browse("ASUS", "asus", "Laptop", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                      
                    elif result == "continue":
                        break                                      

                elif choice == "5":
                    break
                
                else:
                    print("\n-------------------")
                    print("| Invalid choice! |")    
                    print("-------------------")
                    continue






        elif choice == "2":

            while True:

                print("\n=======================")
                print("|| SMARTPHONE BRANDS ||")
                print("=======================")
                print("|   1 -> Apple        |")
                print("|   2 -> Samsung      |")
                print("|   3 -> Google       |")
                print("|   4 -> Back         |")
                print("=======================")
                choice = input("Choice:")
                print("=======================")

                #mobiles
                if choice == "1":

                    result = browse("Apple", "iphone", "mobile", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                     
                    elif result == "continue":
                        break                    

                elif choice == "2":

                    result = browse("Samsung", "samsung", "mobile", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break                    

                elif choice == "3":

                    result = browse("Google", "google", "mobile", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break                     

                elif choice == "4":
                    break
                
                else:
                    print("\n-------------------")
                    print("| Invalid choice! |")    
                    print("-------------------")
                    continue




        #headphones            
        elif choice == "3":

            while True:
                
                print("\n======================")
                print("|| HEADPHONE BRANDS ||")
                print("======================")
                print("|   1 -> Sony        |")
                print("|   2 -> Bose        |")
                print("|   3 -> Back        |")
                print("======================")     
                choice = input("Choice:")
                print("======================")

                if choice == "1":

                    result = browse("Sony", "sony", "headphones", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break

                elif choice == "2":

                    result = browse("Bose", "bose", "headphones", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break    

                elif choice == "3":
                    break

                else:
                    print("\n-------------------")
                    print("| Invalid choice! |")    
                    print("-------------------")
                    continue




        #monitors
        elif choice == "4":

            while True:

                print("\n======================")
                print("|| MONITOR BRANDS   ||")
                print("======================")
                print("|   1 -> LG          |")
                print("|   2 -> Dell        |")
                print("|   3 -> Back        |")
                print("======================")     
                choice = input("Choice:")
                print("======================")



                if choice == "1":

                    result = browse("LG", "lg", "monitor", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break

                elif choice == "2":

                    result = browse("Dell", "dell", "monitor", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break    

                elif choice == "3":
                    break

                else:
                    print("\n-------------------")
                    print("| Invalid choice! |")    
                    print("-------------------")
                    continue      



        #graphics card
        elif choice == "5":

            while True:

                print("\n==========================")
                print("|| GRAPHICS CARD BRANDS ||")
                print("==========================")
                print("|   1 -> NVIDIA          |")
                print("|   2 -> ASUS            |")
                print("|   3 -> Back            |")
                print("==========================")     
                choice = input("Choice:")
                print("==========================")

                if choice == "1":

                    result = browse("NVIDIA", "nvidia", "graphics card", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break                                

                elif choice == "2":

                    result = browse("ASUS", "asus", "graphics card", username)
                    if result == "exit":
                        return
                    elif result == "continue in same section":
                        continue                    
                    elif result == "continue":
                        break 

                elif choice == "3":
                    break
                

                else:
                    print("\n-------------------")
                    print("| Invalid choice! |")    
                    print("-------------------")
                    continue 
                 


        elif choice == "6":
            return





        else:
            print("\n-------------------")
            print("| Invalid choice! |")
            print("-------------------")
            continue
