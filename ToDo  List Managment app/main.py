# || this project is for a files working understanding purpose ||
# something like.... todo list item!: complete/incomplete

# Load  existingitems
# 1. craete new items
# 2. list items
# 3. mark items as complete/incomplete
# 4. save items

# {"tasks": [
#     {
#     "description": "task is this",
#     "complete": True
#     }
# ]}

# |------------------------------------------------------------------------------------------------------|
import json
import os

file_name= "todo_list.json"


def load_tasks():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}
    

def save_tasks(tasks):
    try:
        with open(file_name,'w') as file:
            json.dump(tasks,file)
    except:
        print("Error saving tasks to file.")
    

def view_tasks(tasks):
    print()
    tasks_list = tasks["tasks"]   # giving a key tasks of dictionary so it get value (i.e. list which stores tasks as value)
    if len(tasks_list) == 0:
        print("No Tasks to Display.")
    else:
        print("List of Tasks")
        for idx, task in enumerate(tasks_list):
            status = "[completed]" if task["complete"]  else "[pending]"  # --> if True it means 
            print(f"{idx+1}. {task['description']} | {status}")

    

def add_task(tasks):
    description =input("Enter the task description: ").strip()
    if description :
        tasks["tasks"].append({ "description" : description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    index = int(input("Enter index/sr.no of the task to mark as complete: ").strip()) - 1
    if 0 <= index < len(tasks["tasks"]):
        if tasks["tasks"][index]["complete"]  == True : # --> if True it means task is already completed
            print("Task is already marked as complete.")
        else:
            tasks["tasks"][index]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
    else:
        print("Invalid index. Please try again.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter index/sr.no of the task to delete: ").strip()) - 1
        if 0 <= index < len(tasks["tasks"]):
            deleted_task = tasks["tasks"].pop(index)
            save_tasks(tasks)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid index number.")

def reset_tasks(tasks):
    try:
        incomplete_tasks = []
        for task in tasks["tasks"]:
            if not task["complete"] : # its tasks["tasks"][idx]["complete"] == False
                incomplete_tasks.append(task)
        
        if incomplete_tasks:
            print("\nYou Cannot reset tasks while there are incomplete tasks.")
            print("Incomplete tasks:")
            for idx, task in enumerate(incomplete_tasks):
                print(f"{idx+1}. {task['description']} | {'[completed]' if task['complete'] else '[pending]'}") 
            return
        else:
            reset = input("Are you ure you want to reset all tasks? (yes/no): ").strip().lower()
            if reset == 'yes':
                tasks["tasks"] = []
                save_tasks(tasks)
                print("Tasks List have been reset.")
            else:
                    print("Tasks reset cancelled.")
    except Exception as e:
        print(f"An error occurred while resetting tasks: {e}")    

    
def main():
    # save_tasks({"tasks": ["Saved tasks"]}) #--> Testing

    tasks = load_tasks()

    # print(tasks) # --> Testing

    while True:
        print("\n|| To-Do List Management App ||")
        print("1. View Tasks")
        print("2. Add tasks")
        print("3. Mark as  Complete")
        print("4. delete task")
        print("5. Reset Tasks")
        print("6. Exist")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            reset_tasks(tasks)
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
