class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # greedy하게 앞에부터 순서대로 검사함
        numCheckList = list()
        
        numCheckList.append(num[0]) # 첫번째 수

        for i in range(1, len(num)):
            while (len(numCheckList) > 0 and k > 0 and int(num[i]) < int(numCheckList[-1])): # 검사리스트의 최상단 숫자와 현재 숫자를 검사하면서
                numCheckList.pop() # 현재 num[i]가 검사리스트 숫자보다 더 작으면 빼줌
                k -= 1 
                   
            numCheckList.append(num[i]) # 현재 숫자를 push
        
        zeroCnt = 0

        while (k > 0): # K가 남아있으면 뒤에서부터 빼줌
            numCheckList.pop() 
            k -= 1
            
        for i in numCheckList: # 앞에오는 0 개수 count
            if (i != '0'):
                   break
            zeroCnt += 1

        numCheckList = numCheckList[zeroCnt:]
                   
        if (len(numCheckList) == 0):
                   return '0'
                   
        return("".join(numCheckList))
                   
                
        
                  
            