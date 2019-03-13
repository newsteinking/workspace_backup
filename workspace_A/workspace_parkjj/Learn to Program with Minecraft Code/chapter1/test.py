from mcpi.minecraft import Minecraft
import time
from builtins import int
import string
from xmlrpc.client import boolean

mc=Minecraft.create()
time.sleep(2)
mc.postToChat("Hello")
time.sleep(1.5)
mc.postToChat('Minecraft')
time.sleep(3)
mc.postToChat(1*7)
time.sleep(0.5)
x=3
y=4
mc.postToChat(x+y)
time.sleep(0.5)
z=14
a=2
mc.postToChat(z/a)
time.sleep(1)
mc.postToChat("You're so lucky!")
mc.postToChat("What a nice guy!")

#===============================================================================
# int
# float
# string
# boolean
#===============================================================================

my_string=1