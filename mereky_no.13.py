n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s1=0
s2=0
even=[]
odd=[]
while i<len(n):
    k=n[i]
    if k%2==0:
        s1=s1+k
        even.append(k)
    else:
        s2=s2+k
        odd.append(k)
    i=i+1
print("sum of even=",sum(even))
print("sum of odd=",sum(odd))



























# even=[]
# odd=[]
# for number in n:
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)
# print("total odd=",odd)
# print("total even=",even)
# print("sum of odd",sum(odd))
# print("sum of even=",sum(even)) 








# a=0
# a1=0
# i=0
# even=[]
# odd=[]
# while i<len(n):
#     if i%2==0:
#         even.append(i)
#         a=a+n[i]

#     else:
#         odd.append(i)
# print("sum of even=",sum(even))
# print("sum of odd=",sum(odd))