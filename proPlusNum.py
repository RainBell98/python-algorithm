def solution(num_list):
    answer1 = ""
    answer2 = ""
    for i in num_list:
        if i%2 == 0:
            answer1+=str(i)
        else:
            answer2+=str(i)
    answer = int(answer1)+int(answer2)
    return answer
print(solution([3, 4, 5, 2, 1]))