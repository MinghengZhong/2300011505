for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 3:
        print(169)
        print(196)
        print(961)
    else:
        count = n-3
        for i in range(count//2+1):
            print('1'+'0'*i+'6'+'0'*i+'9'+'0'*(count-2*i))
            print('9'+'0'*i+'6'+'0'*i+'1'+'0'*(count-2*i))
        print('196'+'0'*count)
