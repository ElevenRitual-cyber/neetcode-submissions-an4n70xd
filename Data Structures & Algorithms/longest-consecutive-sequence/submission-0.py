class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)
        for num in numSet:
            if num-1 not in numSet:
                l=1
                x=num
                while x+1 in numSet:
                    x+=1
                    l+=1
                longest=max(l,longest)
        return longest


        