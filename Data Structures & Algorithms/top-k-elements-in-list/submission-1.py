import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=dict()
        for ele in nums:
            if ele not in arr:
                arr[ele]=1
            else:
                arr[ele]+=1
        data=[]
        for key in arr.keys():
            data.append((-arr[key],key))

        heapq.heapify(data)
        ans=[]
        while k>0:
           f,num= heapq.heappop(data)
           ans.append(num)
           k-=1


        return ans


        