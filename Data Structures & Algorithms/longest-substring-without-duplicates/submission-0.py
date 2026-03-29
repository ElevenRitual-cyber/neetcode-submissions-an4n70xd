class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        start=end=0
        lmax=0
        k=len(s)
        while end<k:
            char=s[end]
            while char in seen:
                # keep removing the characters
                seen.remove(s[start])
                start+=1
            lmax=max(lmax,end-start+1)
            seen.add(char)
            end+=1
        return lmax

        