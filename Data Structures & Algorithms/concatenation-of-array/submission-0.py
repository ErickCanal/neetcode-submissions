class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        capacity = 2 * n

        newArr = [0] * capacity
        

        for i in range(n):
            newArr[i] = nums[i]
            newArr[i + n] = nums[i]
        return newArr
