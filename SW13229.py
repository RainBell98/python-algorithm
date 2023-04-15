N = int(input())
for i in range(N):
    n = input()
    if n == 'SUN':
        print("#{}".format(i+1),'7')
    elif n == 'MON':
        print("#{}".format(i+1),'6')
    elif n == 'TUE':
        print("#{}".format(i+1),'5')
    elif n == 'WED':
        print("#{}".format(i+1),'4')
    elif n == 'THU':
        print("#{}".format(i+1),'3')
    elif n == 'FRI':
        print("#{}".format(i+1),'2')
    else:
        print("#{}".format(i+1),'1')