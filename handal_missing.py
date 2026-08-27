#handling missing data //// data cleaning 

#NaN-->(not a number)
#None-->(foor object data type)

# isnull()
# True- value is missing (NaN)
# False - value is present 

import pandas as pd 
data={      # distionary 
    "name":['jay','None','sita','jayuu','sham','dattu','nikhil','sitarani'],
    "age":[20,30,28,21,23,None,22,11],
    "city":['zurkhead','ayodya','rampur','mothawada','jalgoan','paldhi','shirpur','nagar'],
    "Salary":[8000,None,20000,66666,300000,350000,250000,1000000],
    "attendace_score":[89,88,90,99,45,34,45,None]
    }
df=pd.DataFrame(data) 
print(df)
# detect value is missing 
#syatax --> print(DataFrame_varible.isnull())
print(df.isnull()) # detect the value is missing 

# you want know which columns what number of the NaN present 
#sytax-->print(DataFrame_name.isnull().sum())
print(df.isnull().sum()) # detect the NaN value in columns 



#  HANDLE THE MISSING VALUE 
# TWO TYPE HANDLING ---> 1) REMOVING THE NaN VALUE 2)FILL THE NaN VALUE
# 1) drop the missig vlue--> you dont want to fill or this value don'st work it then removing it specific value 

# imp --> axis=0 --> row  &  axis=1-->column
#syntax -->1) dropna(inplace=True)   2)fillna(value,inplace=True)
'''
df.dropna(inplace=True) # this method to use drop the NaN value but this method can removing the other data also then use the fillna method the fill the data defult or you want to
print(df) 
'''
# fillna(value,inplace=True)
'''
df.fillna(0,inplace=True) # fill the defult value 
'''
df['age'].fillna(df['age'].mean(),inplace=True) # this logic use to fill the mean value inside the NaN value in age column
df['Salary'].fillna(df['Salary'].mean(),inplace=True) # this logit also fill the mean value inside the NaN value
print(df)