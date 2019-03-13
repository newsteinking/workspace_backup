from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

wood=17
leaves=18

def making(x,y,z):
    logan.setBlocks(x,y,z,x,y+5,z,wood)
    time.sleep(0.5)
    logan.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
    time.sleep(0.5)
    logan.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)
    time.sleep(1)
    logan.setBlock(x, y + 8, z,11)
    print("..wow")

x,y,z=logan.player.getPos()    
#making(x+5,y,z)
for i in range(1,6):
    making(x+5,y,z+(10*i))