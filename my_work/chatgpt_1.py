dict={
    "Anjali" :[89],
    "Riya" : [78,73],
    "Rahul" : [98,68],
    "Arjun" : [88,92,71],
}

for name in dict:
    marks=dict[name]
    s_marks=sum(marks)
    avg=s_marks/len(marks)
    print(name, ":" ,avg)


 
