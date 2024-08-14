while True:
    user_input = input("Enter if you like to add, show, edit, complete or exit:")
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo = input("Enter your todo:") + '\n'

            file = open("Todos.txt", 'r')
            todos = file.readlines()
            file.close()

            # YOU CAN USE THE BELOW CODE INSTEAD OF THE ABOVE CODE TO READ OR WRITE AS IT IS SHORTER AND
            # DON'T NEED TO CLOSE FILE AS IT DOES IT ON ITS OWN.
            # write open("Todos.txt", 'r') as file:
            # todos = file.readlines()

            todos.append(todo)

            file = open("Todos.txt", 'w')
            todos = file.writelines(todos)
            file.close()

        case 'show':
            file = open("Todos.txt", 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Enter the todo number you want to edit:"))
            number = number - 1
            file = open("Todos.txt", 'r')
            todos = file.readlines()
            file.close()

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            file = open("Todos.txt", 'w')
            todos = file.writelines(todos)
            file.close()

        case 'complete':
            number = int(input("Enter the todo number you want to complete:"))
            number = number - 1

            with open("Todos.txt", 'r') as file:
                todos = file.readlines()

            todos.pop(number)

            file = open("Todos.txt", 'w')
            todos = file.writelines(todos)
            file.close()

        case 'exit':
            print("Thank You. BYE!")
            break
