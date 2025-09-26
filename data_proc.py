import pandas as pd
data = pd.read_excel('file.xlsx')
data.head()

data['Views'] = data['Views'].str.replace(" views","")

new = []

for i in data['Views']:
    if(i.endswith('K')):
        i = i.replace('K','')
        new.append(float(i) * 1000)
    else :
        new.append(i)

data['Views'] = new

#Duration column cleaning
data['Duration'] = data['Duration'].str.replace("\n","")

new2 = []

for i in data['Duration']:
    if(i=='SHORTS' or len(i.split(':'))==1):
        new2.append(i)
    elif(len(i.split(':'))==2):
        i = i.split(':')
        tim = int(i[0])*60 + int(i[1])
        new2.append(tim)
    elif(len(i.split(':'))==3):
        i = i.split(':')
        tim = int(i[0])*3600 + int(i[1])*60 + int(i[2])
        new2.append(tim)
        
data['Duration'] = new2

#Duration column categorization
for i in data['Duration'].index:
    val = data['Duration'].iloc[i]
    if(val=='  SHORTS'):
        continue
    elif(val in range(0,900)):
        data.loc[i,'Duration'] = 'Mini-Videos'
    elif(val in range(901,3600)):
        data.loc[i,'Duration'] = 'Long-Videos'
    else:
        data.loc[i,'Duration'] = 'Very-Long-Videos'
