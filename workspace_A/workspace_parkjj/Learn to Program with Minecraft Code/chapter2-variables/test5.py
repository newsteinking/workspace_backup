from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


x = -133
y = 20
z = -1943

mc.postToChat("I want to Fly into the sky!")

time.sleep(3)
mc.postToChat("NICE!!")
mc.player.setTilePos(x, y+400, z)
