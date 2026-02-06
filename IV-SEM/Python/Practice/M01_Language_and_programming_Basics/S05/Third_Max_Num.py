nums = list(map(int,input("Enter nums:").split()))
if len(set(nums)) >=3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))