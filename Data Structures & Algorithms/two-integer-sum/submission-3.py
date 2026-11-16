class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i, s in enumerate(nums):
            leftO = target - s
            if leftO in result:
                return [i, result[leftO]]
            else:
                result[s] = i
        return []