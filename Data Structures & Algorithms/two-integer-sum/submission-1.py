class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #output is list
        # return i and j
        # for i in nums:
        #     n[i]
        #     for j in nums:
        #     n[j] 
        passedValues = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in passedValues:
                return[passedValues[diff],i]
            passedValues[n] = i
        return