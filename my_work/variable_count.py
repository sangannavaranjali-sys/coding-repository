str=input("Enter the string : ")
count=0
for i in range(len(str)):
    if str[i] in "aeiouAEIOU":
        print(str[i]," is Vowel")
        count +=1
    else:
        print(str[i]," is Not vowel")    
print("The total vowel : ",count)