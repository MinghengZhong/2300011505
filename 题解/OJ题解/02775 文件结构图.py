class File:
    def __init__(self):
        self.name = 'ROOT'
        self.files = []
        self.dirs = []

    def __str__(self):
        return '\n'.join([self.name]+['|     '+s for d in self.dirs for s in str(d).split('\n')]+sorted(self.files))

    def build(self, parent, s):
        if s[0] == 'f':
            parent.files.append(s)
        else:
            dir = File()
            dir.name = s
            parent.dirs.append(dir)
            while True:
                s = input()
                if s == ']':
                    break
                dir.build(dir, s)


x = 0
while True:
    s = input()
    if s == '#':
        break
    x += 1
    root = File()
    while s != '*':
        root.build(root, s)
        s = input()
    print('DATA SET %d:' % x)
    print(root, end='\n\n')
