def solution(phone_book):
    check = 0
    for i in range(len(phone_book)):
        for j in phone_book:
            if phone_book[i] in j:
                check += 1
                continue
    if check >len(phone_book):
        return False
    else:
        return True


print(solution(	["119", "97674223", "1195524421"]))