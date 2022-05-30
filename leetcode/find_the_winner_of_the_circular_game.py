class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i for i in range(1,n+1)]
        now = 1
        
        
        while(len(queue) > 1):
            nowIndex = queue.index(now)
            nextNow = queue[(nowIndex+k)%len(queue)]
            del queue[(nowIndex+k-1)%len(queue)]
            nowIndex = queue.index(nextNow)
            
            now = nextNow
            
        return queue[0]
        