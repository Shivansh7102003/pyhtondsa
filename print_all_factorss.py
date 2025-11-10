n = int(input(" enter the number :"))

# wit complexity O(n)
factors = []
for i in range(1,n+1):
    if n%i ==0:
        factors.append(i)
    

print(factors)

# with O(n/2) complexity

fact = []

for i in range(1 , (n//2)+1):
    if n%i ==0:
        fact.append(i)
fact.append(n)        
print(fact)



# with O(n^1/2) complexity
result = []
for i in range(1 , int(n**(1/2)+1)):
    if n%i == 0:
        result.append(i)
        if n//i !=i:
            result.append(n//i)
        
print(result)