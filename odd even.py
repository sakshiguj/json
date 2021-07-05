k=[]
n=int(input("enter the number="))
for i in range(1,10+1):
    a=int(input("enter the number="))
    k.append(a)
even=[]
odd=[]
for j in k:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("even numbers=",even)
print("odd numbers=",odd)



