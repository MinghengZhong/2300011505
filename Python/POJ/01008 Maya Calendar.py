n = int(input())
print(n)
for i in range(0, n):
    day1, month1, year1 = input().split(' ')
    l1 = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
          'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
    l2 = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
          'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
    count = int(float(day1))+20*l1.index(month1)+365*int(year1)
    print(str(count % 13+1)+' '+l2[count % 20]+' '+str(int(count/260)))
