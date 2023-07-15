def solution(money):
    answer = []
    res = money // 5500
    answer.append(res)
    answer.append(money - 5500 * res)

    return answer

def solution(slice, n):
    return (n-1)//slice+1

def solution(num_list):
    num_list.reverse()
    return num_list

def solution(n):
    ans = n//7
    if ans*7 < n:
        ans += 1
    return ans

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

def solution(my_string, letter):
    return my_string.replace(letter,"")

def solution(array, n):
    return array.count(n)

def solution(my_string):
    answer = ''
    my_string = list(my_string)
    my_string.reverse()
    for i in my_string:
        answer += i
    return answer

def solution(numbers, num1, num2):
    ans = []
    for i in range(num1,num2+1):
        ans.append(numbers[i])
    return ans

def solution(sides):
    return 1 if max(sides)<sum(sides)-max(sides) else 2


def solution(my_string):
    my_string = list(my_string)
    arr = ""
    for i in my_string:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            arr += i
    return arr
