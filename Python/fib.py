def fib(a):
    if(a==1):
        return 1
    if(a==0):
        return 0
    return fib(a-2)+fib(a-1)
print(fib(6))    