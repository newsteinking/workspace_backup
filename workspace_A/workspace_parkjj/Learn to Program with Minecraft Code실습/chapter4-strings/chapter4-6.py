from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time
from mcpi import block
loganid=logan.getPlayerEntityIds()
logan.postToChat("I'm {}".format(loganid))

pos=logan.player.getPos()


x=pos.x
y=pos.y
z=pos.z
one=block.WOOD.id
two=block.LAVA_FLOWING.id
three=block.MUSHROOM_RED.id
up=3


logan.postToChat("What is your favorite block?")
nice_block=(input("[one=wood] [two=mushroom] [three=lava] :"))

if nice_block=='wood':
    logan.setBlock(x+up,y,z,one)
elif nice_block=="mushroom":
    logan.setBlock(x+up,y,z,three)
elif nice_block=="lava":
    logan.setBlock(x+up,y,z,two)
else:
    logan.postToChat("error")
