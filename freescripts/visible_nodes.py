import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

visibleNodeCount = 0

def preOrder(node, mx):
    if (node == None):
        return
    global visibleNodeCount
    if node.data >= mx:
        visibleNodeCount = visibleNodeCount + 1
        mx = node.data
    preOrder(node.left, mx)
    preOrder(node.right, mx)

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(21)
    root.right.left = Node(1)
    preOrder(root, -sys.maxsize-1)
    print(visibleNodeCount)