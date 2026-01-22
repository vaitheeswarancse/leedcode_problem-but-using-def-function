def removeDuplicates(nums):
    l=1
    for i in range(1,len(nums)):
        if nums[i] !=nums[l-1]:
            l+=1
    return l
nums=[1,1,2]
print(removeDuplicates(nums))
