from mcpi.minecraft import Minecraft
import time



def main():
    logan=Minecraft.create()
    #pos=logan.player.getpos()
    #x=pos.x
    #y=pos.y
    #z=pos.z
    x=int(input("X:"))
    y=int(input("Y:"))
    z=int(input("Z:"))
    valid=True 

    if not -128<=x<=128:
        valid=False 
    
    if not -64<=y<=64:
        valid=False
    
    if not-128<=z<=128:
        valid=False
    
    
    
    if valid==True:
        logan.player.setPos(x,y,z)
        blocktype=int(logan.getBlocks(x,y,z,x,y+1,z))
        if blocktype==24:
            logan.setBlocks(x,y,z,x,y+65,z,0)
        else:
            print("success")
    else:
        logan.postToChat("error")

if __name__ == "__main__":
    main()
    
    
    
    