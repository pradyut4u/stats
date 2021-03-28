import csv
with open("SOCR-HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]

for i in range(len(filedata)):
    number=filedata[i][1]
    newdata.append(float(number))

newdata.sort()
l=len(newdata)
if l%2==0:
    meadian1=float(newdata[l//2])
    meadian2=float(newdata[l//2+1])
    meadian=meadian1+meadian2/2
else:
    meadian=float(newdata[l//2])

print("meadian is "+ str(meadian))