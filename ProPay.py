def solution(fees, records):
    s = []
    info = dict()
    for i in range(len(records)):
        k = records[i].split()
        s.append(k)
    p = []
    for parking in s:
        if parking[2] == "IN":
            info[parking[1]] = parking[0]
        elif parking[2] == "OUT":
            time = info[parking[1]]
            time2 = parking[0]
            time = time.split(":")
            time2 = time2.split(":")
            pay = (int(time2[0])*60+int(time2[1])) - ((int(time[0])*60)+int(time[1]))
        if pay<=fees[0]:
            p.append(fees[1])
        else:
            p.append(fees[1]+((pay-fees[0])/10)*600)
    return p
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))