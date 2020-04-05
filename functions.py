from mongodb import collection


def menu():

    #os.system('cls')  # For Windows you have to use cls instead of clear
    print("\nWelcome! What do you want to do?")
    print("\n\t1 - Add a new password")
    print("\t2 - Show all my passwords")
    print("\t3 - Search for a specific password")
    print("\t4 - Edit a password")
    print("\t5 - Remove a password")
    print("\t9 - Exit")


def addPassword(id, service, user, password):

    new_password = {
        "_id": id,
        "service": service,
        "user": user,
        "password": password
    }
    collection.insert_one(new_password)
    print("\nPassword succesfully added to the database.")


def showAll():

    results = collection.find({})

    print("\nSure. These are all your passwords.")
    for result in results:
        print("")
        print(result)


def search(service):
    results = collection.find({"service": service})

    for result in results:
        print("")
        print(result)


def edit(id, user, password):
    collection.update_one({"_id": id},
                          {"$set": {
                              "user": user,
                              "password": password
                          }})
    print("\nSuccesfully updated!")


def removePassword(id_remove):
    collection.delete_one({"_id": id_remove})
    print("\nSuccessfully removed!")
