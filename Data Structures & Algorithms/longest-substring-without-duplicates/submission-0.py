class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = {}
        left = 0
        max_len = 0

        for right, r in enumerate(s):
            if r in result and result[r] >= left:
                left = result[r] + 1
            result[r] = right
            max_len = max(max_len, right - left + 1)

        return max_len
        
#         Longest Substring Without Repeating Characters
#         Task: Return the length of the longest substring containing no repeated characters.

# Method to implement:
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

# Parts list:
#   Data structures:
#     - dict: maps each character to the last index where you saw it
#     - or set: the characters currently inside the window
#     - two int variables: the window's left and right edges
#   Built-ins and methods:
#     - enumerate(s)
#     - key in my_dict  /  my_dict[key] = value
#     - max(a, b)
#     - set approach: my_set.add(value), my_set.remove(value)
#   Syntax and patterns:
#     - for right, char in enumerate(s):
#     - window length: right - left + 1
#     - set approach: a while loop that shrinks the window from the left