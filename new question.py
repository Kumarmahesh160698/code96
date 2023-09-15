text= input("enter the text")
if("make a lot of money" in text):
    a=True
elif("buy noe" in text):
    a=True
elif("click this" in text):
    a=True
elif("subscribe this" in text):
    a=True
else:
    a=False
if(a):
    print("this textis spam")
else:
    print("this text is not spam")