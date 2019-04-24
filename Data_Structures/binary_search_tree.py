from __future__ import annotations
import argparse
import random

class TreeNode():
    """
    A class encapsulating a node in binary tree

    Attributes
    ----------
    data (int)
        The value of the node

    left (TreeNode)
        The left child node with a data value smaller than this node if it exists

    right (TreeNode)
        The right child node with a data value greater than this node if it exists

    Methods
    -------
    insert
        Inserts a node with specified value in the subtree that has node as root
    """
    def __init__(self, data: int):
        self.data = data    # value of node
        self.left = None    # left child
        self.right = None   # right child

    def __repr__(self):
        return '{}'.format(self.data)

    def insert(self, data: int) -> None:
        """
        Inserts a node with specified value in the subtree that has node as root

        Parameters:
            data (int): data value of node to be inserted

        Returns:
            -
        """ 
        # if node has value -> insert value as a child
        if self.data:
            # value is smaller than or equal to node value
            if data <= self.data:
                # no left child exists -> insert value as left child
                if self.left is None:
                    self.left = TreeNode(data)
                # left child exists -> recursively insert into left subtree
                else:
                    self.left.insert(data)
            # value is greater than node value
            else:
                # no right child exists -> insert value as right child
                if self.right is None:
                    self.right = TreeNode(data)
                # right child exists -> recursively insert into right subtree
                else:
                    self.right.insert(data)     
        # node has no value -> assign value to node
        else:
            self.data = data        


class BinarySearchTree():
    """
    A class encapsulating a binary search tree (BST) and related operations

    Attributes
    ----------
    root (TreeNode)
        The root node of the binary tree

    Methods
    -------
    __array_to_bst
        Converts a sorted array into a height-balanced BST

    insert
        Inserts value into BST

    get_height
        Determines height of current BST  

    __get_height
        Determines height of BST by recursively traversing the tree

    is_balanced
        Checks whether the current BST is balanced
    
    __is_balanced
        Checks whether the BST is balanced by recursively traversing the tree

    balance
        Balances the BST if it not current balanced

    __get_sorted_tree_nodes
        Recursively traverses the BST in-order and extracts a sorted array of the values of all nodes in the tree

    invert
        Inverts the BST
    
    __invert_tree
        Inverts the tree by recusively inverting the subtrees

    search
        Searches the BST for a needle using the specified traversal method

    __pre_prder_traversal
        Traverses a BST using pre-order traversal and search for a needle

    __post_prder_traversal
        Traverses a BST using post-order traversal and search for a needle

    __in_prder_traversal
        Traverses a BST using in-order traversal and search for a needle
    
    """
    def __init__(self, data: list):
        # initialize height-balanced tree from data
        self.root = self.__array_to_bst(sorted(data))
        self.n = len(data)

    def __repr__(self):
        return "BinarySearchTree"

    def __array_to_bst(self, data: list) -> TreeNode:
        """
        Converts a sorted array into a height-balanced BST

        Parameters:
            data (list): sorted data array

        Returns:
            TreeNode: root node of built BST
        """ 
        n = len(data)

        # no input data -> no tree
        if n == 0:
            return None
        # single input data element -> node with value
        elif n == 1:
            return TreeNode(data[0])
        # multiple data elements are recursively split by the median
        else:
            # root node is the median
            mid = n // 2
            root = TreeNode(data[mid])

            # left and right subtrees are built from left and right partition
            root.left = self.__array_to_bst(data[:mid])
            root.right = self.__array_to_bst(data[mid+1:])
            return root

    def insert(self, val: int) -> BinarySearchTree:
        """
        Inserts value into BST

        Parameters:
            val (int): value to insert

        Returns:
            BinarySearchTree: self for chained method invocation
        """
        self.root.insert(val)
        self.n += 1
        return self

    def get_height(self) -> int:
        """
        Determines height of current BST

        Parameters:
            - 
        
        Returns:
            int: height of BST
        """ 
        return self.__get_height(self.root)

    def __get_height(self, root) -> int:
        """
        Determines height of BST by recursively traversing the tree

        Parameters:
            root (TreeNode): root node of BST

        Returns:
            int: height of BST subtree with root as root node
        """ 
        # no root means subtree has no height
        if root is None:
            return 0
        # root exists means height is one plus highest of the two subtrees
        else:
            return 1 + max(self.__get_height(root.left), self.__get_height(root.right))

    def is_balanced(self) -> bool:
        """
        Checks whether the current BST is balanced

        Parameters:
            -

        Returns:
            bool: whether the BST is balanced
        """ 
        return self.__is_balanced(self.root)
    
    def __is_balanced(self, root: TreeNode) -> bool:
        """
        Checks whether the BST is balanced by recursively traversing the tree

        Parameters:
            root (TreeNode): root node of BST

        Returns:
            bool: Whether the BST subtree with root as root node is balanced
        """
        # a non-exisitng subtree is per definition sorted
        if root is None:
            return True
        # root exists
        else:
            # is the left subtree balanced?
            left_balance = self.__is_balanced(root.left)

            # is the right subtree balanced?
            right_balance = self.__is_balanced(root.right)

            # height difference between the left and right subtrees
            height_diff = abs(self.__get_height(root.left)-self.__get_height(root.right))

            # a balanced subtree must have balanced subtrees and a maximum height difference of 1 between the left and right subtrees
            return left_balance and right_balance and height_diff <= 1

    def balance(self) -> BinarySearchTree:
        """
        Balances the BST if it not current balanced

        Parameters:
            -
        
        Returns:
            BinarySearchTree: self for chained method invocation
        """ 
        # BST is not already balanced
        if not self.is_balanced():
            sorted_nodes = []
            # extract sorted nodes by in-order traversal
            self.__get_sorted_tree_nodes(self.root, sorted_nodes)

            # rebuild BST from sorted array
            self.root = self.__array_to_bst(sorted_nodes)
        return self

    def __get_sorted_tree_nodes(self, root: TreeNode, sorted_nodes: list) -> None:
        """
        Recursively traverses the BST in-order and extracts a sorted array of the values of all nodes in the tree

        Parameters:
            root (TreeNode): root node of BST
            sorted_nodes (list): sorted list of node values

        Returns:
            None
        """
        # if root exists, in-order traverse the BST to extracted sorted nodes
        if root is not None:
            self.__get_sorted_tree_nodes(root.left, sorted_nodes)
            sorted_nodes.append(root.data)
            self.__get_sorted_tree_nodes(root.right, sorted_nodes)

    def invert(self) -> BinarySearchTree:
        """
        Inverts the BST

        Parameters:
            -
        
        Returns:
            BinarySearchTree: self for chained method invocation
        """ 
        self.__invert_tree(self.root)
        return self
    
    def __invert_tree(self, root: TreeNode) -> TreeNode:
        """
        Inverts the tree by recusively inverting the subtrees

        Parameters:
            root (TreeNode): root node of BST

        Returns:
            TreeNode: the root node of the inverted BST
        """
        if root is None:
            return None
        else:
            # recursively invert left subtree
            left = self.__invert_tree(root.left)

            # recursively invert right subtree
            right = self.__invert_tree(root.right)

            # invert children
            root.left = right
            root.right = left
            return root

    def search(self, needle: int, traversal: str ='pre') -> str:
        """
        Searches the BST for a needle using the specified traversal method

        Parameters:
            needle (int): value to search for
            traversal (str): the traversal type (pre, post, in)

        Returns:
            str: status of the search
        """
        # search the BST using pre-order traversal
        if traversal == 'pre':
            return self.__pre_prder_traversal(self.root, needle)
        # search the BST using post-order traversal
        elif traversal == 'post':
            return self.__post_prder_traversal(self.root, needle)
        # search the BST using in-order traversal
        elif traversal == 'in':
            return self.__in_prder_traversal(self.root, needle)
        # unknown traversal method
        else:
            return 'Unsupported traversal method: {}'.format(traversal)

    def __pre_prder_traversal(self, root: TreeNode, needle: int) -> str:
        """
        Traverses a BST using pre-order traversal and search for a needle

        Parameters:
            root (TreeNode): root node of the BST to search
            needle (int): value to search for

        Returns:
            str: status of the search
        """
        # pre-order: root->left->right
        if needle == root.data:
            return '{} was found'.format(needle)
        elif needle < root.data:
            # no left -> value doesn't exist in BST
            if root.left is None:
                return '{} was not found'.format(needle)
            # left child exists -> search left subtree
            else:
                return self.__pre_prder_traversal(root.left, needle)
        else:
            # no right -> value doesn't exist in BST
            if root.right is None:
                return '{} was not found'.format(needle)
            # right child exists -> search right subtree
            else:
                return self.__pre_prder_traversal(root.right, needle)

    def __post_prder_traversal(self, root: TreeNode, needle: int) -> str:
        """
        Traverses a BST using post-order traversal and search for a needle

        Parameters:
            root (TreeNode): root node of the BST to search
            needle (int): value to search for

        Returns:
            str: status of the search
        """
        # post-order: left->right->root
        if needle < root.data:
            # no left -> value doesn't exist in BST
            if root.left is None:
                return '{} was not found'.format(needle)
            # left child exists -> search left subtree
            else:
                return self.__post_prder_traversal(root.left, needle)
        elif needle > root.data:
            # no right -> value doesn't exist in BST
            if root.right is None:
                return '{} was not found'.format(needle)
            # right child exists -> search right subtree
            else:
                return self.__post_prder_traversal(root.right, needle)
        else:
            return '{} was found'.format(needle)

    def __in_prder_traversal(self, root: TreeNode, needle: int) -> str:
        """
        Traverses a BST using in-order traversal and search for a needle

        Parameters:
            root (TreeNode): root node of the BST to search
            needle (int): value to search for

        Returns:
            str: status of the search
        """
        # in-order: left->root->right
        if needle < root.data:
            # no left -> value doesn't exist in BST
            if root.left is None:
                return '{} was not found'.format(needle)
            # left child exists -> search left subtree
            else:
                return self.__in_prder_traversal(root.left, needle)
        elif needle == root.data:
            return '{} was found'.format(needle)
        else:
            # no right -> value doesn't exist in BST
            if root.right is None:
                return '{} was not found'.format(needle)
            # right child exists -> search right subtree
            else:
                return self.__in_prder_traversal(root.right, needle)

    def print_tree(self) -> None:
        print_list = []
        self.__print_tree(self.root, print_list)
        print(print_list)

    def __print_tree(self, root, print_list):
        if root.left:
            self.__print_tree(root.left, print_list)
        print_list.append(root.data)
        if root.right:
            self.__print_tree(root.right, print_list)    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of a binary search tree and relation operations')
    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int)
    args = parser.parse_args()    
    n = args.data[0]
    seed = args.data[1]

    # shuffle data randomly with seed
    sorted_data = list(range(n))
    random.seed(seed)
    random_data = random.sample(sorted_data, n)
    
    # init tree
    tree = BinarySearchTree(random_data)

    # verify that the tree is balanced
    print('The tree is balanced: {}'.format(tree.is_balanced()))

    # insert arbitrary values
    tree.insert(609)
    tree.insert(802)
    tree.insert(53)
    tree.insert(72)

    # verify that tree is unbalanced
    print('The tree is balanced: {}'.format(tree.is_balanced()))

    # balance the tree
    tree.balance()

    # verify that the tree is balanced
    print('The tree is balanced: {}'.format(tree.is_balanced()))

    # search for arbitrary value that exists in the tree    
    print(tree.search(42, 'in'))

    # search for arbitrary value that does not exist in the tree    
    print(tree.search(55, 'in'))

    # print the tree
    tree.print_tree()

    # invert tree
    tree.invert()

    # print inverted tree
    tree.print_tree()