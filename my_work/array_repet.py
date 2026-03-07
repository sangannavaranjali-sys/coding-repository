a=[10,24,34,26,10,24,34]
n=len(a)
seen=set()
result=0
for i in range(n):
    if(a[i] in seen):
        result=a[i]
        break
    seen.add(a[i])    
print("The repeated item : ",result)        


