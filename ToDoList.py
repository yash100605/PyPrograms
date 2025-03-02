tasks = []
while True:
    print("--To-Do List--")
    print("1. Insert Task")
    print("2. Delete a Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        n = int(input("How many task you want to enter ?: "))
        if n>0:
            i = 1
            while n>0:
                task = input(f"Enter Task {i}: ")
                tasks.append(task)
                i += 1
                n -= 1
            print()
        else:
            print("Invalid Input\n")
    elif choice == 2:
        task = input("Enter the task you want to delete: ")
        if task in tasks:
            tag = tasks.index(task)
            tasks.pop(tag)
            print()
        else :
            print("No task found !")
        
    elif choice == 3:
        if len(tasks)>0:
            print(f"There are {len(tasks)} tasks.")
            print("The tasks are as follows :")
            for i,task in enumerate(tasks,1):
                print(f"Task {i} : {task}")
            print()
        else:
            print("No tasks to Display !")
            print()
    elif choice == 4:
        print("GoodBye!")
        break
    else:
        print("Invalid Choice\n")
        
