# lib/cli.py

from helpers import (
    exit_program,
    list_all_sales_people,
    find_sales_person_by_name,
    find_sales_person_by_id,
    create_sales_person,
    update_sales_person,
    delete_sales_person

)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_sales_people()
        elif choice == "2":
            find_sales_person_by_name()  
        elif choice == "3":
            find_sales_person_by_id() 
        elif choice == "4":
            create_sales_person() 
        elif choice == "5":
            update_sales_person() 
        elif choice == "6":
            delete_sales_person()
        else:
            print("Invalid choice")


def menu():
    print(r"""
        ______           _               _     _        ______      _        _                    
        |  _  \         | |             | |   (_)       |  _  \    | |      | |                   
        | | | |___  __ _| | ___ _ __ ___| |__  _ _ __   | | | |__ _| |_ __ _| |__   __ _ ___  ___ 
        | | | / _ \/ _` | |/ _ \ '__/ __| '_ \| | '_ \  | | | / _` | __/ _` | '_ \ / _` / __|/ _ \
        | |/ /  __/ (_| | |  __/ |  \__ \ | | | | |_) | | |/ / (_| | || (_| | |_) | (_| \__ \  __/
        |___/ \___|\__,_|_|\___|_|  |___/_| |_|_| .__/  |___/ \__,_|\__\__,_|_.__/ \__,_|___/\___|
                                                | |                                               
                                                |_|  
    """)
    print(r"""
                                            /\\      _____          _____       |   |     |
            ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ 
        ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \
        ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
        `````````````````````````````````````````````````````````````````````````````````````
    """)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Sales People")
    print("2. Find Sales Person by name")
    print("3. Find Sales Person by id")
    print("4: Create Sales Person")
    print("5: Update Sales Person")
    print("6: Delete Sales Person")
    print("7. List all customers")
    print("8. Find customer by name")
    print("9. Find customer by id")
    print("10: Create customer")
    print("11: Update customer")
    print("12: Delete customer")
    print("13: List all customers belonging to a Sales Person")



if __name__ == "__main__":
    main()