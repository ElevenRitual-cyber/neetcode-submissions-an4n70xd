class Solution:
    def isValid(self, s: str) -> bool:
        # keep pushing if it is opening 
        if len(s)<=1 or len(s)==0:
            return False
        stack=list()
        open={'(','{','['}
        for b in s:
            if b in open:
                stack.append(b)
            else:
                # if closing and peek are same then pop
                # else return false
                if len(stack)==0:
                    return False
                if b==')' and stack[-1]=='(':
                    stack.pop()
                elif b==']' and stack[-1]=='[':
                    stack.pop()
                elif b=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

            
        