testfile=open("ToDolist.txt","w")

todolist=""

toDoItem=input("Your <todolist> is... : ")

while toDoItem !="exit":
    todolist=todolist+toDoItem+"\n"
    toDoItem=input("Your <todolist> is... : ")
    
testfile.write(todolist)
testfile.close()

