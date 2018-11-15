def find(fn,p):
    print(fn(p))
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
def prime(x):
    if len(factors())