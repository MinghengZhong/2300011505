class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Heap:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Tree(val)
        else:
            self._add(self.root, val)

    def _add(self, node, val):
        if not node:
            return Tree(val)
        if val < node.val:
            node.left = self._add(node.left, val)
        else:
            node.right = self._add(node.right, val)
        return node

    def pop(self):
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        self.root = self._pop(self.root)
        return node.val

    def _pop(self, node):
        if not node.left:
            return node.right
        node.left = self._pop(node.left)
        return node


heap = Heap()
for _ in range(int(input())):
    s = input()
    if len(s)-1:
        heap.add(int(s.split()[1]))
    else:
        print(heap.pop())


'''
import heapq as H

l = []
for _ in range(int(input())):
    s = input()
    if len(s)-1:
        H.heappush(l, int(s.split()[1]))
    else:
        print(H.heappop(l))
'''
