class File:
    def __init__(self):
        self.name = ''
        self.depth = 0
        self.nameset = set()
        self.dic = {}

    def __str__(self):
        output = ''
        if self.name:
            output += ' '*self.depth+self.name+'\n'
        for file in sorted(list(self.nameset)):
            output += str(self.dic.get(file))
        return output


def build(parent, idx, s):
    if s[idx] not in parent.nameset:
        new = File()
        new.name = s[idx]
        new.depth = idx
        parent.nameset.add(s[idx])
        parent.dic[s[idx]] = new
    if idx < len(s)-1:
        build(parent.dic[s[idx]], idx+1, s)


main = File()
for _ in range(int(input())):
    s = input().split('\\')
    build(main, 0, s)
print(str(main), end='')
