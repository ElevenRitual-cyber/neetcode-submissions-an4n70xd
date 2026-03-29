class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        ans=[]
        while i<j:
            temp=numbers[i]+numbers[j]
            if temp==target:
                ans.extend([i+1,j+1])
                break
            elif temp<target:
                i+=1
            else:
                j-=1
        return ans

        