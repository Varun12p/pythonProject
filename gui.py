import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos,txt"):
    with open("todos.txt", 'w') as file:
        pass


sg.theme("LightBlue1")

clock = sg.Text(key='clock')
label = sg.Text("Enter your todo:")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todo1',
                      enable_events=True, size = (30,15))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("Your todo app.",
                   layout=[[clock],[label],[input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Hello", 15))

while True:

    event,value = window.read(timeout=500)
    window['clock'].update(time.strftime("%b %d,%Y:%H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo1'].update(todos)

        case "Edit":
            try:
                todo_to_edit = value['todo1'][0]
                new_todo = value['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todo1'].update(todos)
            except IndexError:
                sg.popup("Select a Todo first.",font=("Hey", 20) )

        case "Complete":
            try:
                todo_to_delete = value['todo1'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todo1'].update(todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Select a Todo first.")

        case "Exit":
            break

        case "todo1":
            window['todo'].update(value=value['todo1'][0])

        case sg.WIN_CLOSED:
            break

window.close()