from mcpi.minecraft import Minecraft



def main():
    logan=Minecraft.create()
    logan.postToChat("Hello")
    answer=input("Do you want to passed away? [Yes / No] :")
    pos=logan.player.getPos()
    x=pos.x
    y=pos.y
    z=pos.z
    
    if answer=="Yes":
        logan.postToChat("Okay..")
        logan.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,11)
    
    
if __name__=="__main__":
    main()