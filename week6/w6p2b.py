n=int(input('enter the number'))
a=0;b=1;c=0;lst=[]
for i in range(1,100):
    c=a+b
    a=b
    b=c
    lst.append(c)
if n in lst:
    print('fibonacci no')
else:
    print('not a fibonacci no')