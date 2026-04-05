class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        x=[0]*len(temperatures)
        stack=list()
        for i,e in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<e:
                k=stack.pop()
                x[k]=i-k
            stack.append(i)
        print(x)
        return x
        