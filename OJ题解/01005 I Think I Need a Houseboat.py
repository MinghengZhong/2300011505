import math
n=int(input())
for i in range(0,n):
    s=list(map(float,input().split()))
    S=math.pi*(s[0]**2+s[1]**2)/2
    ans=1
    b=True
    while b:
        S-=50.0
        if S<=0:
            print('Property '+str(i+1)+': This property will begin eroding in year '+str(ans)+'.')
            b=False
        else:
            ans+=1
print('END OF OUTPUT.')