s = input()
count = 0
for a in s:
    count = (count << 1)+int(a)
    if count % 5 == 0:
        print(1, end='')
    else:
        print(0, end='')
