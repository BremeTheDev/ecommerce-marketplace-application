import mysql.connector as sqlcon
import random
from products_dataset import products



def verifyTables(password):

    database = sqlcon.connect(
    host = "localhost",
    user = "root",
    password = password,
    db = "phonecart"
    )
    cursor = database.cursor()
    cursor.execute("use phonecart")

    with open("products_generated.txt", "r") as file:
        generated = file.read()

    if generated == "True":
        return

    else:
        with open("products_generated.txt", "w") as file:
            file.write("True")
        used_ids = []
        data = []
        for product in products:
            while True:
                generated_id = random.randint(1000000,99999999)

                if generated_id in used_ids:
                    continue

                else:
                    used_ids.append(generated_id)
                    data.append((
                        generated_id,
                        product[0],
                        product[1],
                        product[2],
                        product[3],
                        product[4]
                    ))
                    break

        cursor.executemany("insert into products values (%s,%s,%s,%s,%s,%s)", data)
        database.commit()