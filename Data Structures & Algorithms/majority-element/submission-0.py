class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=0
        candidate=-1
        for ele in nums:
            if vote==0:
                candidate=ele
            vote+=(1 if ele==candidate else -1)
        return candidate
        