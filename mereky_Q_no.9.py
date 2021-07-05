
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 

sum=0
i=0
while i<len(marks):
    j=0
    k=0
    while j<len(marks[i]):
        k=k+marks[i][j]
        j=j+1
    sum=sum+k
    i=i+1
average=sum/len(marks)
print(sum)
print(average)
    