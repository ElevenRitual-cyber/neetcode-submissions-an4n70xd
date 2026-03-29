class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        l=0
        r=n-1
        t=0
        while t<=r:
            if nums[t]==0:
                # swap(l,t)
                nums[l],nums[t]=nums[t],nums[l]
                l+=1
            elif nums[t]==2:
                # swap(r,t)
                nums[r],nums[t]=nums[t],nums[r]
                r-=1
                t-=1
            t+=1

        