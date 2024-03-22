tasks=[]

def add_tasks(task):
    tasks.append({"task":task,"1":False})
    print("tasks added successfully")

def list_tasks():
    print("/ntasks to be completed")
    for index, task in enumerate(tasks, start=1):
        if tasks[::]:
            status= " "
        else:
            status=" "
        print(f"{index}.[{status}] {task['task']}")
    print()
def mark_completed(index):
    if 1<=index<=len(tasks):
        print("task",(index),"marked as complete")
    else:
        print('invalid index')
while True:
    print(" options")
    print("1.add a task")
    print("2. list task")
    print("3.mark as complete")
    print("4. exit") 
    choice=input("enter your choice(1/2/3/4)")
    
    if choice=="1":
        task=input("enter the task")
        add_tasks(task)

    elif choice=="2":
        list_tasks()
    elif choice=="3":
        list_tasks()
        index=int(input("enter the task number"))
        mark_completed(index)
    elif choice=="4":
        print("good bye")
        break

    else:
        print("invalid choice")    