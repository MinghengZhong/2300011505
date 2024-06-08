N = int(input())
dic = {'byte': 1, 'short': 2, 'int': 4, 'long': 8}
slen={}
basic = ['byte', 'short', 'int', 'long']
ss = []
ml = []
name = []
mml = []
nname = []
count = 0
for _ in range(N):
    ins = input().split()
    if ins[0] == '1':
        s = ins[1]
        k = int(ins[2])
        tl = []
        max = 1
        scount=0
        for i in range(k):
            t, n = input().split()
            if scount%dic[t]!=0:
                scount=(count//dic[t]+1)*dic[t]
            scount+=dic[t]
            if dic[t] > max:
                max = dic[t]

        dic[s] = max
        slen[s]=
    elif ins[0] == '2':
        t = ins[1]
        n = ins[2]
        if t in basic:
            if count % dic[t] != 0:
                count = (count//dic[t]+1)*dic[t]
            ml.append[count]
            name.append(n)
            mml.append[count]
            nname.append(n)
            count += dic[i]
        else:

    elif ins[0] == '3':
        s = ins[1]
        for i in range(len(mml)):
            if nname[i] == s:
                print()
    else:
        addr = int(ins[1])
        for i in range(len(ml)):
            if i != len(ml)-1:
                if addr >= ml[i] and addr <= ml[i+1]:
                    print(name[i])
                    break
            else:
                print(name[-1])
                break
