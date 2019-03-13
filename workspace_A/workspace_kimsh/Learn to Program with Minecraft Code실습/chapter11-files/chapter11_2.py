from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

test=open("ToDolist.txt","r")
#mc.postToChat(test)
for line in test:
    mc.postToChat(line)
    time.sleep(1)
test.close()