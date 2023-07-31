def solution(myString):
    return myString.lower()

def solution(arr1, arr2):
    if len(arr1)>len(arr2):
        return 1

def solution(num_list):
    answer = 1
    for i in num_list:
        answer *= i
    return sum(num_list)
    if len(num_list) >= 11 else answer
    elif len(arr1)<len(arr2):
        return -1
    else:
        if sum(arr1)>sum(arr2):
            return 1
        elif sum(arr2)>sum(arr1):
            return -1
        else:
            return 0
return answer