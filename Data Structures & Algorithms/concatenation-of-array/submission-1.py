class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=2*n
        ans=[0]
        ans=ans*x
        for i in range(2*n):
            ans[i]=nums[i%n]
        return ans
        