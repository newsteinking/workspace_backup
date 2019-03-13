from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

while True:
    command=input("Do you want to finish? [exit] :")
    if command=="exit":
        break
    else:
        time.sleep(0.1)
        logan.postToChat("ccccccooooooooooooooooMMMMMMMMMMMMMMMMMMMMMMmmmmmmmmmmmmAAAAAAAAAAAAAnnnnnnnnnnnnnnDDDDDDDDDDDDDD!!")
        
logan.postToChat("exit")