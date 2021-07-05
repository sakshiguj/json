list1=input("enter the number=")
i=1
a=[]
while i<=len(list1):
    a.append(list1[-i])
    i=i+1
k=list(list1)
print(k)
if k==a:
    print("palidrome hai")
else:
     print("palidrome nhi hai")


# reverse=s[::-1]
# if s==reverse:
#     print("yes")
# else:
#     ("no")