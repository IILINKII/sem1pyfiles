a=open('file.txt','r')

try:
    print('hello',file =a)
except Exception as e:
    print('sorry, error:',e)
else:
    print('written!')
finally:
    print('complete!')