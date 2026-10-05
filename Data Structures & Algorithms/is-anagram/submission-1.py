class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False 
        count = collections.defaultdict(int)
        for a in s:
            count[a] += 1
        for a in t:
            count[a] -= 1
        return all(value == 0 for value in count.values())

    
        

