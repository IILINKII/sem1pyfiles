lst=[(120,'a',12,23,34),(462,'v',90,34,67),(552,'k',34,54,76)]

print(sorted(lst))
print(sorted(lst,key=lambda x:x[1]))
print(sorted(lst,key=lambda x: x[2]+x[3]+x[4],reverse=True))