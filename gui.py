import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter your todo:")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Your todo app.",
                   layout=[[label],[input_box,add_button]],
                   font=("Hello", 20))

while True:

    event,value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break






window.close()