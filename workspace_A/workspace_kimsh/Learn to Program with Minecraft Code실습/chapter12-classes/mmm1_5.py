print(str(list(range(1,10001))).count('8'))
n, m = map(int, input().split())
for i in range(n):
    if i % 2 == 0:
        print("#"*m)
    else:
        s = ["."]*m
        s[(i//2)%2-1] = "#"
        print("".join(s))
        
        
n, m = map(int, input().split())
for i in range(n):
    if i%2==0:
        print("#"*m)
    else:
        if i%4==1:
            s=["."]*m 
            s[-1]="#"
            print("".join(s))
        else:
            s=["."]*m 
            s[0]="#"
            print("".join(s))