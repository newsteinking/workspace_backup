from mcpi.minecraft import Minecraft
import time
logan=Minecraft.create()

password="cuty logan"
m_password=input("What is your magic password? :")

while password != m_password:
    logan.postToChat("Password is incorrect")
    m_password=input("What is your magic password? :")
    
    if password==m_password:
        logan.postToChat("correct!")
    else:
        print("test")
        break 

print("correct")