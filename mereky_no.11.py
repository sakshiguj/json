     
# # magic_square = [
# #     [5, 3, 7],
# #     [1, 8, 9],
# #     [6, 4, 2]



# # magic_square = [
#     # [8, 3, 4],
#     # [1, 5, 9],
#     # [6, 7, 2]




# # a=[]
# # for i in range(3):
# #     b=[]
# #     for j in range(3):
# #         j=int(input("enter the number"))
# #         b.append(j)
# #     a.append(b)
# # print("given number")
# # for i in range(3):
# #     for j in range(3):
# #         print(a[i][j],end=" ")
# #     print()
# # sum1=0
# # sum2=0
# # for i in range(3):
# #     for j in range(3):
# #         if i==j:
# #             sum1=sum1+a[i][j]
# #         if i+j==3-1:
# #             sum2==sum2+a[i][j]
# # if sum1!=sum2:
# #     f=1
# # else:
# #     for i in range(3):
# #         sum3=0
# #         sum4=0
# #         for j in range(3):
# #             sum3=sum4+a[i][j]
# #             sum3=sum4+a[i][j]
# #         if sum3!=sum4:
# #             f=1
# #         elif sum3!=sum4:
# #             f=1
# #         else:
# #             f=0
# # if f!=0:
# #     print("given number is magic squre")
# # else:
# #     print("not")



 
# magic_square = [
#     [8, 3, 7],
#     [1, 5, 9],
#     [6, 7, 9]
# ] 
# i=0
# s1=0
# while i<len(magic_square):
#     a=0
#     while a<len(magic_square):
#         v=magic_square[i][a]
#         s1=s1+v
#         break
#         a=a+1
#     i=i+1
# print(s1)
# j=0
# s2=0
# while j<len(magic_square):
#     b=0
#     while b<len(magic_square):
#         w=magic_square[j][b]
#         s2=s2+w
#         break
#         b=b+1
#     j=j+1
# print(s2)
# k=0
# s3=0
# while k<len(magic_square):
#     c=0
#     while c<len(magic_square):
#         x=magic_square[j][c]
#         s3=s3+x
#         break
#         c=c+1
#     k=k+1
# print(s3)
# if s1==s2==s3:
#     print("it is magic_square")
# else:
#     print("not")


        


     
# magic_square = [
#     [5, 3, 7],
#     [1, 8, 9],
#     [6, 4, 2]



# magic_square = [
    # [8, 3, 4],
    # [1, 5, 9],
    # [6, 7, 2]




# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         j=int(input("enter the number"))
#         b.append(j)
#     a.append(b)
# print("given number")
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end=" ")
#     print()
# sum1=0
# sum2=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             sum1=sum1+a[i][j]
#         if i+j==3-1:
#             sum2==sum2+a[i][j]
# if sum1!=sum2:
#     f=1
# else:
#     for i in range(3):
#         sum3=0
#         sum4=0
#         for j in range(3):
#             sum3=sum4+a[i][j]
#             sum3=sum4+a[i][j]
#         if sum3!=sum4:
#             f=1
#         elif sum3!=sum4:
#             f=1
#         else:
#             f=0
# if f!=0:
#     print("given number is magic squre")
# else:
#     print("not")



 
magic = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
sum=0
i=0
while i<len(magic):
    col=0
    while col<len(magic):
        sum=sum+magic[i][col]
        break
        col=col+1
    i=i+1
print(sum)
k=0
sum1=0
while k<len(magic):
    row=0
    while row<len(magic):
        sum1=sum1+magic[k][row]
        break
        row=row+1
    k=k+1
print(sum1)
y=0
sum2=0
while y<len(magic):
    dig=0
    while dig<len(magic):
        sum2=sum2+magic[y][dig]
        break
        dig=dig+1
    y=y+1
print(sum2)
if sum==sum1==sum2:
    print("Its magical square")
else:
    print("Its not magical square")
