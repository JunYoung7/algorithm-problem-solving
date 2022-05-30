class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        tmp = ''
        stack = []
        tmp = ''
        tmpNumber = ''

        for i in range(len(s)):
                print(stack)
                if(s[i] == ']'):
                    while(len(stack) != 0 and stack[-1] != '['):
                        tmp = stack.pop() + tmp
                        
                    stack.pop()
                    while(len(stack) != 0 and stack[-1].isdigit()):
                        tmpNumber = stack.pop() + tmpNumber
                    
                    if (len(tmpNumber) > 0):
                        tmp = tmp * int(tmpNumber)
                    
                    stack.append(tmp)
                                                                    
                    tmpNumber = ''
                    tmp = ''
                else:
                    stack.append(s[i])
                    
        return "".join(stack)
                    
                