from __future__ import annotations
import argparse
import random
from tree_node import BinaryTreeNode


class BinarySearchTree():
    """
    A class encapsulating a binary search tree (BST) and related operations

    Attributes
    ----------
    root (BinaryTreeNode)
        The root node of the binary tree

    Methods
    -------
    __array_to_bst
        Converts a sorted array into a height-balanced BST

    insert
        Inserts value into BST

    __insert
        Inserts value into BST by recursively traversing the tree

    delete
        Delete value from BST

    __delete
        Delete value from BST by recursively traversing the tree

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

    __get_max_value
        Traverses a BST and returns the maximum value in the subtree

    __get_min_value
        Traverses a BST and returns the minimum value in the subtree   
    """
    def __init__(self, data: list = None):
        # initialize height-balanced tree from data
        if data:
            self.root = self.__array_to_bst(sorted(data))
            self.n = len(data)
        else:
            self.root = None
            self.n = 0


    def __repr__(self):
        return "BinarySearchTree"


    def __array_to_bst(self, data: list) -> BinaryTreeNode:
        """
        Converts a sorted array into a height-balanced BST

        Parameters:
            data (list): sorted data array

        Returns:
            BinaryTreeNode: root node of built BST
        """
        # length of data in current recursion
        n = len(data)

        # no input data -> no tree
        if n == 0:
            return None
        # single input data element -> node with value
        elif n == 1:
            return BinaryTreeNode(data[0])
        # multiple data elements are recursively split by the median
        else:
            # root node is the median
            mid = n // 2
            root = BinaryTreeNode(data[mid])

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
        self.root = self.__insert(self.root, val)
        self.n += 1
        return self

    
    def __insert(self, root: BinaryTreeNode, val: int) -> BinaryTreeNode:
        """
        Inserts value into BST by recursively traversing the tree

        Parameters:
            root (BinaryTreeNode): root node of subtree
            val (int): value to insert

        Returns:
            BinaryTreeNode: root of node of subtree
        """
        # if no root exists, the new node is the root
        if root is None:
            return BinaryTreeNode(val)

        # if value to insert is smaller than root, traverse down left subtree
        if val < root.data:
            root.left = self.__insert(root.left, val)
        # otherwise, traverse down right subtree
        else:
            root.right = self.__insert(root.right, val)

        return root

    
    def delete(self, key: int) -> BinarySearchTree:
        """
        Delete value from BST

        Parameters:
            key (int): value to delete

        Returns:
            BinarySearchTree: self for chained method invocation
        """
        self.root = self.__delete(self.root, key)
        self.n -= 1
        return self

    
    def __delete(self, root: BinaryTreeNode, key: int) -> BinaryTreeNode:
        """
        Delete value from BST by recursively traversing the tree

        Parameters:
            root (BinaryTreeNode): root node of subtree
            val (int): key to delete

        Returns:
            BinaryTreeNode: root of node of subtree
        """
        # if root does not exist, there is no more to traverse
        if root is None: 
            return root  
    
        # if key is smaller than root, the key must be in the left subtree
        if key < root.data: 
            root.left = self.__delete(root.left, key) 
        # if key is greater than root, the key must be in the right subtree
        elif key > root.data: 
            root.right = self.__delete(root.right, key)
    
        # else the key is equal to the root, and the root must be deleted
        else:   
            # if root has no children it is deleted; if root has only one child it becomes the new root
            if root.left is None: 
                child_node = root.right  
                root = None 
                return child_node 
            elif root.right is None: 
                child_node = root.left  
                root = None
                return child_node 

            # if node has two children, the inorder succesor is chosen as new root
            # inorder-succesor is the smallest in the right subtree
            temp = self.__get_min_value(root.right)
    
            # the value of the new root is copied to the current root 
            root.key = temp.key 
    
            # the inorder succesor is then deleted 
            root.right = self.__delete(root.right, temp.key) 
    
        return root


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
            root (BinaryTreeNode): root node of BST

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


    def __is_balanced(self, root: BinaryTreeNode) -> bool:
        """
        Checks whether the BST is balanced by recursively traversing the tree

        Parameters:
            root (BinaryTreeNode): root node of BST

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
        Balances the BST if it is not current balanced

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


    def __get_sorted_tree_nodes(self, root: BinaryTreeNode, sorted_nodes: list) -> None:
        """
        Recursively traverses the BST in-order and extracts a sorted array of the values of all nodes in the tree

        Parameters:
            root (BinaryTreeNode): root node of BST
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


    def __invert_tree(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Inverts the tree by recusively inverting the subtrees

        Parameters:
            root (BinaryTreeNode): root node of BST

        Returns:
            BinaryTreeNode: the root node of the inverted BST
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


    def __pre_prder_traversal(self, root: BinaryTreeNode, needle: int) -> str:
        """
        Traverses a BST using pre-order traversal and search for a needle

        Parameters:
            root (BinaryTreeNode): root node of the BST to search
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


    def __post_prder_traversal(self, root: BinaryTreeNode, needle: int) -> str:
        """
        Traverses a BST using post-order traversal and search for a needle

        Parameters:
            root (BinaryTreeNode): root node of the BST to search
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


    def __in_prder_traversal(self, root: BinaryTreeNode, needle: int) -> str:
        """
        Traverses a BST using in-order traversal and search for a needle

        Parameters:
            root (BinaryTreeNode): root node of the BST to search
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
    

    def __get_max_value(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Traverses a BST and returns the maximum value in the subtree

        Parameters:
            root (BinaryTreeNode): root node of the subtree to search

        Returns:
            BinaryTreeNode: root node of subtree
        """
        current = root

        while(current.right is not None):
            current = current.right

        return current


    def __get_min_value(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Traverses a BST and returns the mninimum value in the subtree

        Parameters:
            root (BinaryTreeNode): root node of the subtree to search

        Returns:
            BinaryTreeNode: root node of subtree
        """
        current = root

        while(current.left is not None):
            current = current.left

        return current


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
    parser = argparse.ArgumentParser(description='Implementation of a binary search tree and related operations')
    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int, required=True)
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

    # delete value that exist in the tree, and verify that is has been deleted
    tree.delete(42)
    print(tree.search(42, 'in'))
    tree.print_tree()

    # invert tree
    tree.invert()

    # print inverted tree
    tree.print_tree()