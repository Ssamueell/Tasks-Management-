import pandas as pd

class Tasks:
    def __init__(self, title: str, description: str, status: bool):
        self.title = title
        self.description = description
        self.status = status

    @property
    def show_t(self) -> str:
        return f'{self.title}'
    
    @property
    def show_d(self) -> str:
        return f'{self.description}'
    
    @property 
    def show_status(self) -> bool:
        return f'{self.status}'

    def change_s(self): 
        self.status = True
        return self.status

    def __str__(self) -> str:
        status = "Completed" if self.status else "Pending"
        return f"Title: {self.title} | Description: {self.description} | Status: {status}"

    def to_dict(self) -> dict:
        return {
            'Title': self.title,
            'Description': self.description,
            'Status': self.status
        }

def task_add():
    tarefas_list = []
    while True:
        tarefa_title = input("Title (or type 'quit' to stop):\n")
        if tarefa_title.lower() == 'quit':
            break
        elif tarefa_title.isdigit():
            print('Enter a Valid Title')
            continue
        task_description = input("Description:\n")
        task_status = False
        task = Tasks(task_title, task_description, task_status)
        tarefas_list.append(task)
    return tarefas_list

def task_remove(task_list):
    if not task_list:
        print("No tasks to remove.")
        return task_list
    print("\nCurrent Tasks:")
    for i, tarefa in enumerate(task_list):
        print(f"{i + 1}. {task}")
    try:
        completed_task_index = int(input("\nEnter the number of the task to remove (or 0 to cancel): ")) - 1
        if completed_task_index == -1:
            print("No task removed.")
            return task_list
        if 0 <= completed_task_index < len(task_list):
            check = input('Are you sure you want to remove it? Type (yes) or (no): ')
            if check.lower() == 'yes':
                removed_task = task_list.pop(completed_task_index)
                print(f"Task '{removed_task.title}' has been removed.")
            else:
                print("Task not removed.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return task_list

def change_status(task_list):
    if not task_list:
        print("No tasks to mark.")
        return task_list
    for i, task in enumerate(task_list):
        print(f'{i + 1}. {task}')
    try:
        task_index = int(input("\nEnter the number of the task to mark as completed (or 0 to cancel): ")) - 1
        if 0 <= task_index < len(task_list):
            task_list[task_index].change_s()
            print(f"Task '{task_list[task_index].title}' marked as completed.")
        else:
            print('Mark a valid Task')
    except ValueError:
        print('Enter a valid number')

def main():
    task_list = task_add()
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Remove a task")
        print("3. Save and exit")
        print('4. Add another task')
        print('5. Mark task as completed')
        option = input("Choose an option: ")
        if option == "1":
            print("\nCurrent Tasks:")
            for task in task_list:
                print(task)
        elif option == "2":
            task_list = task_remove(tarefas_list)
        elif option == "3":
            tasks_data = [task.to_dict() for task in task_list]
            df = pd.DataFrame(tasks_data)
            tasks_json = df.to_json(orient='records', lines=True)
            with open('tasks.json', 'w') as f:
                f.write(tasks_json)
            print("Tasks saved to 'tasks.json'. Exiting...")
            break
        elif option == '4':
            task_list += task_add()
        elif option == '5':        
            change_status(task_list)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
