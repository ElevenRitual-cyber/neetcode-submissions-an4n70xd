class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list()
        for index,value in enumerate(speed):
            cars.append((position[index],speed[index]))
        cars=sorted(cars,key=lambda x:x[0],reverse=True)
        # make a stack now
        stack=list()
        for p,s in cars:
            # if stack is empty just put it
            speed=(target-p)/s
            if not stack:
                stack.append(speed)
            if stack[-1] <speed:
                stack.append(speed)


        
        return len(stack)
        