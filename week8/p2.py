student={}
n=int(input('enter the no of students'))
for i in range(n):
    srn=input('enter srn:')
    student[srn]={}
    student[srn]['m'] = int(input('enter maths marks:'))
    student[srn]['p'] = int(input('enter physics marks:'))
    student[srn]['c'] = int(input('enter chem marks:'))
    student[srn]['b'] = int(input('enter bio marks:'))
#print(student)

total={}
for i in student:
    total[i]=student[i]['m']+student[i]['p']+student[i]['c']+student[i]['b']
#print(total,sorted(total.values()))


same={}

for i in student:
    if student[i]['m'] not in same:
        same[student[i]['m']] = []
    same[student[i]['m']].append(i)
#print(same)








