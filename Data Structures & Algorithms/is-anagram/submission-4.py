class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen=dict()
        for char in s:
            if char not in seen:
                seen[char]=1
            else:
                seen[char]+=1
        for char in t:
            if char in seen:
                seen[char]-=1
            else:
                return False
        for v in seen.values():
            if v!=0:
                return False
        return True
        