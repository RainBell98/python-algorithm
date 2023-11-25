def solution(arr,n):
    for i in range(n):
        arr.append(arr[i])
        arr.remove(arr[i])
    return arr
print(solution([2, 1, 6],1))