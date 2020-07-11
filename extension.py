file_name=input("enter the file name").casefold()
b=file_name.split('.')
y=b[1]
if(y=='py'):
    print("file extension is python")
elif(y=='java'):
    print("file extension is java")
elif(y=='c'):
    print("file extension is C")
elif(y=='cpp'):
    print("file extension is c++")
else:
    print("please enter valid file name")
