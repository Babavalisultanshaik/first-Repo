import numpy as np
import pandas as pd
d={'empno':np.arange(101,111),
    'ename':['smith','ward','allen','manupriya','anitha','james','nishika','king','ford','sharanya'],
   'sal':[800,6000,3950,4250,3000,3999,4777,5555,8000,7590],
   'comm':[300,np.nan,400,np.nan,100,0,np.nan,np.nan,np.nan,np.nan],
   'job':['clerk','salesman','manager','analyst','president','hr','clerk','salesman','analyst','clerk'],
   'hiredate':['3/jun/2000','3/jun/2001','3/jul/2000','3/jun/2000','6/jun/2000','6/jun/2000','5/dec/1999','3/jun/2000','3/jun/2000','3/jun/2000'],
   'deptno':[10,20,20,30,10,20,30,20,10,30]}
df=pd.DataFrame(d)
x= df.describe(include='all')
print(x)