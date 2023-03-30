import numpy as np
class SparseMatrix:
    def __init__(self,m,n):
        self.sList=[[m,n,0]]

    def append(self, i, j, val):
        self.sList.append([i,j,val])
        self.sList[0][2] += 1

    def shape(self):
        return(self.sList[0][0], self.sList[0][1])
    def pprint(self):
        X=np.zeros(self.shape())
        for i in range(1,len(self.sList)):
            X[self.sList[i][0],self.sList[i][1]]=self.sList[i][2]

s=SparseMatrix(3,4)
s.append(0,1,1)
s.append(1,1,2)
s.append(1,3,3)
s.pprint



import numpy as np
class SparseMatrix:
    def __init__(self,m,n):
        self.sList=[[m,n,0]]

    def append(self, i, j, val):
        self.sList.append([i,j,val])
        self.sList[0][2] += 1

    def shape(self):
        return(self.sList[0][0], self.sList[0][1])

    def getValue(self, i, j):
        for i in range(1,len(self.sList)):
            if self.sList[i][0] == i and self.sList[i][1] ==j:
                return self.sList[i][2]
        return 0
    @classmethod
    def transpose(cls,X):
        _tmp = X.shape()
        s_T=SparseMatrix(_tmp[1], _tmp[0])
        sList = copy.deepcopy(X.sList)
        for i in range(len(sList)):
            sList[i][0],sList[i][1]=sList[i][1],sList[i][0]
        s_T.sList=sList
        return s_T

    @classmethod
    def add(cls,A,B):
        _tmp=A.shape()
        C=SparseMatrix(_tmp[0],_tmp[1])
        m=_tmp[0]
        n=_tmp[1]
        C=SparseMatrix(m,n)
        locations=set()
        for i in range(len(A.sList)):
            locations.add((A.sList[i][0],A.sList[i][1]))
        for i in range(len(B.sList)):
            locations.add((B.sList[i][0],B.sList[i][1]))
        for loc in locastions:
            A.getValue(loc[0],loc[1]) +B.getValue(loc[0],loc[1]) != 0:
            C.append(loc[0],loc[1])+B.getValue(loc[0],loc[1])


        #for i in range(m):
         #   for j in range(n):
          #      addVal=A.getValue(i,j)+B.getValue(i,j)
           #     if addVal !=0:
            #        C.append(i,j,addVal)

        #return C

    def pprint(self):
        X=np.zeros(self.shape())
        for i in range(1,len(self.sList)):
            X[self.sList[i][0],self.sList[i][1]]=self.sList[i][2]
        print(X)

a=SparseMatrix(3,3)
a.append(0,0,1)
a.append(1,1,2)
a.append(2,2,3)

b=SparseMatrix(3,3)
b.append(0,2,6)
b.append(1,1,5)
b.append(2,0,4)

c=SparMatrix.add()