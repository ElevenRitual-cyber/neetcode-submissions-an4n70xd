class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        anss=right
        while left<=right:
            mid=left+(right-left)//2
            est=1
            tem=0
            for w in weights:
                tem+=w
                if tem>mid:
                    est+=1
                    tem=w
            if est<=days:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans