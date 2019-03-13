
from mcpi.minecraft import Minecraft
#from builtins import True, False
mc=Minecraft.create()

mc.postToChat("test")

#mc.postToChat(1/0)
#print(1/0)

try:
    print(1/0)
except:
    print("error")

#===============================================================================
# True
# False
#===============================================================================




















