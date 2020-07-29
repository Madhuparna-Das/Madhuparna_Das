string=input("enter the string")
all_freq = {} 
for i in string: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
sorted((all_freq),reverse=True)
  
# printing result  
print ("Count of all characters in the string is :\n "
                                        +  str(all_freq)) 
