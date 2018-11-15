n=int(input('enter a number'))
lst=[]
for i in range(1,n):
    if n%i==0:
        lst.append(i)
if sum(lst)==n:
    print('perfect no')
else:
    print('not a perfect no')