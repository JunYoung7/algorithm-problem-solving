import math

def solution(str1, str2):
    answer = 0
    
    arr1 = []
    arr2 = []
    
    # 2글자씩 잘라서 arr1, arr2에 추가 (영문자만 검사해서)
    for i in range(len(str1)-1):
        if (str1[i].isalpha() and str1[i+1].isalpha()):
            arr1.append(str1[i].lower() + str1[i+1].lower())
    
    for i in range(len(str2)-1):
        if (str2[i].isalpha() and str2[i+1].isalpha()):
            arr2.append(str2[i].lower() + str2[i+1].lower())
            
    union = arr1[:] # 다중집합 합집합
    arr1BasisForUnion = arr1[:] #합집합을 위한 검사용 arr1
    arr1BasisForIntersection = arr1[:] #교지합을 위한 검사용 arr2
    intersection = [] # 다중집합 교집합
    
    
    for alpha in arr2:
        if (alpha in arr1BasisForUnion):
            arr1BasisForUnion.remove(alpha) 
            # B에 있는 요소가 arr1에 있으면, arr1에서 지워줘야함. 그래야 B가 중복요소가 더 많을 때 해결
        else:
            union.append(alpha) # union에 추가 (union집합은 arr1 상태에서 시작)
            
        if (alpha in arr1BasisForIntersection):
            arr1BasisForIntersection.remove(alpha) # 지워주고 추가만 해주면 됨.
            intersection.append(alpha)
            
    return math.trunc((len(intersection) / len(union)) * 65536) if (len(union) != 0) else 65536 # len(intersection)이 0인것은 고려하면 X