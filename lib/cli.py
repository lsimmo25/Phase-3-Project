# lib/cli.py

from helpers import (
    exit_program,
    list_all_employee,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_all_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_customer,
    update_customer,
    delete_customer,
    all_customers_belonging_to_an_employee

)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_employee()
        elif choice == "2":
            find_employee_by_name()  
        elif choice == "3":
            find_employee_by_id() 
        elif choice == "4":
            create_employee() 
        elif choice == "5":
            update_employee() 
        elif choice == "6":
            delete_employee()
        elif choice == "7":
            list_all_customers()
        elif choice == "8":
            find_customer_by_name()
        elif choice == "9":
            find_customer_by_id()
        elif choice == "10":
            create_customer()
        elif choice == "11":
            update_customer()
        elif choice == "12":
            delete_customer()
        elif choice == "13":
            all_customers_belonging_to_an_employee()
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
    print("1. List all Employees")
    print("2. Find Employee by name")
    print("3. Find Employee by id")
    print("4: Create Employee")
    print("5: Update Employee")
    print("6: Delete Employee")
    print("7. List all customers")
    print("8. Find customer by name")
    print("9. Find customer by id")
    print("10: Create customer")
    print("11: Update customer")
    print("12: Delete customer")
    print("13: List all customers belonging to a Employee")



if __name__ == "__main__":
    main()