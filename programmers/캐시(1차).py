from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    
    if (cacheSize == 0):
        return len(cities) * 5
    
    for city in cities: 
        city = city.upper()
        try: # cache hit
            cache.remove(city) # 캐시 앞에 있는 city를 날려주고 가장 최근에 사용되도록 뒤에 추가해줌
            cache.append(city)
            answer += 1 
            continue
        except:
            pass
        
        # cache miss
        if (len(cache) >= cacheSize):
            cache.popleft() 
        
        cache.append(city)
        answer += 5
            
    return answer