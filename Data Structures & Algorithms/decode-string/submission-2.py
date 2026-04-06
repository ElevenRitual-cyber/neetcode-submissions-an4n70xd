class Solution:
    def decodeString(self, s: str) -> str:
        times=list()
        chars=list()
        num=0
        curr=str()
        for e in s:
            if e.isdigit():
                num=num*10+int(e)
            elif e=="[":
                times.append(num)
                chars.append(curr)
                curr=""
                num=0
            elif e=="]":
                temp=curr
                curr=chars.pop()
                c=times.pop()
                curr+=temp*c
            else:
                curr+=e
        return curr

        