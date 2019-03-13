from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

food=[]
while True:
    a=input("What do you want to eat for lunch?")    
    if a=="exit":
        break
    food.append(a)
    
food.insert(1,'test')
#===============================================================================
# food[1]='test'
#===============================================================================
logan.postToChat("Your lunch is {}".format(food))
food.sort()
logan.postToChat("Your lunch is {}".format(food))