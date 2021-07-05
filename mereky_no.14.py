# n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# s1=0
# s2=0
# even=0
# odd=0
# while i<len(n):
#     a=n[i]
#     if a%2==0:
#         even=even+1
#         s1=s1+n[i]
#     else:
#         odd=odd+1
#         s2=s2+n[i]
#     i=i+1
# avg1=s1/4
# avg2=s2/7
# print("total even=",even,"total odd=",odd)
# print("averge of even=",avg1,"average of odd=",avg2)



n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s1=0
s2=0
k1=0
k2=0
even=[]
odd=[]
while i<len(n):
    k=n[i]
    if k%2==0:
        even.append(k)
        s1=s1+k
        k1=k1+1
    else:
        odd.append(k)
        s2=s2+k
        k2=k2+1
    i=i+1
avg1=s1/4
avg2=s2/7
print("total even=",even)
print("total odd=",odd)
print("total even=",k1)
print("total odd=",k2)
print("sum of even=",sum(even))
print("sum of odd=",sum(odd))
print("total avg=",avg1)
print("total avg=",avg2)

