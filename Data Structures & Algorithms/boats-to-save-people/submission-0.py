class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        i=0
        j=n-1
        a=0
        while i<=j:
            sum=people[i]+people[j]
            if sum<=limit:
                a+=1
                i+=1
                j-=1
            else:
                a+=1
                j-=1
        return a

        