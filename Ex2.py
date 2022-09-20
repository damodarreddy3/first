#Average
arrayList =[1,2,3,4,5,6,7,9,10,11,12,13]
def average(arr):
    return sum(arr)/len(arr)
average= average(arrayList)
print("Average " + str(average))

#Maximum 
maximumNumber = max(arrayList)
print("Maximum: " + str(maximumNumber))

#Array reverse
arrayList.reverse()
print("Reverse: " + str(arrayList))

#Copy an array into another
newArray = []
arrayList.reverse()
newArray= arrayList.copy()
print("Copy an array into another: " + str(newArray))

# prime number
def primeNumber(arrayList):
    primeNumberList=[]
    for i in arrayList:
        count=0
        for j in range(1,i):
            if i%j ==0:
                count+=1
        if count == 1:
            primeNumberList.append(i)
            count =0
    return primeNumberList
primeNumbers = primeNumber(arrayList)
print("Prime Numbers in an Array: "+ str(primeNumbers))

