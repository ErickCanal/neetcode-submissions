class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums)
        nums.sort()
        # while left < right:
        for i in range(len(nums)):
            nums[i] == nums[i - 1]
            # result.append([a,b,c])


# -------
# Task: Return unique triplets whose values sum to zero.

# Method to implement:
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:

# Parts list:
#   Data structures:
#     - list of lists: the triplets you return
#     - the sorted input list
#     - three int variables: the fixed index i and the left and right pointers
#   Built-ins and methods:
#     - nums.sort(): sorts in place
#     - len(nums)
#     - range(len(nums))
#     - result.append([a, b, c])
#   Syntax and patterns:
#     - for i in range(...):
#     - continue: skip to the next loop round
#     - while left < right:
#     - left += 1  /  right -= 1
#     - comparing neighbors: nums[i] == nums[i - 1]