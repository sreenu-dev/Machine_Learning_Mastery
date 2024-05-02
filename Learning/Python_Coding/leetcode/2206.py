from typing import List


def divideArray(nums: List[int]) -> bool:
    num_dict=dict()
    for num in nums:
        if num in num_dict:
            num_dict[num]=num_dict[num]+1
        else:
            num_dict[num]=1
    for key in num_dict:
        print(num_dict[key]%2)
        if num_dict[key]%2!=0:
            return False
    return True

nums=[3,2,3,2,2,2]
print(divideArray(nums))