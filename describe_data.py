# 1) describe() -->method gives you a quick statistical summary of numerical data.
'''
Statistic	  Meaning
count	      Number of values
mean	      Average
std	          Standard deviation
min	          Minimum value
25%	          25th percentile
50%           Median
75%     	  75th percentile
max	          Maximum value

#example-->

import pandas as pd
data={ # distionary 
    "name":['jay','ram','sita','jayuu','sham','dattu','nikhil','sitarani'],
    "age":[20,30,28,21,23,53,22,11],
    "city":['zurkhead','ayodya','rampur','mothawada','jalgoan','paldhi','shirpur','nagar'],
    "salary":[8000,55000,20000,66666,300000,350000,250000,1000000],
    "attendace_score":[89,88,90,99,45,34,45,46]
}
new=pd.DataFrame(data) #converd into the datafream
new.to_csv("output_1.csv",index=False) #creat the csv file 
print(new) #print the file in terminal 
print(new.info()) # idetify the data  with help of .info()
print(new.describe()) # describe the statstic all

'''


# 1)-->how big is your dataset
# 2)-->what are the name if columns 
" pandas provied the two atrubute for this "
# shape and columns 
# shape--> give the two value int form of tuple row's and column  -- to idetify the how ig dataset.
# columns--> show the name of the columns and you want to change the any column then you acess it and change perticular data.
 # -->

import pandas as pd
data={ # distionary 
    "name":['jay','ram','sita','jayuu','sham','dattu','nikhil','sitarani'],
    "age":[20,30,28,21,23,53,22,11],
    "city":['zurkhead','ayodya','rampur','mothawada','jalgoan','paldhi','shirpur','nagar'],
    "salary":[8000,55000,20000,66666,300000,350000,250000,1000000],
    "attendace_score":[89,88,90,99,45,34,45,46]
}
new=pd.DataFrame(data) #converd into the datafream
new.to_csv("output_1.csv",index=False) #creat the csv file 
print(new) #print the file in terminal 
print(new.shape) #give the two value int form of tuple row's and column  -- to idetify the how ig dataset.(row,column)
print(new.columns)#show the name of the columns and you want to change the any column then you acess it and change perticular data.

# maniulation specific column and row 
# filter the row 
#1)-->select specific column
#2)-->filter rows
#3)-->combine multiple conditions 
#single column
print(new["name"]) # selecting the one column in series  sytax--> print(variable_name["column_name"]) in the square bracket 
#multiple columns
print(new[["name","salary"]])# selecting the multiple column sytax--> print(variable_name[["column_name_1","column_name_2"]])

# filter the row's --> 
# apliying  condition 
high_salary=new[new['salary']>50000] #aplying the condition on the specific column and row  direct print --> print(new[new['salary']>50000])
print(high_salary)

# use two or more condition on one column and row
filter=new[(new['salary']>50000) & (new['age']>30)] # sytax new[(new['column_1']>condition) & (new[column_2]>condition)]
print(filter)
# use two condion on one row filterd 
# or condiona one candition are true 
# and conditon both condiition are true 
  

  
