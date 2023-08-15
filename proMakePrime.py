from itertools import combinations, permutations
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums,3))
    for i in combi:
        if prime(sum(i)) == True:
            answer +=1
    return answer
print(solution([1,2,3,4]))