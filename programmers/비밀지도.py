def solution(n, arr1, arr2):
    answer = []
    
    temp1 = [['' for i in range(n)] for j in range(n)]
    temp2 = [['' for i in range(n)] for j in range(n)]
    answer = []

    for i in range(n):
        tempStr = ''
        num1 = arr1[i]
        num2 = arr2[i]
        
        # 2진수로 변환
        for j in range(n):
            temp1[i][j] = '#' if (num1 // pow(2,n-1-j) == 1) else ''
            num1 = num1 % pow(2,n-1-j)
            temp2[i][j] = '#' if (num2 // pow(2,n-1-j) == 1) else ''
            num2 = num2 % pow(2,n-1-j)
        
        # 최종 answer에 추가될 값 계산위에 두 배열의 # 여부를 확인
        for j in range(n):
            tempStr = tempStr + ('#' if (temp1[i][j] == '#' or temp2[i][j] == '#') else ' ')            
        
        answer.append(tempStr)
        
    return answer