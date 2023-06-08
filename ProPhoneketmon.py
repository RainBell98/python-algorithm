def solution(nums):
    p_cnt = len(nums)//2
    nums = set(nums)
    arr = list(nums)
    if p_cnt <= len(arr):
        return p_cnt
    elif p_cnt>len(arr):
        return len(arr)
print(solution([3,3,3,2,2,4]))
