#TO DO LIST APPLICATION
Todo_List=[]
def addtask():
    task=input("Enter ur task here..")
    Todo_List.append({"tasktodo":task,"Done":False})
    print("Task added successfully..")
    
def viewtask():
    if not Todo_List:
        print("No tasks to do right now..")
    else:
        for i, task in enumerate(Todo_List):
            status_symbol = '✓' if task['Done'] else '✗'
            
            status_text = 'Done' if task['Done'] else 'Pending'
            print(f"{i + 1}. {task['tasktodo']} [{status_symbol}] - {status_text}")

def deletetask():
    viewtask()
    if Todo_List:
        try:
            tasktodelete = int(input("Enter the task number to delete: ")) - 1

            if 0 <= tasktodelete < len(Todo_List):
                deletedtask = Todo_List.pop(tasktodelete)
                print("Task '{deletedtask['tasktodo']}' removed..")
            else:
                print("No such task number is available..")
        except ValueError:
            print("Please enter a numeric value.")
    else:
        print("No tasks available to delete.")


    
    
def marktaskcompleted():
    viewtask()
    if Todo_List:
        try:
            task_to_mark = int(input("Enter the task number to mark as completed: ")) - 1

            if 0 <= task_to_mark < len(Todo_List):
                Todo_List[task_to_mark]['Done'] = True
                print(f"Task '{Todo_List[task_to_mark]['tasktodo']}' marked as completed ✓.")
            else:
                print("No such task number is available..")
        except ValueError:
            print("Please enter a numeric value.")
    else:
        print("No tasks available to mark as completed.")

    

    

def main():
    
    while(1):
        print("\n1.ADD TASK..\n2.VIEW TASK..\n3.DELETE TASK..\n4. MARK COMPLETED TASK...\n5.EXIT..")
        choice=input("Enter ur choice>>")
        if choice=='1':
            addtask()
        elif choice=='2':
            viewtask()
        elif choice=='3':
            deletetask()
        elif choice=='4':
            marktaskcompleted()
        elif choice=='5':
            print("Bye ..see u in ur next task..")
            return
        else:
            print("Entered wrong choice...please choose correct choice")

if __name__=="__main__":
    main()
