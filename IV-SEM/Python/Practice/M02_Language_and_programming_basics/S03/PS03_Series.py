'''
Docstring for Python.Practice.M02_Language_and_programming_basics.S03.PS03_Series
1)arthimetic series
a = int(input())
d = int(input())
for i in range(10):
    print(a+(i*d))
    
2)fabbinaci serirs
a=0 
b=1
n=int(input())
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b 

using list
li = [0,1]
n = int(input())
for i in range(2,n):
    li.append(li[i-2] + li[i-1])
print(li)

power of a number

n = int(input())
for i in range(1,11):
    print(n**i , end=" ")
    '''
