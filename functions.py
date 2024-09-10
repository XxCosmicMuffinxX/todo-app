FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, mode='r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, mode='w') as file:
        file.writelines(todos_args)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
