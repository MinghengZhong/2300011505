n = int(input())
numbers = {}
duplicate = False
for i in range(0, n):
    s = input()
    a = ''
    for j in range(0, len(s)):
        if s[j] == '-':
            continue
        elif s[j] == '0':
            a += '0'
        elif s[j] == '1':
            a += '1'
        elif s[j] == 'A' or s[j] == 'B' or s[j] == 'C' or s[j] == '2':
            a += '2'
        elif s[j] == 'D' or s[j] == 'E' or s[j] == 'F' or s[j] == '3':
            a += '3'
        elif s[j] == 'G' or s[j] == 'H' or s[j] == 'I' or s[j] == '4':
            a += '4'
        elif s[j] == 'J' or s[j] == 'K' or s[j] == 'L' or s[j] == '5':
            a += '5'
        elif s[j] == 'M' or s[j] == 'N' or s[j] == 'O' or s[j] == '6':
            a += '6'
        elif s[j] == 'P' or s[j] == 'R' or s[j] == 'S' or s[j] == '7':
            a += '7'
        elif s[j] == 'T' or s[j] == 'U' or s[j] == 'V' or s[j] == '8':
            a += '8'
        elif s[j] == 'W' or s[j] == 'X' or s[j] == 'Y' or s[j] == '9':
            a += '9'
    if a not in numbers.keys():
        numbers[a] = 1
    else:
        numbers[a] = numbers[a]+1
        duplicate = True
if duplicate:
    numbers = dict(sorted(numbers.items()))
    for a in numbers.keys():
        if numbers[a] >= 2:
            print(a[0:3]+'-'+a[3:7]+' '+str(numbers[a]))
else:
    print('No duplicates.')
