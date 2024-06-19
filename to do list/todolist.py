tasks = []

def addTask():
    task= input("Please enter a task: ")
    tasks.append(task)
    print(f"Task'{task}' added to the list. ")

def listTasks() :
    if not task:
        print("There are no task currently.")
    else:
        print("current Task:")
        for index, task in enumerate(task):
            print(f"Task #{index}. {task}")

    

def deleteTask():
    listTasks()
    try:
      taskToDelete = int(input("Enter the # o to delete: "))
      if taskToDelete >=0 and taskToDelete < len(tasks):
          tasks.pop(taskToDelete)
          print(f"Task {taskToDelete} has been removed.")
      else:
          print(f"Task #{taskToDelete} was not found.")
    except:
        print("invalid input.")

if __name__=="__main__":
    ### Create a loop to run app
    print("welcom to the to do list app:)")
    while True:
        print("\n")
        print("please select one of the following options")
        print("-----------------------------------------")
        print("1. Add a new task")
        print("2. Deleat a task")
        print("3. list task")
        print("4. Quit")

        choice= input("Enter your choice: ")

        if(choice =="1"):
            addTask()
        elif(choice =="2"):
           deleteTask()
        elif(choice =="3"):
           listTasks()
        elif(choice =="4"):
            break
        else:
            print("invalid input. Please try again.")

        print("goodbye")



