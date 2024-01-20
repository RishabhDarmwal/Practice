#creating input files file1 and file2
file1 = open('file1.txt', 'w')
f1=[(1,'Ravi',50000),(1,'Atul',80000),(3,'Sohil',45000),(4,'Gopal',35000),(5,'Soujanya',45000)]
for s in f1:
    line=str(s[0])+','+s[1]+','+str(s[2])+'\n'
    file1.write(line)

file2 = open('file2.txt', 'w')
f2=[(1,1500),(2,1400),(3,2000),(4,1500),(5,1800)]
for s in f2:
    line=str(s[0])+','+str(s[1])+'\n'
    file2.write(line)
file1.close()
file2.close()

#displaying file 1 and file 2
file1=open('file1.txt','r')
file2=open('file2.txt','r')
print("File1 is :")
print(file1.read())
print("File2 is :")
print(file2.read())
file1.close()
file2.close()



#creating output file
file1=open('file1.txt','r')
file2=open('file2.txt','r')
data1=[]
data2=[]

for i in file1:
    i=i[:-1] #to remove \n from string
    data=i.split(',')
    data1.append(data)

for i in file2:
    i=i[:-1] #to remove \n from string
    data=i.split(',')
    data2.append(data)

output=open('output.txt','w+')
for i in range(len(data1)):
    output.write(data1[i][0]+ ','+ data1[i][1]+ ',' + str(int(data1[i][2])+int(data2[i][1]))+'\n')
for i in output:
    print(i)

file1.close()
file2.close()
output.close()

#printing output file
output=open('output.txt','r')
print("Output File is:")
for i in output:
    print(i,end='')
output.close()