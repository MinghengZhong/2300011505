while True:
    day = int(input())
    if day == 0:
        break
    n = int(((1+8*day)**.5-1)/2)
    print('%d %d' % (day, int(n*(n+1)*(2*n+1)/6)+(day-int(n*(n+1)/2))*(n+1)))
