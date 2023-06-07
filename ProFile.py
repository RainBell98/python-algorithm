def solution(files):
    arr = []
    answer = []

    for file in files:
        file = list(file)
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if file[i].isnumeric():
                head = file[:i]
                number = file[i:]
                for j in range(len(number)):
                    if number[j].isnumeric()==False:
                        number = number[:j]
                        tail = number[j:]
                        break
                arr.append([head,number,tail])
                break
    arr = sorted(arr,key = lambda x:(x[0].upper(),int(x[1])))

    return [''.join(i) for i in arr]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

