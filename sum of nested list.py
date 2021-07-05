# a=[[1,2],[4,5]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     d=0
#     while j<len(a[i]):
#         d=d+a[i][j]
#         j=j+1
#     sum=sum+d
#     i=i+1
# print(sum)




# a=[[1,2],[3,4],5,6]
# # k=0
# i=0
# sum=0
# while i<len(a):
#     if type(a)==type(a[i]):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1

# a=[[1,2],[3,4],5,6]
# # k=0
# i=0
# sum=0
# while i<len(a):
#     if type(a)==type(a[i]):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1

# a=[[1,2],[3,4],5,6]
# i=0
# sum=0
# while i<len(a):
#     if type(a)==type(a[i]):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)

# a=[10,20,[30,40]]

# n=len(a)

# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m=len(a[i])
#             for j in range(m):
#                 print(a[i][j])
#     else:
#         print(a[i])


a=[2,3,[4,5]]
# n=[]
i=0
sum=0
while i<len(a):
    if i<2:
        sum=sum+a[i]
    else:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    i=i+1
print(sum)
