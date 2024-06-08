def check(n):
    if n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True


n = int(input())
for i in range(int(n/2)+1, 1, -1):
    if check(i):
        if check(n-i):
            print(i*(n-i))
            break
