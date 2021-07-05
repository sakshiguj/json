char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
d=[]
while i<len(char_list):
    j=0
    a=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    a.append(char_list[i])
    a.append(count)
    if a  not in d:
        d.append(a)
    i=i+1
print(d)


