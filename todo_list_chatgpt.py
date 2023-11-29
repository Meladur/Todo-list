print("Welcome to my Todo-List app")

todo_list = []
#In this version i asked chat to orgnize the list with index and the name and to make it on txt file
# Load tasks from a file on startup
try:
    with open("todo_list.txt", "r") as file:
        todo_list = file.read().splitlines()
except FileNotFoundError:
    pass  # If the file doesn't exist yet, ignore the error

while True:
    user = input("Please choose a command add, view, remove, exit: ").lower()

    if user == "add":
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added!")

    elif user == "view":
        if not todo_list:
            print("Nothing to view!")
        else:
            print("Tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")

    elif user == "remove":
        if not todo_list:
            print("Nothing to remove ! ")
        else:
            task = input("Please choose the task : ")
            todo_list.remove(task)
            print("Task removed! ")


    elif user == "exit":
        # Save tasks to a file before exiting
        with open("todo_list.txt", "w") as file:
            for task in todo_list:
                file.write(f"{task}\n")
        print("Tasks saved. Exiting the app.")
        break

    else:
        print("Invalid command!")
