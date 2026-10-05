class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        brackets = {"(": ")", "{": "}", "[": "]"} 
        for i in s:
            if i in brackets:
                my_stack.append(i)
            elif len(my_stack) == 0 or brackets[my_stack.pop()] != i:
                return False
        return len(my_stack) == 0

                