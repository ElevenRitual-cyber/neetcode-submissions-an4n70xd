class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        n=len(nums)
        for ind in range(n):
            ele=nums[ind]
            if ele not in seen:
                seen[ele]=ind
        ans=list()
        print(seen)
        for ind in range(n):
            remain=target-nums[ind]
            if remain in seen and ind!=seen[remain]:
                if ind<seen[remain]:
                    ans.append(ind)
                    ans.append(seen[remain])
                else:
                    ans.append(seen[remain])
                    ans.append(ind)
                break

        # ans.sort()
        return ans
                
        