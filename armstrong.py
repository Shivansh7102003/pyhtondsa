# check if the umber is armstrong 

n = int(input(" enter the number:"))

num = n
length = len(str(num))

result = 0
while num >0:
    
    id = num%10
    result = result + id**length
    num = num//10
    
print(result == n)
