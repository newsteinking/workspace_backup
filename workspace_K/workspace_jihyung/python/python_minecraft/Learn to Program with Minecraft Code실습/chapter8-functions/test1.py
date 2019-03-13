from mcpi.minecraft import Minecraft
mc=Minecraft.create()


def greeting(name):
    #print("{} hellow".format(name))
    
    return name+" "+"hellow"
    
    
#=greeting("sam ")
print(greeting("sam"))
print(greeting("john"))

print("sam"+" "+"hello")
print("john"+" "+"hello")