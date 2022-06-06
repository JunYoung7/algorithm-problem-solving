from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preDict = defaultdict(list)
        
        for i in prerequisites:
            preDict[i[0]].append(i[1]) # dictionary에 저장 
        
        visited = [] # 방문했던 history
        traced = [] 
        
        def dfs(node):        
            if node in visited:
                return True
            
            if node in traced:
                return False # 순환 = 수강할 수 없는 구조임
                      
            traced.append(node)
            
            for i in preDict[node]:
                if (dfs(i) == False):
                    return False
                
            traced.remove(node)
            
            visited.append(node)
            
            return True
            
        for i in range(numCourses):
            if (dfs(i) == False):
                return [] # 방법이 없음

        return visited