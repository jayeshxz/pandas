# after manipulation the data // cleaning the data how to save it 
# how creat datafram with help of dictionaryy

import pandas as pd

data={ # distionary 
    "name":['jay','ram','sita','jayuu'],
    "age":[20,30,28,21],
    "city":['zurkhead','ayodya','rampur','mothawada']

}
df=pd.DataFrame(data) # syatx the creat the file  after manipulation annd cleaning the data 
print(df)
'''
df.to_csv("output.csv",index=False) # sytax .to_typefile --># save the file df.to_csv,json,excel,gbq ("file name what you want")
df.to_excel("new_file_save.xlsx",index=False) # save the file in ecel form
df.to_json("new_file_json.json",index=False)

'''