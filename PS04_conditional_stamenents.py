#Read a num from the user and check whether it is +ve , -ve or zero 
'''
Input : 10 
output : '+ve'

Input  : 0 
output : 'Zero'

Input : -5
output : '-ve'
'''
n = int(input())
if n > 0:
    print("+ve")
elif n == 0:
    print("zero")
else:
    print("-ve")
