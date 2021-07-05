# list=[15,58,20,2,3]
# i=1
# while i<=len(list):
#     print(list[-i])
#     i=i+1

# list=[15,58,20,2,3]
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1

# list=[15,58,20,2,3]
# list.reverse()
# print(list)


list1=[15,58,20,2,3]
i=len(list1)-1
k=[]
while i>=0:
    a=list1[i]
    k.append(a)
    i=i-1
print(k)
