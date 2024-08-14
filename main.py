import functions
import time

time = time.strftime("%b %d,%Y:%H:%M:%S")
print("It is", time)

while True:
    user_input = input("Enter if you like to add, show, edit, complete or exit:")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todo)

    elif user_input.startswith("show"):
        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{todo}")

    elif user_input.startswith("edit"):
        try:

            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print ("Enter the number of todo to edit:")
            continue

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])
            number = number - 1

            todos = functions.get_todos()

            todos.pop(number)

            functions.write_todos(todos)
        except IndexError:
            print ("There is no item with that number.")
            continue

    elif user_input.startswith("exit"):
        break

    else:
        print("Command is invalid.")


