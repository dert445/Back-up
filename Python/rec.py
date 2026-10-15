def rec(a):
    if(a==1):
        return 1
    return a*rec(a-1)
num=int(input())
c=rec(num)
print(c)