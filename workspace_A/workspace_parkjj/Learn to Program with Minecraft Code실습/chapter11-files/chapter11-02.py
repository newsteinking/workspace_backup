from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

toDoList=open("todofile.txt","r")
for line in toDoList:
    logan.postToChat(line)
    time.sleep(1)