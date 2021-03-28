import csv
with open ("SOCR-HeightWeight.csv",newline="") as f:
    reader= csv.reader(f)
    filedata= list(reader)
    
filedata.pop(0)
newdata=[]
print(len(filedata))
for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))

l= len(newdata)
total=0
for a in newdata:
    total= total+a

mean=total/l
print("mean is "+ str(mean))