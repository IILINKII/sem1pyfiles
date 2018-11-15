all='''karnataka bangalore whitefield
tamilnadu chennai marina_beach
karnataka mysore nellorehalli
kerala munnar chokramudi_peak
kerala kochi fort_kochi
tamilnadu chennai annanagar
karnataka ballari byappanahalli
tamilnadu chennai chidambaram
kerala kochi nefertiti
karnataka bangalore indiranagar
karnataka ballari MGroad
tamilnadu salem ganesh_temple
tamilnadu salem trishur
kerala kochi mantancherry_palace
kerala munnar anamudi
kerala munnar kollukumalai_tea'''
'''
place={}
count=0
for i in all.split('\n'):
   a = i.split()[0]
   b = i.split()[1]
   c = i.split()[2]
   if a not in place:
     place[a] = 0
     count+=1
   place[a]+=1
print(place, 'total states:', count)

place={}
for i in all.split('\n'):
    a = i.split()[0]
    b = i.split()[1]
    c = i.split()[2]
    if a not in place:
       place[a]=set()
    place[a].add(b)
print(place)
'''
place={}
count=0
for i in all.split('\n'):
   a = i.split()[0]
   b = i.split()[1]
   c = i.split()[2]
   if a not in place:
       place[a]={}
   if b not in place[a]:
       place[a][b]=set()
   place[a][b].add(c)
   count+=1
print(place, 'total no of places',count)