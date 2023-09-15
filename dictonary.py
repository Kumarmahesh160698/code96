myDict={
"fast":  "in a quick manner",
"mahesh" : "is a teacher",
"mark":[1,23,34],
"another":{'mahesh':'teacher'}
}
print(myDict['fast'])
myDict['mark']=[343,65] #element ko replace kr sakt h  
print(myDict['mark'])
print(myDict['another']['mahesh']) #nested dictonary  
#dictnary method
print (myDict.keys())
print(myDict.items())
updateDict={"lovis":"freind" ,  
            
     "mahesh":"is a recercher"       
            
            }
myDict.update(updateDict)#update the dictnary using update method
print(myDict)

print(myDict.get["mahesh2"])