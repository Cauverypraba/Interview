str1=input()
str=str1.lower()
count=0
for i in range(0,len(str)):
    if str[i]!=str[i-1]:
       count+=1
print(count)