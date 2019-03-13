from mcpi.minecraft import Minecraft

def hamsu(name):
    """
    
     this is test 
     
    """
    return name*3

mc=Minecraft.create()

mc.postToChat(hamsu("car the garden."))  
