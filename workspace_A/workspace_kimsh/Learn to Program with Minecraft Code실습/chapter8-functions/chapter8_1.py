from mcpi.minecraft import Minecraft

def main():
    mc=Minecraft.create()
    mc.postToChat("Minecraft...")

def hello():
    mc=Minecraft.create()
    mc.postToChat("Hi")
    
def hello2(name):
    mc=Minecraft.create()
    mc.postToChat("hello {}".format(name))
    
def hello3(inpoot):
    if inpoot=="hello":
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
    hello()
    hello2("BIBI")
    hello3("hello")