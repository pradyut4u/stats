import csv
from collections import Counter
with open("SOCR-HeightWeight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]

for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))

data= Counter(newdata)
print(data)