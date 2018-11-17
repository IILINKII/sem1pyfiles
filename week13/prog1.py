r=int(input('enter the no of rows'))
c=int(input('enter the no of columns'))

class matrix:
    def __init__(self,r,c):
        self.r=r
        self.c=c
        mat=[]
        temp=[]
        for j in range(c):
            temp.append(0)
        for i in range(r):
            mat.append(temp)
        self.mat=mat


    def printmat(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.mat[i][j],end=' ')
            print()


    def upd(self):
        self.mat=[]
        temp=[]
        print('enter the elements row wise one by one')
        for i in range(r):
            for j in range(c):
                temp.append(int(input('enter element:')))
            self.mat.append(temp)
            temp=[]
        #print('the updated matrix is:')
        #self.printmat()

    def add(self,x):


        for i in range(self.r):
            for j in range(self.c):
                self.mat[i][j]+=x.mat[i][j]
        #print('the updated matrix is:')
        #self.printmat()




xyz= matrix(r,c)
xyz.printmat()
print('for matrix updation:')
xyz.upd()
xyz.printmat()
print('for matrix to be added:')
p=matrix(r,c)
p.upd()
xyz.add(p)
xyz.printmat()


'''
    def __str__(self):
        return self.mat
'''