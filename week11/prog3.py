import copy
a=[1,2,3,23,233,4]
def myreduce(fn,lst):
    nlst=copy.deepcopy(lst)
    i=0
    while i<len(nlst)-1:
        nlst[i+1]=fn(nlst[i],nlst[i+1])
        i+=1
    return nlst[len(nlst)-1]
def inttostr(lst):
    nlst=[]
    for i in lst:
        nlst.append(str(i))
    return(nlst)

#print(myreduce(lambda x,y:x+y,a))
print(myreduce(lambda x,y:max(x,y),a))
print(myreduce(lambda x,y:x+y,inttostr(a)))