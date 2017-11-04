from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.db_product


def main():
    while (1):
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            print ('delete')
            delete()
        else:
            print ('\n INVALID SELECTION \n')


def insert():
    try:
        id_product = input('Enter id product :')
        name_product = input('Enter name product :')
        qty = input('Enter qty :')

        db.product.insert_one(
            {
                "id": id_product,
                "name_product": name_product,
                "qty": qty
            })
        print ('\nInserted data successfully\n')

    except Exception as e:
        print (str(e))


def update():
    try:
        id_product = input('\nEnter id to update\n')
        name_product = input('\nEnter name product to update\n')
        qty = input('\nEnter qty to update\n')

        db.product.update_one(
            {"id": id_product},
            {
                "$set": {
                    "name_product": name_product,
                    "qty": qty
                }
            }
        )
        print ("\nRecords updated successfully\n")

    except Exception as e:
        print (str(e))

def read():
    try:
        empCol = db.product.find()
        print ('\n All data from Product Database \n')
        for emp in empCol:
            print (emp)

    except Exception as e:
        print (str(e))

def delete():
    try:
        id_product = input('\nEnter id product to delete\n')
        db.product.delete_one({"id": id_product})
        print ('\nDeletion successful\n')
    except Exception as e:
        print (str(e))


main()