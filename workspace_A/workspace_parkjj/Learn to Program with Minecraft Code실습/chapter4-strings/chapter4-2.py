from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

firstname=input("What is your first name? :")
secondname=input("What is your second name? :")
logan.postToChat("hello, "+firstname+" "+secondname)
logan.postToChat("hello, {} {}".format(firstname,secondname))
#===============================================================================
# Ross
# Taylor
# 
# 
# Hello Ross Taylor!
#===============================================================================