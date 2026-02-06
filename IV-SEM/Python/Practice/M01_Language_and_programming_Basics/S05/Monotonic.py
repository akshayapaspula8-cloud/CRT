nums = list(map(int,input("enter num").split()))
inc = True
dec = True
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        dec=False
    if nums[i]<nums[i-1]:
        inc=False
if inc or dec:
    print("Monotonic Array")
else:
    print("not monotonic array")

