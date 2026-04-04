class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand=list()
        for e in tokens:
            if e not in "+*/-":
                operand.append(int(e))
                print(operand)
            else:
                op2=operand.pop()
                op1=operand.pop()
                result=0
                if e== "+":
                    result=op1+op2
                elif e=="-":
                    result=op1-op2
                elif e=="*":
                    result=op1*op2
                elif e=="/":
                    result=int(op1/op2)
                operand.append(result)
            # print(operand)
        print(operand)
        return operand.pop()


        