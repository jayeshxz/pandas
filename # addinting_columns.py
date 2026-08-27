# addinting the columns
#how to add column in their 
import pandas as pd  # import the pandas labrary
data={      # distionary 
    "name":['jay','ram','sita','jayuu','sham','dattu','nikhil','sitarani'],
    "age":[20,30,28,21,23,53,22,11],
    "city":['zurkhead','ayodya','rampur','mothawada','jalgoan','paldhi','shirpur','nagar'],
    "Salary":[8000,55000,20000,66666,300000,350000,250000,1000000],
    "attendace_score":[89,88,90,99,45,34,45,46]}


df=pd.DataFrame(data) # converd the data into data fream 


# column addind sytax  in their this dictionary  1) i want add performance score column 

#sytax= datafream_variable_name=["column_name"] = data_of the column

df["performance"] = 66,55,44,8,64,85,99,77 # add in one column  

 # print the after add column 

# add one more column with use to another column 1) add the column increment 10% bonus 

df["Salary_bonus"]=df["Salary"]*0.1 #creat the column to bounus of 10% of the salary


#using insert() method --> this use to add the column in specific position using the insert() method
#sytax-->datafream_variable_name.insert(location,"column_name",[add_data])
df.insert(0,"current_steat",['temp','per','temp','per','temp','per','temp','per'])



#  updating specific value in the column and row
# how to change perticular value with the help of the row  and column
# syntax--> datafream_variable_name.loc[row_index,"column_name"]=new_value
#ex- update the ram's salary 55000 to 70000 
df['Salary_1']=df['Salary']
df.loc[1,"Salary"]=70000 # change the perticular value 

# update the multiple vlaue's 
df['Salary_1']=df['Salary_1']*1.05
print(df)
