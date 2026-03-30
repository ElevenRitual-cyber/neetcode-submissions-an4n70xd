class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lm=float('inf')
        sums=0
        j=0
        for i in range(len(nums)):
            sums+=nums[i]
            while sums>=target:
                lm=min(i-j+1,lm)
                sums-=nums[j]
                j+=1
        return 0 if lm == float('inf') else lm
        