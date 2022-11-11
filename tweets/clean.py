# st="@elle_vader @DrEricDing I've had five now. Hardly any side effects, probably because I'm 62, so my immune response isn't as robust."
# st1="RT @Flipboard: Find out why @taylorswift13's return to pop in “Midnights” has captured the attention of more than just her loyal fans. Plus…"
# st2="Just posted a photo https://t.co/R4Qj1tqezZ"

import pandas as pd

def clean(st):
	st=str(st)
	words=list(st.split())
	if words[0]=='RT':
		return None
	res=[]
	for i in range(len(words)):
		if len(words[i])>7 and words[i][0:8]=="https://":
			continue
		if words[i][0]!='@':
			res.append(words[i])
	return ' '.join(res)


df=pd.read_csv('top50.csv',encoding='gb18030')
cols=[]
for i in range(1,51):
	col='s'+str(i)
	cols.append(col)

for col in cols:
	df[col]=df.apply(lambda x:clean(x[col]),axis=1)

df.to_csv('top50_cleaned.csv',encoding='gb18030')