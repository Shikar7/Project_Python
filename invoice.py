import re
import pandas as pd
import pdfplumber
from collections import namedtuple

Inv = namedtuple('Inv', 'vend_num vend_name inv_dt due_dt inv_amt net_amt description')

ap = 'preports.pdf'
with pdfplumber.open(ap) as pdf:
    page=pdf.pages[15]
    text = page.extract_text()
#print(text)

new_vendor_re = re.compile(r'^\d{3} [A-z].*')#begining of the line(^)and \d{3} means followed by 3 digits and space and letters[A-Z] and .*(whatever the data after that)
#inv_line_re = re.compile(r'\d{6} \d{6} [\d,]+\.\d{2}') 
#running the loop to get the data according to regular expressioon(re)
inv_line_re = re.compile(r'(\d{6}) (\d{6}) ([\d,]+\.\d{2}) [\sP]*([\d,]+\.\d{2}) [YN ]*\d (.*?) [*\s\d]')
line_items = []
for line in text.split('\n'): #iterate over text 
    if new_vendor_re.match(line): #we are checking the condition according to line and printing
        vend_num,*vend_name = line.split()
        vend_name = ' '.join(vend_name)
        # print(vend_num)
        # print(vend_name)

    line = inv_line_re.search(line)
    if line:
        #print(line.group(1))
        inv_dt = line.group(1)
        due_dt = line.group(2)
        inv_amt = line.group(3)
        net_amt = line.group(4)
        desc = line.group(5)
        line_items.append(Inv(vend_num, vend_name, inv_dt, due_dt, inv_amt, net_amt, desc))
    

print(line_items[1])

df = pd.DataFrame(line_items)
print(df.head())

#below codes are not working some issue with pandas
#df['inv_dt'] = pd.to_datetime(df['inv_dt']) #converting to data format
#df['due_dt'] = pd.to_datetime(df['due_dt']) 


#df['inv_amt'] = df['inv_amt'].map(lambda x: float(x.replace(',', ''))) #when we see the info of these coulums they were none so we are converting them to float for further calculations
#df['net_amt'] = df['net_amt'].map(lambda x: float(x.replace(',', '')))

print(df.sum())
df.to_csv('inv_result.csv')
