class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i , num in enumerate(nums):
            print(i)
            plcHold = target - num
            
            if plcHold in res:
                return [res[plcHold], i]
            res[num] = i
