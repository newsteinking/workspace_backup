from mcpi.minecraft import Minecraft
import time

def main():
    ans1=input("Answer1:")
    ans2=input("Answer2:")
    count=0
    print(len(ans1))
    if len(ans1)!=0:
        count=count+1
        print(count)
        if len(ans2)!=0:
            count=count+1
            print(count)
            
    print(count)
    
if __name__=="__main__":
    main()

