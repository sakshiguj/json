number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19,]
i=0
b=[]
while i<len(n):
    j=len(n)-1
    while j>4:
        if n[i]+n[j]== number:
            b.append([n[i],n[j]])
        j=j-1
    i=i+1
print(b)

















































# number=30
# n=[10,11,12,13,14,16,17,18,19,20,15]
# i=0
# l=len(n)
# a=[]
# while i<l:
#     j=len(n)-1
#     while j>l//2:
#         if n[i]+n[j]==number:
#             a.append([n[i],n[j]])
#         j=j-1
#     i=i+1
# print(a)

# 


