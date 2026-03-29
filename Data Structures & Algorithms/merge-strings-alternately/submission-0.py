class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn=0
        n=len(word1)
        n2=len(word2)
        i=0
        j=0
        ans=str()
        while i<n and j<n2:
            if turn==0:
                ans+=word1[i]
                i+=1
            elif turn==1:
                ans+=word2[j]
                j+=1
            turn^=1
        while i<n:
            ans+=word1[i]
            i+=1
        while j<n2:
            ans+=word2[j]
            j+=1
        return ans
        