# to find the frequncy of number present in the list and store them in dictionary in form of key value pair 
num = [5,6,7,8,4,4,6,4,6,48,2,4,2,6,7,2,4,5,2]
frequency_map = {}

for i in range(0 , len(num)):
    if num[i] not in frequency_map:
        frequency_map[num[i]] = 1
    else :
        frequency_map[num[i]] = frequency_map[num[i]]+1
        
print(frequency_map)


# method 2 using hashmaps 

hash_maps  = {}

for i in range(0,len(num)):
    hash_maps[num[i]]= hash_maps.get(num[i] , 0) +1
    
print(hash_maps) 