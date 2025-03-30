import pandas as pd

class Tarefa:
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

def tarefas_add():
    tarefas_list = []
    while True:
        tarefa_title = input("Title (or type 'quit' to stop):\n")
        if tarefa_title.lower() == 'quit':
            break
        elif tarefa_title.isdigit():
            print('Enter a Valid Title')
            continue
        tarefa_description = input("Description:\n")
        tarefa_status = False
        tarefa = Tarefa(tarefa_title, tarefa_description, tarefa_status)
        tarefas_list.append(tarefa)
    return tarefas_list

def tarefas_remove(tarefas_list):
    if not tarefas_list:
        print("No tasks to remove.")
        return tarefas_list
    print("\nCurrent Tasks:")
    for i, tarefa in enumerate(tarefas_list):
        print(f"{i + 1}. {tarefa}")
    try:
        completed_task_index = int(input("\nEnter the number of the task to remove (or 0 to cancel): ")) - 1
        if completed_task_index == -1:
            print("No task removed.")
            return tarefas_list
        if 0 <= completed_task_index < len(tarefas_list):
            check = input('Are you sure you want to remove it? Type (yes) or (no): ')
            if check.lower() == 'yes':
                removed_task = tarefas_list.pop(completed_task_index)
                print(f"Task '{removed_task.title}' has been removed.")
            else:
                print("Task not removed.")

        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return tarefas_list

def change_status(tarefas_list):
    if not tarefas_list:
        print("No tasks to mark.")
        return tarefas_list
    for i, tarefa in enumerate(tarefas_list):
        print(f'{i + 1}. {tarefa}')
    try:
        task_index = int(input("\nEnter the number of the task to mark as completed (or 0 to cancel): ")) - 1
        if 0 <= task_index < len(tarefas_list):
            tarefas_list[task_index].change_s()
            print(f"Task '{tarefas_list[task_index].title}' marked as completed.")
        else:
            print('Mark a valid Task')
    except ValueError:
        print('Enter a valid number')

def main():
    tarefas_list = tarefas_add()
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
            for tarefa in tarefas_list:
                print(tarefa)
        elif option == "2":
            tarefas_list = tarefas_remove(tarefas_list)
        elif option == "3":
            tasks_data = [tarefa.to_dict() for tarefa in tarefas_list]
            df = pd.DataFrame(tasks_data)
            tasks_json = df.to_json(orient='records', lines=True)
            with open('tasks.json', 'w') as f:
                f.write(tasks_json)
            print("Tasks saved to 'tasks.json'. Exiting...")
            break
        elif option == '4':
            tarefas_list += tarefas_add()
        elif option == '5':        
            change_status(tarefas_list)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()