import functools as ft

a= ['hattori','ahatsoff','hahaha','kamehameha']
longest=max(a,key=len)
print(longest)

suff=list(filter(lambda x: x.endswith('ha'),a))
print(suff)

pref=list(filter(lambda x: x.startswith('ha'),a))
print(pref)


abc=lambda x:'hat' in x

ins=list(filter(abc,a))

#ins=list(filter(lambda x, y: y in x,(a,'hat')      idk what is this
print(ins)

lena=list(map(len,a))
summ=ft.reduce((lambda x, y: x+y),lena)

avg=summ/len(a)

print(avg)