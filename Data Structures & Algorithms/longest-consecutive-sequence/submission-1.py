class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        e=set(nums)
        mc=0
        for i in range(len(nums)):
            ele=nums[i]
            
            c=1
            if ele-1 in e:
                continue
            while ele+1 in e:
                ele+=1
                c+=1
            mc=max(mc,c)
        return mc

        