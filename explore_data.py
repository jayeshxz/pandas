# 1--> explore the data set first 
# 2-->understand the data 
# 3-->identify the problem which method we use in side the file 
# 4-->plane next steps
#------------------------------------------------------------------------------------------------#
# we have two methos the to explore the row's 
#head(n) --> method use to show the fist row in the data set 
#tail(n) --> method use to show the last row in the data set 
#n--> numbers what ammount of the row show or defult head() --> show the 5 rwo only same as tail()
import pandas as pd
data=pd.read_csv("sales_data_sample.csv")
'''
print(data.head(2)) # --> show the fist 2 row's  or defult head() was show fist five row's
print(data.tail(1)) # -->show the last 1 row     or defult tail() was show last five row's

'''
# 5-->cloumns, rows?
# 6-->what type of ?
# 7-->missing data?

#(-->) .info()-->method are use to identify the
#  1)number of column rows and cloumns 
#  2)column name 
#  3)int64 float64 object 
#  4)non null count's 
#  5)memory usager of the data frame 
print(data.info()) # summerized the data set -->idetify the nan or null value & type of data 



