''' 1) panda's --> Pandas is a Python library used to work with and analyze data 
 --) series --> a series is a one-dimentional labeled array that can hold any data type:integers,float,string,or even python object.each element in the series has a unique label called an index 
   it is often used to track change or pattern over time such as daily temperatures , stock price,or sales revenue.
2) datafram is a twodimentional labeled data structure in pandas,similar to a tabel in a database,an excel spreadsheet, or a SQL tabel.
--) it consist of rows and column,where:
a) rows have indices (labels)
b) columns have names(labels)
'''


import pandas as pd
data=pd.read_csv("sales_data_sample.csv") # 1) import the file which you have  #sytax of inclute the file which you have 2) data=pd.read_csv("sales_data_sample.csv",encoding="latin1") or data=pd.read_csv("sales_data_sample.csv",encoding="utf-8") while error are often use it
print(data.head())# show the head of file  for read the file 
print(data.tail())#show the tail of file for read the file 

