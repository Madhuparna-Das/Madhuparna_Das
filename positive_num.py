l=[]
n=eval(input("enter the no of elements of list"))
print("enter the elements one by one")
for i in range(1,n+1):
    l.append(eval(input()))
print("the positive numbers are")
for i in l:
    if(i>0):
        print(i)
    
