a=['nike','adidas','reebok']
b=list(range(int(input ('enter n'))))
c=['best','w','gu','fast']
def mymap(fn,lst):
        nlst=[]
        for i in lst:
            nlst.append(fn(i))
        return nlst
def lentup(x):
    return(x,len(x))



def osq(n):
    if n%2==1:
        return n**2
    else:
        return 0

lst1=list(set(mymap(osq,b)))
lst1=[x for x in lst1 if x!=0]
print(sorted(lst1))

print(mymap(lambda x:x+'est',c))

print(list(map(lentup,a)))