def solution(array,commands):
    res = []
    array.insert(0,0)
    for i in range(len(commands)):
        arr = []
        for j in range(len(array)):
            if commands[i][1]>=j>=commands[i][0]:
                arr.append(array[j])
        arr.sort()
        arr.insert(0,0)
        res.append(arr[commands[i][2]])
    return res