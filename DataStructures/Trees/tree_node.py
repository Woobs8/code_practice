from __future__ import annotations

class BinaryTreeNode():
    """
    A class encapsulating a node in a binary tree

    Attributes
    ----------
    data (int)
        The value of the node

    left (TreeNode)
        The left child node with a data value smaller than this node if it exists

    right (TreeNode)
        The right child node with a data value greater than this node if it exists


    """
    def __init__(self, data: int):
        self.data = data    # value of node
        self.left = None    # left child
        self.right = None   # right child
        self.height = 1


    def __repr__(self):
        return '{}'.format(self.data)