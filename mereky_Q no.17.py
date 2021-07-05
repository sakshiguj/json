mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr=mainStr.split()
i=0
while i<len(substr):
    over=0
    if "over" in substr:
        substr.remove("over")
    i=i+1
print(substr)







