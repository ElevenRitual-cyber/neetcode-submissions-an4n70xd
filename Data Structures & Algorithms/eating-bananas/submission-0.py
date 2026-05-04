class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(mid):
            t = 0
            for b in piles:
                t += (b + mid - 1) // mid   # FIXED
            return t <= h

        left = 1
        right = max(piles)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if isValid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans