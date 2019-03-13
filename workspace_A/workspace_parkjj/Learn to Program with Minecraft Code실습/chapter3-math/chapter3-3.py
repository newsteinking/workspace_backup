from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

sum=0
for i in range(1,11):
    sum=sum+i
    #logan.postToChat(sum)
    print(sum)
    if i==10:
        logan.postToChat(sum)
        
        
        
##
#===============================================================================
# void main()
# {
#     int sum=0
#     for (i=0;i<11;i++)
#     {
#         sum=sum+i
#         printf(' 5d',sum)
#     }
# }
#     
#===============================================================================