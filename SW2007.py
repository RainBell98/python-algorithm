T = int(input())

testcase = []
for i in range(T):
    testcase.append(input())

for i in range(T):
    test = testcase[i]
    pattern = test[0]
    end_point = 1
    while True:
        if pattern == test[len(pattern):len(pattern) * 2]:
            break
        pattern = test[:end_point]
        end_point += 1
    print("#{} {}".format((i+1), len(pattern)))
