import os
import functions
from masterpw import MASTERPW
from mongodb import collection

PASSWORD = input("\nIntroduce the master password: ")

while MASTERPW != PASSWORD:
    if MASTERPW != PASSWORD:
        print("Invalid password! Try again.")
        break

if MASTERPW == PASSWORD:

    while True:
        # show the menu
        functions.menu()
        # we ask the user to introduce an option
        opcionMenu = input("\nInsert an option: ")
        # depends on what the user introduces, we do different things
        if opcionMenu == "1":
            print("\nOk, now you have to introduce some data.")
            pass_id = int(
                input(
                    "\nIntroduce an id for this password (Number between 1 and 1000): "
                ))
            service = input("Introduce the service (Facebook, Gmail...): ")
            user = input("Introduce your user: ")
            password = input("Introduce your password: ")

            functions.addPassword(pass_id, service, user, password)

        elif opcionMenu == "2":
            functions.showAll()

        elif opcionMenu == "3":
            search_service = input(
                "\nOk, introduce the name of the service : ")
            functions.search(search_service)

        elif opcionMenu == "4":
            id_edit = int(
                input(
                    "\nIntroduce the id of the user/password you want to edit : "
                ))
            user_edit = input("Introduce the new username : ")
            pass_edit = input("Introduce the new password : ")
            functions.edit(id_edit, user_edit, pass_edit)

        elif opcionMenu == "5":
            id_remove = int(
                input(
                    "\nOk, introduce the id of the password you want to remove : "
                ))
            functions.removePassword(id_remove)

        elif opcionMenu == "9":
            print("\nHope to see you soon!")
            break
        else:
            print("")
            input(
                "That option is not correct. Please enter a correct option: ")
