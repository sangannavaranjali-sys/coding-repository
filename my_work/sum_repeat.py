a=[10,2,5,4,6,7]
target=17
seen=set()
for x in a:
    y=target-x
    if y in seen:
        print(y)
        break
    else:
        seen.add(x)
    
