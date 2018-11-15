a=['ansc','2kaka','jdck','*3kjwcu']
b=[(9,3),(23,2),(144,12)]
def myfilter(fn,lst):
    nlst=[]
    for i in lst:
        if fn(i)==True:
            nlst.append(i)
    return nlst


print(myfilter(lambda x: x[0].isdigit()!=True,a))
print(myfilter(lambda x: x[0]%x[1]==0,b))