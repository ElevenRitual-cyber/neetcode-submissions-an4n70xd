class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele=dict()
        n=len(nums)
        for i in range(n):
            e=nums[i]
            if e not in ele:
                ele[e]=1
            else:
                ele[e]=ele[e]+1
        ans=[]
        print(ele)
        for key in ele.keys():
            x=ele[key]
            if x>n//3:
                ans.append(key)
        return ans
        