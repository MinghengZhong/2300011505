'''
class tree:
    def __init__(name, value):
        name.value = value
        name.left = None
        name.right = None
'''

s = input()
n = int(input())
l = [0]*len(s)
dic = {}
quotes = []
for i in range(n):
    ss, num = input().split()
    dic[ss] = int(num)
quote = 0
for i in range(len(s)):
    if s[i] == '(':
        quote += 1
    elif s[i] == ')':
        quote -= 1
    quotes.append(quote)
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-':
        for j in range(len(s)):
            if quotes[i] <= quotes[j] and i != j:
                l[j] += 1
    elif s[i] == '*' or s[i] == '/':
        if quotes[i-1] == quotes[i]:
            l[i-1] += 1
        else:
            for j in range(i-1, -1, -1):
                if quotes[j] == quotes[i]:
                    break
                l[j] += 1
        if quotes[i+1] == quotes[i]:
            l[i+1] += 1
        else:
            for j in range(i+1, len(s)):
                if quotes[j] == quotes[i]:
                    break
                l[j] += 1
for i in range(0, max(l)+1):
    for j in range(0, len(s)):
        if s[j] != '(' and s[j] != ')':
            if l[j] == i:
                print(s[j], end='')
            else:
                print(' ', end='')
    print('')
