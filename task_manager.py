#=====importing libraries===========
import datetime


#====Defined Functions========
def read_users_file():
    """Function reads the file user.txt in order to store users in
    a dictionary.

    Returns:
        dictionary: Conatins all the users read from user.txt
    """
    # Creating dictionary
    user_dict = {}

    try:
        user_file = open("./user.txt", "r")
        contents = user_file.readlines()

        for user in contents:
            user_dict[user.strip().split(", ")[0]] = user.strip().split(", ")[1]

    except FileNotFoundError:
        if user_login == "Y":
            print("No Users Registered")

    return user_dict


def menu_display_admin():
    print("\nr - register a user\na - add task")
    print("va - view all tasks\nvm - view my tasks")
    print("s - Statistics\ne - exit")
    print("...............")


def menu_display_user():
    print("\na - add task")
    print("va - view all tasks\nvm - view my tasks\ne - exit")
    print("...............")


def register_new_user(new_username, new_password):
    """Takes in new username and new password and stores
    them in the user.txt file.

    Args:
        new_username (any) 
        new_password (any)
    """

    try:
        user_file = open("./user.txt", "r")
        user_file = open("./user.txt", "a")
        user_file.write(f"\n{new_username}, {new_password}")
        user_file.close()
    except FileNotFoundError:
        if user_login == "Y":
            print("User file not found")
        

def print_tasks(list_of_tasks):

    print(f"""
Task:\t\t\t{list_of_tasks[1]}
Assigned to:\t\t{list_of_tasks[0]}
Date assigned:\t\t{list_of_tasks[3]}
Due date:\t\t{list_of_tasks[4]}
Task complete?\t\t{list_of_tasks[5]}
Task description:\n{list_of_tasks[2]}
""")


def read_tasks():
    """Reads the file tasks.txt and stores each line in a list

    Returns:
        list: list containing information from tasks.txt
    """
    try:
        tasks_file = open("./tasks.txt", "r")
        contents = tasks_file.readlines()
        list_of_tasks = []

        for line in contents:
            list_of_tasks += line.strip().split(", "),

        return list_of_tasks
    
    except FileNotFoundError:
        if user_login == "Y":
            print("Tasks file not found")
                

def add_task(task, assigned_to, date_assigned, due_date, completion, description):
    """Task in the arguments listed below and prints them out to the file
tasks.txt

    Args:
        task (any): The task to be assigned
        assigned_to (any): user the task will be assigned to
        date_assigned (any): Date task was assigned
        due_date (any): Due date of task.
        completion (any): No/Yes to indicated whether task has been completed
        description (any): Description of task.
    """
    try:
        tasks_file = open("./tasks.txt", "r")
        tasks_file = open("./tasks.txt", "a")
        tasks_file.write(f"\n{assigned_to}, {task}, {description}, {date_assigned}, {due_date}, {completion}")
    except FileNotFoundError:
        tasks_file = open("./tasks.txt", "a")
        tasks_file.write(f"{assigned_to}, {task}, {description}, {date_assigned}, {due_date}, {completion}")


#====Login Section====
username = None

# Ask User if they want to login in.
print("Welcome To Task Manager.")
user_login = input("Would You Like to Login?(Y/N): ").strip().upper()

while user_login == "Y":

    # Acquire username and password.
    print("\nPlease Enter Your details below")
    username = input("Username\t\t: ")
    password = input("Password\t\t: ")

    # Verify if valid username and password were entered
    if username in read_users_file():

        if password == read_users_file()[username]:
            break
        else:
            print("\nYou have entered an incorrect Password")
            user_login = input("Would You Like to try to login again?(Y/N): ").strip().upper()
            if user_login != "Y":
                username = None

    else:
        print("\nYou have entered an incorrect Username and Password")
        user_login = input("Would You Like to try to login again?(Y/N): ").strip().upper()
        username = None

# When user has choosen not to login
if user_login != "Y" and user_login != "N":
    print(".........\nInvalid input, Please restart process.")

elif user_login != "Y":
    print("Goodbye!!")

#=====Admin menu=====
while username == "admin":
    print(f"\nWelcome {username}")
    menu_display_admin()

    menu = input("What would you like to do?: ").strip().lower()

    # Register New User
    if menu == "r":
        register_user = "Y"

        while register_user == "Y":
            print("\nRegister a New User")
            print("Please enter new user details below")

            new_username = input("New Username\t\t: ")

            # Check if username already exists.
            if new_username in read_users_file():
                print("Username already exists, Please enter different Username")

            else:
                new_password = input("New Password\t\t: ")
                confirm_pass = input("Confirm Password\t: ")

                # Check if passwords match
                if new_password == confirm_pass:
                    register_new_user(new_username, new_password)
                else:
                    print("Passwords do not match!")

            register_user = input("\nWould You like to register a new user again?(Y/N): ").strip().upper()
                        
            if register_user == "N":
                break
            elif register_user == "Y":
                continue
            else:
                print("Input not recognised, please restart process")
                break

    # Add New Task
    elif menu == "a":
        print("To add a task, please fill in the details below")
        
        assigned_to = input("Assigning to: ")

        # Confirm if user exists
        if assigned_to in read_users_file():
            task = input("Task: ")
            date_assigned = datetime.date.today().strftime("%d %b %Y")

            try:
                print("\nDue Date\nThe details on date must be numbers\n")
                day = int(input("Day: "))
                month = int(input("Month: "))
                year = int(input("Year: "))
                due_date = datetime.date(year,month,day).strftime("%d %b %Y")

            except Exception as error:
                print(error)
                break

            completion = "No"
            description = input("\nTask descriptio:\n")

            add_task(task, assigned_to, date_assigned, due_date, completion, description)
            print("\nTask Added")
                    
        else:
            print("User not recognised")

    # View all Tasks
    elif menu == "va":
        try:
            for tasks in range(len(read_tasks())):
                print_tasks(read_tasks()[tasks])

        except Exception:
            print("Error with the task file, check if file exists")

    # View my tasks           
    elif menu == "vm":
        try:
            for tasks in range(len(read_tasks())):
                if (read_tasks()[tasks][0]) == username:
                    print_tasks(read_tasks()[tasks])
                else:
                    print("\nNo Tasks to display")
                    break

        except Exception:
            print("Error with the task file, check if file exists")

    # Statistics for admin
    elif menu == "s":
        try:
            # Determine number of tasks and users
        
            number_of_tasks = len(read_tasks())
            number_of_users = len(read_users_file())

            # Determine number of tasks not completed
            not_completed_tasks = 0
            for tasks in range(len(read_tasks())):
                if (read_tasks()[tasks][5]) == "No":
                    not_completed_tasks += 1

            # Number of tasks completed
            completed_tasks = number_of_tasks - not_completed_tasks

            print("\nWelcome to Task Statistics")
            print(f"\nThe total number of tasks: {number_of_tasks}\t\tThe total number of Users: {number_of_users}")
            print(f"\nNot completed:\t{not_completed_tasks}\nCompleted:\t{completed_tasks}")

        except Exception:
            print("Error with Task file")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("\nYou have entered an invalid input. Please try again")

#=====User Menu=====
while username in read_users_file() and username != "admin":
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    print(f"\nWelcome {username}")
    menu_display_user()
    menu = input("What would you like to do?: ").strip().lower()

    # Add New Task
    if menu == "a":
        print("To add a task, please fill in the details below")
        
        assigned_to = input("Assigning to: ")

        # Verify if user exists
        if assigned_to in read_users_file():
            task = input("Task: ")
            date_assigned = datetime.date.today().strftime("%d %b %Y")

            try:
                print("\nDue Date\nThe details on date must be numbers\n")
                day = int(input("Day: "))
                month = int(input("Month: "))
                year = int(input("Year: "))
                due_date = datetime.date(year,month,day).strftime("%d %b %Y")
            except Exception as error:
                print(error)
                break

            completion = "No"
            description = input("\nTask descriptio:\n")

            add_task(task, assigned_to, date_assigned, due_date, completion, description)
            print("\nTask Added")
                    
        else:
            print("User not recognised")

    # View all tasks
    elif menu == "va":
        try:
            for tasks in range(len(read_tasks())):
                print_tasks(read_tasks()[tasks])
                
        except Exception:
            print("Error with the task file, check if file exists")

    # View my tasks         
    elif menu == "vm":
        try:
            for tasks in range(len(read_tasks())):
                if (read_tasks()[tasks][0]) == username:
                    print_tasks(read_tasks()[tasks])
                else:
                    print("\nNo Task to display")
                    break

        except Exception:
            print("Error with the task file, check if file exists")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("\nYou have entered an invalid input. Please try again")
