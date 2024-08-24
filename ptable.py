import pandas as pd
data = pd.read_csv('result.txt',on_bad_lines='skip')
#data.columns = ['SI.No', 'Subject Title', 'Grade','Grade Points','Credits'] 
print(data.info())
data.to_csv('fromtxt.csv',  
                  index = None) 