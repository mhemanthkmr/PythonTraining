# a = [1,2,2,2,3,3,4,5]

# N = len(a)

# hash = [0] * (max(a) + 1) 

# for i in range(N):
#     hash[a[i]] += 1

# answer = []

# index = 0
# for i in hash:
#     if(i == 1) : 
#         answer.append(index)
#     index+=1

# print(hash)
# print(answer)


map = {}
a = [1,2,2,2,3,3,4,5]

for i in a :
    map[i]=map.get(i,0)+1

print(map)


# from collections import Counter

# elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 1, 1, 1, 2, 2]

# # Using collections.Counter for comparison
# counter_dict = Counter(elements)
# print("Counter frequency count:",counter_dict)