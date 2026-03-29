class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        see=dict()
        for i ,e in enumerate(nums):
            if e in see and abs(see[e]-i)<=k:
                return True
            see[e]=i
                
        return False