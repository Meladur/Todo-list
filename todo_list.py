print("Welcome to my Todo-List app")

todo_list = []

while(True):
    user = input("Please choose a command add, view, remove, exit : ")
    if user == "add":
        task = input("Enter your task : ")
        todo_list.append(task)
        print("Task added! ")

    elif user == "view":
        if not todo_list:
            print("Nothing to view ! ")
        else:
            for task in todo_list:
                print(task)

    elif user == "remove":
        if not todo_list:
            print("Nothing to remove ! ")
        else:
            task = input("Please choose the task : ")
            todo_list.remove(task)
            print("Task removed! ")

    elif user == "exit":
        break
    else:
        print("Invalid command ! ")