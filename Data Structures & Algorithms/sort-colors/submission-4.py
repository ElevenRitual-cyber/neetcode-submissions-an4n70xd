class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        n=len(nums)
        i=0 #for zeors
        j=0 #for ones
        k=n-1 #for twos
        while j<=k:
            if nums[j]==1:
                j+=1
            elif nums[j]==2:
                swap(j,k)
                k-=1
            else:
                swap(i,j)
                i+=1
                j+=1
        