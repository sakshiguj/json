# list1 = [1,2,3,4,5,6]
# list2 = [0,1,2,3,6,7]
# i=0
# t=[]
# for i in list1:
#     if i  not in  list2:
#         t.append(i)
# print(t)


list1 = [1,2,3,4,5,6]
list2 = [0,1,2,3,6,7]
i=0
t=[]
for i in list2:
    if i not in list1:
        t.append(i)  
print(t) 