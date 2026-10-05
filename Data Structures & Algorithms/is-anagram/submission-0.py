class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # str s, t
        if len(t) != len(s):
            return False 
        count = collections.defaultdict(int)
        for a in s:
        #     if a != 
            count[a] += 1
        #     else
        #         return true
        for a in t:
        #     if a != 
            count[a] -= 1
                # if count[a] < 0:
                #     return False
        return all(value == 0 for value in count.values())

        # lookup = collections.defaultdict(collections.deque)
        # for i, n in enumerate(t):
        #     lookup[n].append(i)
        # result = []
        # for n in s:
        #     result.append(lookup[n].popleft())
        # return result
        

