# from collections import Counter
# import math
# nlist = list(input())

# for i in range(len(nlist)):
#     if nlist[i] =='6':
#         nlist[i] = '9'

# counter = Counter(nlist)
# max_num = max(counter, key = counter.get)

# if max_num == '9':
#     print(math.ceil(counter[max_num]/2))
# else:
#     print(counter[max_num])

word = input()

nums= [0]*10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num==9:
        if nums[6]<=nums[9]:
            nums[6]+=1
        else:
            nums[9]+=1 
    else:
        nums[num] +=1

print(max(nums))