lst=[12,24,35,70,88,120,155]
badnum=[0,4,5]
lst=[i for i in lst if lst.index(i) not in badnum]
print(lst)
lst=[12,24,35,24,88,120,155]
lst=[x for x in lst if x!=24]
print(lst)