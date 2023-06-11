def solution(citations):
    citations.sort()
    for i,citiation in enumerate(citations):
        if citiation>=len(citations)-i:
            return len(citations)-i
    return 0
