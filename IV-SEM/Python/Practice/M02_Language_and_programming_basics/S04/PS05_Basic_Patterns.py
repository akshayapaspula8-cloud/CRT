'''
input = 4 
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

2) input 4 
* 
* * 
* * * 
* * * *
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

3) n = 4 
output: * * * * 
        * * * 
        * * 
        *

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    
4] n = 4 
output : 1
         2 3
         4 5 6
         7 8 9 10 

k = 1
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k += 1 
    print()
    
5] n = 4 
output:
A 
A B 
A B C 
A B C D 
print(ord('A'))
print(char(65))

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

    
6]input : 4
output:
A 
B C
D E F
G H I J
n = int(input())
k = 65 
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k += 1 
    print()
    
7] input:4 
output:
* * * *
*     *
*     *
* * * *
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
