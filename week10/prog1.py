a='qwerty'
def cnt(a):
    if len(a)==0:
        return 0
    else:
        return(cnt(a[1:])+1)
print(cnt(a))
