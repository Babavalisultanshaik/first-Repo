import pandas as pd
l=[10,20,30]
d = pd.Series(l,index=['a','b','c'])
print(d)
e= pd.DataFrame([[10,'smith'],[20,'allen']],index=['x','y'],columns=['id','ename'])
print(e)