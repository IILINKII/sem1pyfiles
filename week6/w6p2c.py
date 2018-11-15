n=int(input('enter the number to be checked'))
for i in range(1,100):
    if n/(2**i)==1:
        print('perfect power of 2')
        break
    elif(i==99):
        print('not a perfect power of 2')