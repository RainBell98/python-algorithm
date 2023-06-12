import collections
def solution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    answer = list(answer)
    return answer[0]
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
