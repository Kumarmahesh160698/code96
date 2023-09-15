#a= None
#if(a is None):
#    print("yes")
#else:
#    print("no")  
#a=[24,45,65] 
#print(457 in a)
num1=int(input("enter the num 1"))
num2=int(input("enter the no 2"))
num3 =int (input("enter the no3"))
num4=int(input("enter the no4"))

if(num1>num4):
    f1=num2
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num1
if(f1>f2):
    print(str(f1)   + "is greater")
else:
    print(str(f2)  +"is greater")

