numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
b=[]
i=0
count=0
while i<len(numbers):
    a=numbers[i]
    if a>20 and a<40:
        b.append(a)
        count=count+1
    i=i+1
print(b,count)






































































# numbers.sort()
# max=numbers[-1]
# print("max numbers=",max)

# u=[]
# num=int(input("enter the number"))
# for i in range(num):
#     num=int(input("enter the number"))
#     u.append(num)
# print("maximum  numbers is=",max(u))

#  a=numbers[0]
# a1=max(numbers)
# print(a1)

