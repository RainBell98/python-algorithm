def solution(cipher, code):
    answer = ''
    cipher = list(cipher)
    for i in range(len(cipher)):
        if((i+1)%code == 0):
            answer+=cipher[i]
    return answer