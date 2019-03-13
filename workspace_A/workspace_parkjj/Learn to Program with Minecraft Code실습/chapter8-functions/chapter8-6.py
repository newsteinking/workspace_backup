from mcpi.minecraft import Minecraft
import time
from mcpi import block


logan=Minecraft.create()
x,y,z=logan.player.getPos()
def make_melon():
    return block.FLOWER_YELLOW.id
logan.setBlock(x+5,y,z,make_melon())
