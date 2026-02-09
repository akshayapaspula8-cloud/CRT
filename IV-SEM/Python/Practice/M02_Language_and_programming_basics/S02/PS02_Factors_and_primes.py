'''
1)Count the factors of given number.

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i,end=" ")
print("Number of factors:", count)
'''
'''
2) Reverse Integer 

x = int(input())
r = int(str(abs(x))[::-1])*(-1 if x < 0 else 1)
print(r if -2**31 <= r <= 2**31 - 1 else 0)
A question on ascii value
'''
'''
is prime or not
n = int(input("enter a num:"))
count = 0 
for i in range(1, n+1):
    if n % i == 0 & n<=1 :
        print("not prime")
    else:
        print("prime")
'''