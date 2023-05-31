def solution(record):
    s = []
    info = dict()
    answer = []
    for i in range(len(record)):
        k = record[i].split(" ")
        s.append(k)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][0] == "Enter" or s[i][0] == "Change":
                info[s[i][1]] = s[i][2]
    for i in s:
        if i[0] == "Enter":
            answer.append(info[i[1]]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(info[i[1]]+"님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))