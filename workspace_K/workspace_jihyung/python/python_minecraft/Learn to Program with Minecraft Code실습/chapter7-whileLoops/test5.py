import time

answer="y"
count=0
while (answer=='y'):   # == <= >= 
    answer=input("y or n ")
    count=count+1
    print(answer)
    time.sleep(1)
    
print("{},{}".format(count,answer))