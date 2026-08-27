#removing the column you want to
import pandas as pd
data={      # distionary 
    "name":['jay','ram','sita','jayuu','sham','dattu','nikhil','sitarani'],
    "age":[20,30,28,21,23,53,22,11],
    "city":['zurkhead','ayodya','rampur','mothawada','jalgoan','paldhi','shirpur','nagar'],
    "Salary":[8000,55000,20000,66666,300000,350000,250000,1000000],
    "attendace_score":[89,88,90,99,45,34,45,46]
    }
df=pd.DataFrame(data)
print("befor removing the attendace_score")
print(df)
# removing the column
#sytax--> dataframe_variable_name.drop(columns=["column_name"],inplace=True) --> this syntax removing the hole column
print("after removing the attendace_score")
df.drop(columns=["attendace_score"],inplace=True) # removing the columns 
print(df)
# you can also drop the multiple column 
df.drop(columns=["age","Salary",'city'],inplace=True)
print(df)


#use the drop function to use unnassery column delet

