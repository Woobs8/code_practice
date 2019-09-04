from __future__ import annotations
import argparse
import random
from tree_node import BinaryTreeNode


class AVLTree():
    """
    A class encapsulating a binary search tree (BST) and related operations

    Attributes
    ----------
    root (BSTNode)
        The root node of the binary tree

    Methods
    -------
    insert
        Inserts value into tree

    __insert
        Inserts a node into the AVL tree recursively while ensuring the tree remains balanced

    delete
        Deletes value from tree

    __delete
        Delete value from BST by recursively traversing the tree.

    left_rotate
        Left-rotate subtree around pivot z

    right_rotate
        Right-rotate subtree around pivot z

    get_height
        Determines height of current tree  

    __get_height
        Determines height of tree by recursively traversing the tree

    get_height_diff
        Returns height difference between left and right subtrees of node

    is_balanced
        Checks whether the current tree is balanced
    
    __is_balanced
        Checks whether the tree is balanced by recursively traversing the tree

    __get_sorted_tree_nodes
        Recursively traverses the tree in-order and extracts a sorted array of the values of all nodes in the tree

    invert
        Inverts the tree
    
    __invert_tree
        Inverts the tree by recusively inverting the subtrees

    search
        Searches the tree for a needle using the specified traversal method

    __pre_prder_traversal
        Traverses a tree using pre-order traversal and search for a needle

    __post_prder_traversal
        Traverses a tree using post-order traversal and search for a needle

    __in_prder_traversal
        Traverses a tree using in-order traversal and search for a needle

    __get_max_value
        Traverses a BST and returns the maximum value in the subtree

    __get_min_value
        Traverses a BST and returns the minimum value in the subtree
    """
    def __init__(self, data: list = None):
        # initialize height-balanced tree from data
        self.n = len(data)
        if data:
            self.root = BinaryTreeNode(data[0])
            for i in range(1,n):
                self.root = self.__insert(self.root, data[i])
        else:
            self.root = None


    def __repr__(self):
        return "AVLTree"


    def insert(self, val: int) -> AVLTree:
        """
        Inserts value into tree

        Parameters:
            val (int): value to insert

        Returns:
            AVLTree: self for chained method invocation
        """
        if self.root is None:
            self.root = BinaryTreeNode(val)
        else:
            self.root = self.__insert(self.root, val)
        
        self.n += 1
        return self


    def __insert(self, root: BinaryTreeNode, data: int):
        """
        Inserts a node into the AVL tree while ensuring the tree remains balanced.

        The tree is balanced by traveling up the tree from a newly inserted node until
        an unbalance node (z) is encountered. The subtree of the unbalanced node is then balanced
        by doing one of four possible operations that rotate the node and its child nodes.
        Selecting the right operation is a matter of finding the height difference between
        the two subtrees to determine whether they are balanced, and comparing the values of 
        the last two children (x and y) along the traveled path to determine whether they are 
        left-left, left-right, right-right or right-left children.

        Parameters:
            root (BinaryTreeNode): root node of subtree
            data (int): data value of node to be inserted
        """ 
        # insert new node into tree as in a traditional BST
        if not root: 
            return BinaryTreeNode(data) 
        elif data < root.data: 
            root.left = self.__insert(root.left, data) 
        else: 
            root.right = self.__insert(root.right, data)

        # update height attribute of parent node
        root.height = 1 + max(self.__get_height(root.left), self.__get_height(root.right))

       # get 'balance factor' (height difference between left and right subtrees)
        balance = self.get_height_diff(root)
        
        # balance subtree if unbalanced
        # Case 1: left-left rotation
        # z is the unbalance node, y is the first child, and x is the grandchild
        #                      -    z    -
        #                     |           |
        #                 -   y   -       T4
        #                |         |
        #              - x -       T3
        #             |     |
        #             T1    T2  
        # balance factor is greater than 1, while x and y are both left children
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Case 2: left-right rotation
        # z is the unbalance node, y is the first child, and x is the grandchild
        #                      -    z    -
        #                     |           |
        #                 -   y   -       T4
        #                |         |
        #                T1      - x -       
        #                       |     |
        #                       T1    T2  
        # balance factor is greater than 1, while y is a left child and x is a right child
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 3: right-right rotation
        # z is the unbalance node, y is the first child, and x is the grandchild
        #                      -    z    -
        #                     |           |
        #                     T1      -   y   -       
        #                            |         |
        #                            T2      - x -       
        #                                   |     |
        #                                   T3    T4  
        # balance factor is greater than 1, while x and y are both right children
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Case 4: right-left rotation
        # z is the unbalance node, y is the first child, and x is the grandchild
        #                      -    z    -
        #                     |           |
        #                     T1      -   y   -       
        #                            |         |
        #                          - x -       T4
        #                         |     |
        #                         T2    T3
        # balance factor is smaller than 1, while y is a right child and x is a left child
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def delete(self, key: int) -> AVLTree:
        """
        Deletes value from tree

        Parameters:
            key (int): value to delete

        Returns:
            AVLTree: self for chained method invocation
        """
        self.root = self.__delete(self.root, key)
        self.n -= 1
        return self


    def __delete(self, root: BinaryTreeNode, key: int) -> BinaryTreeNode:
        """
        Delete value from BST by recursively traversing the tree.

        The tree is balanced by traveling up the tree from a newly inserted node until
        an unbalance node (z) is encountered. The subtree of the unbalanced node is then balanced
        by doing one of four possible operations that rotate the node and its child nodes.
        Selecting the right operation is a matter of finding the height difference between
        the two subtrees to determine whether they are balanced, and finding the two tallest children
        of z (meaning the children that have highest subtress themselves) to determine whether 
        they are left-left, left-right, right-right or right-left children.

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
            root.data = temp.data 
    
            # the inorder succesor is then deleted 
            root.right = self.__delete(root.right, temp.data)

        # update height attribute of parent node
        root.height = 1 + max(self.__get_height(root.left), self.__get_height(root.right))

       # get 'balance factor' (height difference between left and right subtrees)
        balance = self.get_height_diff(root)
        
        # balance subtree if unbalanced
        # Case 1: left-left rotation
        # z is the unbalance node, y is the taller child of z, x is the taller child of y
        #                      -    z    -
        #                     |           |
        #                 -   y   -       T4
        #                |         |
        #              - x -       T3
        #             |     |
        #             T1    T2  
        # balance factor is greater than 1, while x and y are both left children
        if balance > 1 and self.get_height_diff(root.left) >= 0:
            return self.right_rotate(root)

        # Case 2: left-right rotation
        # z is the unbalance node, y is the taller child of z, x is the taller child of y
        #                      -    z    -
        #                     |           |
        #                 -   y   -       T4
        #                |         |
        #                T1      - x -       
        #                       |     |
        #                       T1    T2  
        # balance factor is greater than 1, while y is a left child and x is a right child
        if balance > 1 and self.get_height_diff(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 3: right-right rotation
        # z is the unbalance node, y is the taller child of z, x is the taller child of y
        #                      -    z    -
        #                     |           |
        #                     T1      -   y   -       
        #                            |         |
        #                            T2      - x -       
        #                                   |     |
        #                                   T3    T4  
        # balance factor is smaller than 1, while x and y are both right children
        if balance < -1 and self.get_height_diff(root.right) <= 0:
            return self.left_rotate(root)

        # Case 4: right-left rotation
        # z is the unbalance node, y is the taller child of z, x is the taller child of y
        #                      -    z    -
        #                     |           |
        #                     T1      -   y   -       
        #                            |         |
        #                          - x -       T4
        #                         |     |
        #                         T2    T3
        # balance factor is smaller than 1, while y is a right child and x is a left child
        if balance < -1 and self.get_height_diff(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def left_rotate(self, z: BinaryTreeNode) -> BinaryTreeNode: 
        """
        Left-rotate subtree around pivot z

        Parameters:
            z (BinaryTreeNode): root node of subtree to pivot rotation on

        Returns:
            BinaryTreeNode: root of left-rotated subtree
        """
        # get references to child nodes of pivot
        y = z.right     # right child of pivot
        T2 = y.left     # left child of y
  
        # rotate nodes around pivot
        y.left = z      # y becomes new root of subtree, and pivot becomes child of y
        z.right = T2    # T2 becomes right node of pivot
  
        # update height of rotated nodes
        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right)) 
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right)) 
  
        # return the new root 
        return y
  

    def right_rotate(self, z): 
        """
        Right-rotate subtree around pivot z

        Parameters:
            z (BinaryTreeNode): root node of subtree to pivot rotation on

        Returns:
            BinaryTreeNode: root of right-rotated subtree
        """
        # get references to child nodes of pivot
        y = z.left      # left child of pivot
        T3 = y.right    # right child of y
  
        # rotate nodes around pivot 
        y.right = z     # y becomes new root of subtree, and pivot becomes child of y
        z.left = T3     # T3 becomes left node of pivot
  
        # update height of rotated nodes
        z.height = 1 + max(self.__get_height(z.left), self.__get_height(z.right)) 
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right)) 
  
        # return the new root 
        return y 


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
            root (BSTNode): root node of BST

        Returns:
            int: height of BST subtree with root as root node
        """ 
        # no root means subtree has no height
        if root is None:
            return 0
        # root exists means root height is subtree height
        else:
            return root.height


    def get_height_diff(self, root: BinaryTreeNode) -> int:
        """
        Returns height difference between left and right subtrees of node

        Parameters:
            root (BSTNode): root node of subtree

        Returns:
            int: height difference between subtrees
        """    
        if root is None:
            return 0
        else:
            return self.__get_height(root.left) - self.__get_height(root.right)


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
            root (BSTNode): root node of BST

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
            height_diff = abs(self.get_height_diff(root))

            # a balanced subtree must have balanced subtrees and a maximum height difference of 1 between the left and right subtrees
            return left_balance and right_balance and height_diff <= 1


    def __get_sorted_tree_nodes(self, root: BinaryTreeNode, sorted_nodes: list) -> None:
        """
        Recursively traverses the BST in-order and extracts a sorted array of the values of all nodes in the tree

        Parameters:
            root (BSTNode): root node of BST
            sorted_nodes (list): sorted list of node values

        Returns:
            None
        """
        # if root exists, in-order traverse the BST to extracted sorted nodes
        if root is not None:
            self.__get_sorted_tree_nodes(root.left, sorted_nodes)
            sorted_nodes.append(root.data)
            self.__get_sorted_tree_nodes(root.right, sorted_nodes)


    def invert(self) -> AVLTree:
        """
        Inverts the BST

        Parameters:
            -
        
        Returns:
            AVLTree: self for chained method invocation
        """ 
        self.__invert_tree(self.root)
        return self


    def __invert_tree(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Inverts the tree by recusively inverting the subtrees

        Parameters:
            root (BSTNode): root node of BST

        Returns:
            BSTNode: the root node of the inverted BST
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
            root (BSTNode): root node of the BST to search
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
            root (BSTNode): root node of the BST to search
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
            root (BSTNode): root node of the BST to search
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
        print('tree: {}'.format(print_list))
        print('tree size: {}'.format(len(print_list)))


    def __print_tree(self, root, print_list):
        if root.left:
            self.__print_tree(root.left, print_list)
        print_list.append(root.data)
        if root.right:
            self.__print_tree(root.right, print_list)    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of an AVL tree and related operations')
    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int, required=True)
    args = parser.parse_args()    
    n = args.data[0]
    seed = args.data[1]

    # shuffle data randomly with seed
    sorted_data = list(range(n))
    random.seed(seed)
    random_data = random.sample(sorted_data, n)
    
    # init tree
    tree = AVLTree(random_data)
    tree.print_tree()

    # insert arbitrary values and verify that the tree is always balanced
    tree.insert(609)
    tree.print_tree()
    print('The tree is balanced: {}'.format(tree.is_balanced()))
    tree.insert(802)
    tree.print_tree()
    print('The tree is balanced: {}'.format(tree.is_balanced()))
    tree.insert(53)
    tree.print_tree()
    print('The tree is balanced: {}'.format(tree.is_balanced()))
    tree.insert(72)
    tree.print_tree()
    print('The tree is balanced: {}'.format(tree.is_balanced()))

    # search for arbitrary value that exists in the tree    
    print(tree.search(42, 'in'))

    # search for arbitrary value that does not exist in the tree    
    print(tree.search(55, 'in'))

    # delete value that exist in the tree, and verify that is has been deleted
    tree.delete(42)
    print(tree.search(42, 'in'))
    tree.print_tree()
    print('The tree is balanced: {}'.format(tree.is_balanced()))

    # invert tree
    tree.invert()

    # print inverted tree
    tree.print_tree()