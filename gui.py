import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter your todo:")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todo1',
                      enable_events=True, size = (30,15))
edit_button = sg.Button("Edit")

window = sg.Window("Your todo app.",
                   layout=[[label],[input_box,add_button],
                           [list_box,edit_button]],
                   font=("Hello", 15))

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
            window['todo1'].update(todos)
        case "Edit":
            todo_to_edit = value['todo1'][0]
            new_todo = value['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todo1'].update(todos)
        case "todo1":
            window['todo'].update(value=value['todo1'][0])



        case sg.WIN_CLOSED:
            break






window.close()