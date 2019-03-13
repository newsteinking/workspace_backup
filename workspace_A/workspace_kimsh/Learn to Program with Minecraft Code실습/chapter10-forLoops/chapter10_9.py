from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
pos=mc.player.getPos()
x,y,z=pos.x,pos.y,pos.z
front=3

Blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]
for Block in reversed(Blocks):
#===============================================================================
# a=Blocks.reverse()
# for Block in a:
#===============================================================================
    for block in Block:
        mc.setBlock(x+front,y,z,block,4)
        x+=1
    y+=1
    x=pos.x
    