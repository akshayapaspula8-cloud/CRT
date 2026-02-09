'''
1) write a python code to count the digits of the number?
ex:15678-->output:5

num = 15678
count = len(str(num))
print(f"Number of digits:{count}")


2) sum of the digits of a number?
ex: 12345-->1+2+3+4+5=15

num  = 12345
digits_sum = sum(int(digit)for digit in str(num))
print(f"sum of digits:{digits_sum}")

num = int(input("enter num"))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(sum)


3)product of a given number?

num = int(input())
sum = 1  
while num > 0:
    sum *= num % 10
    num //= 10
print(sum)


4)reverse the given number?

num = int(input("Enter a number: "))
rev = 0
while num  > 0:
    digit = num % 10
    rev  = rev * 10 + digit
    num //=10
print("Reversed number:",rev)


5) count the even and odd digits?

n = int(input("enter n:"))
even = 0
odd =0
while n>0:
    d = n%10
    if d%2==0:
        even +=1
    else:
        odd+=1
    n//=10
print(even)
print(odd)
'''
