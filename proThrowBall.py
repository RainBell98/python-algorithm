def solution(numbers,k):
    return numbers[2 * (k - 1) % len(numbers)]
print(solution([1, 2, 3, 4],2))