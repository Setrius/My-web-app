FILEPATH = "todos.txt"

# Setting up a custom function for reading and writing to the txt doc
# avoid using variables used elsewhere in the code ie 'todos' was changed to todos_local
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to do items to the list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == '__main__':
    print('hello')
    print(get_todos())