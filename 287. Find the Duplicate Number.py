def findDuplicates(nums):
    i=0
    l=0
    nums.sort()
    for i in range(i,len(nums)):
        if nums[i] ==nums[l+1]:
            return nums[i]
nums=[1,3,4,2,2]
print(findDuplicates(nums))
