def judge(s):
    l = []
    for a in s:
        if a in l:
            return False
        else:
            l.append(a)
    return True


s = input()
n = int(s)
while True:
    n += 1
    if judge(str(n)):
        print(n)
        break
