from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

x,y,z=logan.player.getPos()
startz=z
blocks = [[35, 35, 22, 22, 22, 22, 35, 35],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 35, 35, 35, 35, 22],
          [22, 35, 22, 35, 35, 22, 35, 22],
          [22, 35, 35, 22, 22, 35, 35, 22],
          [35, 22, 35, 35, 35, 35, 22, 35],
          [35, 35, 22, 22, 22, 22, 35, 35]]
for block in reversed(blocks):
    for blocktype in block:
        logan.setBlock(x+3,y,z,blocktype)
        z+=1
        time.sleep(0.1)
    y+=1
    z=startz
    