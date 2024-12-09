from Btree import Btree
from HeaderFormat import Btree

def createMenu():
    print("--------------------------MENU:--------------------------")
    print("create - create a new index file")
    print("open - open an existing index file")
    print("insert - insert a key into the Btree")
    print("load - read unsigned integers")
    print("print - print the Btree")
    print("extract - overwrite the file")
    print("quit - quit program")
    print("---------------------------------------------------------")
def handleCreate():
    filename = input("Enter the desired filename")
    try:
        #does file exits?
        if open(filename, 'rb'):
            bool = input("File f{filename} exists. Do you want to overwrite? yes/no").strip().lower()
        if bool != "yes":
            print("No overwrite decided")
    except FileNotFoundError:
        pass

    with open(filename, 'wb') as open_file:
        header = HeaderFormat(rootID = 0, )
def handleInsert(BtreeClass):
    key = input("Enter key to insert")
    value = input("Enter value to insert")
def promptUser():
    createMenu()
    return input("Enter command: ").strip().lower()
def main():
    BtreeClass = None
    comm = promptUser()
    while comm != quit:
        if comm == "create":
            handleCreate()
        elif comm == "insert":
            handleInsert(BtreeClass)
