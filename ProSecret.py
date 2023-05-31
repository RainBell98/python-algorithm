def plus(x):
    x = list(x)
    x_r = []
    k = []
    a,b,c = '','',''
    for i in range(len(x)):
        if x[i].isnumeric() == True:
            x_r.append(x[i])
    for i in range(len(x_r)):
        if i<4:
            a += x_r[i]
        elif 4<=i<6:
            b += x_r[i]
        else:
            c += x_r[i]
    k.append(a)
    k.append(b)
    k.append(c)
    return k

def solution(today,terms,privacies):
    today = list(today)
    today_r = []
    terms_r = []
    privacies_r = []
    answer = []
    answer2 = []
    for i in range(len(today)):
        if today[i].isnumeric() == True:
            today_r.append(today[i])
    today_f = plus(today_r)
    for i in range(len(terms)):
        a = terms[i].split()
        terms_r.append(a)
    for i in range(len(privacies)):
        a = privacies[i].split()
        privacies_r.append(a)
    for i in range(len(privacies_r)):
        privacies_f = plus(privacies_r[i][0])
        for j in range(len(terms_r)):
            if privacies_r[i][1] == terms_r[j][0]:
                size = int(terms_r[j][1])
                month = int(privacies_f[1])+size
                day = int(privacies_f[2])
                if day == 28:
                    month += 1
                if month>12:
                    year = int(privacies_f[0])+1
                    month -= 12
                    privacies_f[0] = year

                privacies_f[1] = month
        if int(today_f[0])<int(privacies_f[0]):
            answer.append(i+1)
        elif int(today_f[0]) == int(privacies_f[0]):
            if int(today_f[1]) < int(privacies_f[1]):
                answer.append(i+1)
            elif int(today_f[1])==int(privacies_f[1]):
                if int(today_f[2])<int(privacies_f[2]):
                    answer.append(i+1)
    for j in range(len(privacies)):
        answer2.append(j+1)
    for j in answer:
        for s in answer2:
            if j == s:
                answer2.remove(s)


    return answer2

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A","2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
#print(plus("2022.05.19"))