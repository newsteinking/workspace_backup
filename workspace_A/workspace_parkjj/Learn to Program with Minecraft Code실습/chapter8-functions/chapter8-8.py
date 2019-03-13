from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

#===============================================================================
# x,y,z=logan.player.getPos()
#===============================================================================
def get_color(color):
    
    global x
    global y
    global z
    
    x,y,z=logan.player.getPos()
    if color == "pink":
        block_color=6
    elif color == "black":
        block_color=15
    elif color == "gray":
        block_color=7
    elif color == "red":
        block_color=14
        
    return block_color

colors=get_color("pink")
astring=input("[pink] [black] [gray] [red] :")
logan.setBlock(x+5,y+1,z,35,get_color(astring))