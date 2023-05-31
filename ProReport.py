def solution(id_list,report,k):
    report_r = {x:0 for x in id_list}
    answer = {x:0 for x in id_list}

    report = set(report)
    report = list(report)
    for i in report:
        report_r[i.split()[1]]+=1
    for i in report:
        if report_r[i.split()[1]]>=k:
            answer[i.split()[0]]+=1

    return list(answer.values())




print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))