
from funcions import get_todos,write_todos
import time

now_date=time.strftime(" ˘%b,%d.%Y,%H:%M:%S")

print("It is",now_date)
while True:
    user_action=input("What are you want to do? Add,Show or Exit:")


    if user_action.startswith('add'):
        todo=user_action[4:]

        todos=get_todos('todos.txt')

        todos.append(todo+'\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)




    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')


        for index,item in enumerate(todos):
            print(f'{index+1}. {item.strip()}')


    elif user_action.startswith('edit'):
        try:
            number=int(input("Enter the number of the todo:"))
            number=number-1
            todos = get_todos()
            new_todo=input("Enter the new todo:")+"\n"
            todos[number] = new_todo
            with open('todos.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid input")

    elif user_action.startswith('done'):
        try:
            number=int(user_action[5:])

            todos = get_todos('todos.txt')
            index=number-1

            todos.pop(index)

            write_todos(todos)
        except ValueError:
            print ('You have to write a number')
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid input")


