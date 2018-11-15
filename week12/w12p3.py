a=open('w12p2.py','r')
b=open('headers.txt','w')
lines=a.readlines()
lines=[x.split('\n') for x in lines]

lines=[x for x in lines if x]

for i in lines:
    #if i[len(i)-1][-1]==':':
    if i[len(i)-1].endswith(':'):

        print(i,file=b)

a.close()
b.close()

a=open('w12p2.py','r')
b=open('fndefs.txt','w')

lines=a.readlines()
lines=[x.strip('\n') for x in lines]
lines=[x for x in lines if x]


flag= False


for i in lines:
    if i.startswith('def'):
        flag=True
        print(i,file=b)

    elif i.startswith('    ') and flag:
        print(i,file=b)
    else:
        flag = False
