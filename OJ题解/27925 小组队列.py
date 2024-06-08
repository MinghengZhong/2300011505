from collections import defaultdict as D
t = int(input())
num = {}
tail_list = ['' for _ in range(t)]
next, head, tail = D(str), '', ''
for i in range(t):
    for new in input().split():
        num[new] = i
while (s := input()) != 'STOP':
    if s[0] == 'D':
        print(head)
        if tail_list[num[head]] == head:
            tail_list[num[head]] = ''
        head = next[head]
    else:
        new = s[8:]
        if not head:
            head = new
            tail = new
        else:
            Tail = tail_list[num[new]]
            if Tail:
                next[new], next[Tail] = next[Tail], new
                if Tail == tail:
                    tail = new
            else:
                next[tail] = new
                tail = new
        tail_list[num[new]] = new
