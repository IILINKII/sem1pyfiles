a=open('file1.txt','r')
b=open('file2.txt','r')
alines=a.readlines()
blines=b.readlines()
alines=set([x.strip() for x in alines])
blines=set([x.strip() for x in blines])

print(alines|blines)

print(alines&blines)

ainb=[x for x in alines if x in blines]
print(ainb)

print(alines^blines)

a.close()
b.close()

