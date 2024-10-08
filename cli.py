# new_todos = [item.strip('\n') for item in todos] (list comprehension-striping the '\n' in the console terminal)
# cli = Command Line interface

from functions import get_todos, write_todos
# Imported functions from new py file to optimize the code
import time

now = time.strftime("%b, %d.%Y, %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = get_todos(filepath='../web_app1/WebApp/todos.txt')  # there is no need for the arg in the() it is mentioned in the function
        todos.append(todo)
        write_todos(filepath="../web_app1/WebApp/todos.txt", todos_args=todos)  # same here only keep in the () the var todos

    elif user_action.startswith("show"):
        todos = get_todos(filepath='../web_app1/WebApp/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos(filepath='../web_app1/WebApp/todos.txt')
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(filepath="../web_app1/WebApp/todos.txt", todos_args=todos)

        except ValueError:
            print("This command is not valid, Enter a number and space after the command")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos(filepath='../web_app1/WebApp/todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(filepath="../web_app1/WebApp/todos.txt", todos_args=todos)

            message = f"todo {todo_to_remove} was removed from the list "
            print(message)
        except ValueError:
            print("Error put space after complete")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")
# sell
