class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, s in enumerate(nums):
            diffr = target - s
            if diffr in result:
                return [result[diffr], i]
            else:
                result[s] = i
        return []