arr = [1,2,3,4]
arr1 = [1,2,3,4,5,6,7]

mergedArr = []

for x in arr:
    if not x in mergedArr:
        mergedArr.append(x)
for y in arr1:
    if not y in mergedArr:
        mergedArr.append(y)



print(mergedArr)