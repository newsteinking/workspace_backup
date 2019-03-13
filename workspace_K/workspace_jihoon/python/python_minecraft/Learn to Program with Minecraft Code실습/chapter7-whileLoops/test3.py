import time
# answer="y""try ag
# while answer=="y":
#     answer=input("input your answer y or n:")
#     time.sleep(1)
#     print(answer)

# print("finished")

password="cat"
passwordinput=input("input your password:")
while password!=passwordinput:
    passwordinput=input("input your password:")
    time.sleep(1)
    if password==passwordinput:
        print("password accepted")
    else :
        print("try again")
        break
print("finished")