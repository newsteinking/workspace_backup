from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create()
mc.postToChat("test")
x=110
y=50
z=102

mc.player.setTilePos(x,y,z)
z=20
time.sleep(2)
mc.player.setTilePos(x, y, z)

