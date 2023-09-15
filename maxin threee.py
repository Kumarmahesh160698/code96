def max(num1,num2,num3):
    if (num1>num2):
        if(num1>num2):
          return num1
        else:return num2
    else:
      if(num2>num3):
         return num2
      else:
         return num3
      

m=max(34,54,23)
print(m)


def far(cel):
   return (cel*(9/5))+32


f=far(0)
print(f)

n=3
for i in range(n):
   print("*" * (n-i))