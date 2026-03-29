class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=dict()
        for ele in nums:
            if ele not in seen:
                seen[ele]=1
            else:
                seen[ele]+=1
            if seen[ele]==2:
                return True
        return False

        