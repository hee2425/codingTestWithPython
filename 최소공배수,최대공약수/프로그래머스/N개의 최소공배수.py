from math import gcd   
def solution(arr):
                            
    answer = arr[0]                                 
    for num in arr:                                
        answer = answer*num // gcd(answer, num)  
        #최대 공약수 = 두수 곱//최소공배

    return answer