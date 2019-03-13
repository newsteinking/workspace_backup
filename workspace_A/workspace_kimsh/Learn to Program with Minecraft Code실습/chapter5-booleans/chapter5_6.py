from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
front=3
blocktype=103

mc.setBlock(x+front,y,z,blocktype)
check_blocktype=mc.getBlock(x+front,y,z)

checkblock= check_blocktype==blocktype

if checkblock:
    mc.postToChat("This is water melon.")
    
else: 
    mc.postToChat("This is others.")
