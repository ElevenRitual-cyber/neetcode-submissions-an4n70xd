class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        n=len(s)
        for i in range(n):
            maxc=0
            chm=[0]*26
            for j in range(i,n):
                char=s[j]
                chm[ord(char)-ord('A')]+=1
                maxc=max(maxc,chm[ord(char)-ord('A')])
                op=(j-i+1)-maxc
                if op>k:
                    break
                l=max(j-i+1,l)
        return l

        