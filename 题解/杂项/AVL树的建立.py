class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)
        if balance > 1 and val < node.left.val:
            return self.rotate_right(node)
        if balance < -1 and val > node.right.val:
            return self.rotate_left(node)
        if balance > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and val < node.right.val:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def pre(self, node, result):
        if node:
            result.append(node.val)
            self.pre(node.left, result)
            self.pre(node.right, result)


n = int(input())
tree = Tree()
for a in list(map(int, input().split())):
    tree.root = tree.insert(tree.root, a)
result = []
tree.pre(tree.root, result)
print(' '.join(map(str, result)))
