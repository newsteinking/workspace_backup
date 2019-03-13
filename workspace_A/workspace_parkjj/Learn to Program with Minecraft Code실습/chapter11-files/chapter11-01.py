print("XD")

toDoFile=open("todofile.txt","w")

toDoList=""

toDoItem=input("to do Item:")

while toDoItem != "exit":
    toDoList=toDoList+toDoItem+"\n"
    toDoItem=input("to do Item:")

toDoFile.write(toDoList)
toDoFile.close