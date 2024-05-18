from helpers import (
    exit_program,
    list_all_employees,
    select_employee,
    create_employee
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_employees()
        elif choice == "2":
            select_employee()
        elif choice == "3":
            create_employee()
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
                                            /\\      _____  pyth        _____       |   |     |
            ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ 
        ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \
        ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
        `````````````````````````````````````````````````````````````````````````````````````
    """)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Employees")
    print("2. Select an Employee")
    print("3. Create Employee")

if __name__ == "__main__":
    main()