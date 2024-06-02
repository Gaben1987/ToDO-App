import os

if os.path.exists('proba.txt'):
    print('hello')
else:
    print('not exists')    

Filepath='todos.txt'

def get_todos(Filepath):
    with open(Filepath, 'r') as file:
        todos = file.readlines()
        return todos
def write_todos(todos, Filepath):
    with open(Filepath, 'w') as file:
        file.writelines(todos)
        return todos

if __name__ == "__main__":
  print("Hello World")