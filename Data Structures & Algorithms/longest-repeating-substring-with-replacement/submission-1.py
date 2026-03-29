class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxc=0
        mapch=[0]*26
        j=0
        l=0
        for i in range(len(s)):
            char=s[i]
            mapch[ord(char)-ord('A')]+=1
            maxc=max(maxc,mapch[ord(char)-ord('A')])
            
            while (i-j+1)-maxc>k:
                ch=s[j]
                mapch[ord(ch)-ord('A')]-=1
                maxc=max(maxc, mapch[ord(ch)-ord('A')])
                j+=1
            l=max(l,i-j+1)


        return l