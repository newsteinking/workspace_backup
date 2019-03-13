from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
global mc; mc = Minecraft.create()
mc.postToChat("what")
x=100
y=0
z=100
mc.player.setTilePos(x,y,z)
time.sleep(10)