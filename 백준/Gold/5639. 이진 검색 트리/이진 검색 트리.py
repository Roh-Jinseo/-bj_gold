import sys;sys.setrecursionlimit(2*10**5)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if child.value < self.value : #left
            if not self.left:
                self.left = child
                return
            self.left.insert(child)
        else: # right
            if not self.right:
                self.right = child
                return
            self.right.insert(child)
        return

    def post(self):
        if self.left:
            self.left.post()

        if self.right:
            self.right.post()

        print(self.value)

root = None
while True:
    try:
        if root is None:
            root = TreeNode(int(sys.stdin.readline()))
        else:            root.insert(TreeNode(int(sys.stdin.readline())))
    except:        break

if root:    root.post()
