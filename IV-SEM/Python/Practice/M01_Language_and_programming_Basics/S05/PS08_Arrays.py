import numpy as np
arr = np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even number list is:",np.arange(2,10,2))
print("Odd number list is:",np.arange(1,10,2))

n = int(input("Enter the size"))
ele = list(map(int,input("enter else").split()))
print("Array Ele are:" ,np.array(ele))