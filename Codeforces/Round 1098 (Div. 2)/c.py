'''
find b closest to a st. b is only made of digits d1 or d2

b could either be the smallest number that is 1 digit longer
largest number that is 1 digit shorter
closest in terms of same len..?
'''

'''
700
6 7
677
'''


#highkey hardcoding this
q = int(input())
for _ in range (q):
    inp = input().split()
    a, n = inp[0], inp[1]
    d = input().split()

    if d[0] == '0':
        s = int(d[1] + ('0' * len(a))) - int(a)
    else:
        s = int(d[0] * (len(a)+1)) - int(a)
    
    if (len(a)>=2):
        s = min(s, int(int(a) - int(d[1] * (len(a)-1))))

    num = ""
    for i in range(len(a)):
        cand = num + d[1] + d[0] * (len(a)-i-1)

        if int(cand) <= int(a):
            num += d[1]
        else:
            cand = num + d[0] + d[1] * (len(a)-i-1)

            if not (len(a) > 1 and i == 0 and d[0] == '0') and int(cand) <= int(a):
                num += d[0]
            else:
                break

    if len(num) == len(a):
        s = min(s, abs(int(num)-int(a)))
    
    num = ""
    for i in range(len(a)):
        cand = num + d[0] + d[1] * (len(a)-i-1)

        if not (len(a) > 1 and i == 0 and d[0] == '0') and int(cand) >= int(a):
            num += d[0]
        else:
            cand = num + d[1] + d[0] * (len(a)-i-1)
            if int(cand) >= int(a):
                num += d[1]
            else:
                break
    if len(num) == len(a):
        s = min(s, abs(int(num)-int(a)))

    print(s)
