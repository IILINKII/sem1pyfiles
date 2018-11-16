l=['a',0,2]
def reci(x):
    new=[]
    for i in range(len(x)):
        try:
            new.append(1/x[i])
        except Exception as e:
            print('sorry, error:',e)
    return new
print(reci(l))