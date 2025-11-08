# to find out that the input number is palindrome or not
n = int(input(" enter the number:"))
num = n
result = 0
while num>0:
    id = num%10
    result= (result*10)+ id
    num = num//10
    
print(result == n)  