from typing import List

def countElements(nums: List[int]) -> int:
    nums.sort()
    if(nums[0]==nums[len(nums)-1]):
        return 0;
    else:
        higherNumber=nums[len(nums)-1]
        lowerNumber=nums[0]
        count=0
        for i in range(len(nums)):
            if nums[i]!=higherNumber and nums[i]!=lowerNumber:
                count+=1
        return count;
    # higherNumber=max(nums)
    # lowerNumber=min(nums)
    # count=0
    # if higherNumber==lowerNumber:
    #     return 0
    # for i in range(len(nums)):
    #     if nums[i]!=higherNumber and nums[i]!=lowerNumber:
    #         count+=1
    # return count;

inp=[11,7,2,15]
inp2=[1,3,1,3]

print(countElements(inp2))


