"""
  Find the least common ancestor between two nodes on a binary search tree.
  The least common ancestor is the farthest node from the root that is an ancestor
  of both nodes. For example, the root is a common ancestor of all nodes on the
  tree, but if both nodes are descendents of the root's left child, then that left
  child might be the lowest common ancestor. You can assume that both nodes are in
  the tree, and the tree itself adheres to all BST properties. The function
  definition should look like question4(T, r, n1, n2), where Tis the tree
  represented as a matrix, where the index of the list is equal to the integer
  stored in that node and a 1 represents a child node, r is a non-negative integer
  representing the root, and n1 and n2 are non-negative integers representing the
  two nodes in no particular order. For example, one test case might be ...
  question4([[0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0]],
            3,
            1,
            4)
"""

# helper function to find parent
def parent(tree, node):
    rows = len(tree)
    for i in xrange(rows):
        if tree[i][node] == 1:
            return i
    return -1

def question4(tree, root, node_1, node_2):
    if tree:
      node_1_paths = []
      while node_1 != root:
          node_1 = parent(tree, node_1)
          node_1_paths.append(node_1)
      if len(node_1_paths) == 0:
          return -1
      while node_2 != root:
          node_2 = parent(tree, node_2)
          if node_2 in node_1_paths:
              return node_2
    return -1

print question4([
                  [0,1,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [1,0,0,0,1],
                  [0,0,0,0,0]
                ],
                3,
                1,
                4)
# returns 3

print question4(None, 3, 1, 4)
# returns -1




