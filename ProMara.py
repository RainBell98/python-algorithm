def solution(participant,completion):
    for finish in participant:
        if finish in completion:
            participant.remove(finish)
    return participant[0]