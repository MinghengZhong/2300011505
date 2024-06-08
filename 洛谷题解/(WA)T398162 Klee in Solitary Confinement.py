n, k = map(int, input().split())
l = list(map(int, input().split()))
num = [l[0]]
count = {l[0]: 1}
continue_count = {l[0]: 1}
current = l[0]
current_continue = 1
for i in range(1, n):
    if l[i] == current:
        count[current] = count[current]+1
        current_continue += 1
        if current_continue > continue_count[current]:
            continue_count[current] = current_continue
    else:
        current = l[i]
        current_continue = 1
        if current in num:
            count[current] = count[current]+1
            if current_continue > continue_count[current]:
                continue_count[current] = current_continue
        else:
            num.append(current)
            count[current] = 1
            continue_count[current] = 1

ans = max(count.items(), key=lambda x: x[1])[1]
for i in range(len(num)):
    for j in range(len(num)):
        if num[j]+k == num[i]:
            if count[num[i]]+continue_count[num[j]] > ans:
                ans = count[num[i]]+continue_count[num[j]]
print(ans)
