import argparse
import random


class BinaryHeap():
    """
    A class encapsulating a binary heap data structure

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
    def __init__(self, data: list, heap_type: str='max'):
        self.heap = data.copy()
        self.heap_type = heap_type
        self.__heapify()


    def __repr__(self):
        return str(self.heap)


    def __heapify(self):
        """
        Builds a min or max heap data structure from the heap attribute

        Parameters:
            -

        Returns:
            None
        """
        n = len(self.heap)
        for i in range(n-1,-1,-1):
            if self.heap_type == 'max':
                self.__max_heapify(self.heap, n, i)
            elif self.heap_type == 'min':
                self.__min_heapify(self.heap, n, i)


    def __max_heapify(self, arr: list, n: int, root_idx: int) -> list:
        """
        Builds a max heap from the input array using root_idx as the root element and tree depth determined by size n

        Parameters:
            arr (list): list of data elements
            n (int): length of array to build heap from
            root_idx: index of the root element in the array

        Returns:
            list: array representation of max heap
        """
        max_idx = root_idx                          # max value is initialized as the root
        l = self.__left_child_index(root_idx)       # left child index of root
        r = self.__right_child_index(root_idx)      # right child index of root

        # if left child exists and is greater than root, change current max value
        if l < n and arr[l] > arr[max_idx]:
            max_idx = l
        
        # if right child exists and is greater than current max value, change current max value
        if r < n and arr[r] > arr[max_idx]:
            max_idx = r

        # if the max value changed, then it is swapped with the root
        if max_idx != root_idx:
            arr[max_idx], arr[root_idx] = arr[root_idx], arr[max_idx]

            # since root is swapped, its new subtree must be heapified
            self.__max_heapify(arr, n, max_idx)


    def __min_heapify(self, arr: list, n: int, root_idx: int) -> list:
        """
        Builds a max heap from the input array using root_idx as the root element and tree depth determined by size n

        Parameters:
            arr (list): list of data elements
            n (int): length of array to build heap from
            root_idx: index of the root element in the array

        Returns:
            list: array representation of max heap
        """
        min_idx = root_idx                          # min value is initialized as the root
        l = self.__left_child_index(root_idx)       # left child index of root
        r = self.__right_child_index(root_idx)      # right child index of root

        # if left child exists and is greater than root, change current max value
        if l < n and arr[l] < arr[min_idx]:
            min_idx = l
        
        # if right child exists and is greater than current max value, change current max value
        if r < n and arr[r] < arr[min_idx]:
            min_idx = r

        # if the max value changed, then it is swapped with the root
        if min_idx != root_idx:
            arr[min_idx], arr[root_idx] = arr[root_idx], arr[min_idx]

            # since root is swapped, its new subtree must be heapified
            self.__max_heapify(arr, n, min_idx)


    def insert(self, data: int) -> None:
        """
        Inserts an element into the heap

        Parameters:
            data (int): data to insert into heap

        Returns:
            None
        """
        self.heap.append(data)
        self.__heapify()


    def remove(self, key: int) -> None:
        """
        Removes an element from the heap

        Parameters:
            key (int): index at which to remove element

        Returns:
            None
        """
        if key <= (len(self.heap)-1):
            self.heap = self.heap[:key] + self.heap[key+1:]
            self.__heapify()
        else:
            raise IndexError


    def __len__(self):
        return len(self.heap)


    def __parent_index(self, i: int) -> int:
        """
        Find parent index of index i for array representation of max heap

        Parameters:
            i (int): index of element in array representation of heap

        Returns:
            int: parent index of i
        """
        return (i-1)//2
    

    def __left_child_index(self, i: int) -> int:
        """
        Find left child index of index i for array representation of max heap

        Parameters:
            i (int): index of element in array representation of heap

        Returns:
            int: left child index of i
        """
        return (2*i)+1
    

    def __right_child_index(self, i: int) -> int:
        """
        Find right child index of index i for array representation of max heap

        Parameters:
            i (int): index of element in array representation of heap

        Returns:
            int: right child index of i
        """
        return (2*i)+2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of binary heap data structure')
    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int)
    parser.add_argument('-type', help='type of queue [std, de]', choices=['max','min'], default='max')
    args = parser.parse_args()    
    n = args.data[0]
    seed = args.data[1]
    heap_type = args.type

    # shuffle data randomly with seed
    sorted_data = list(range(n))
    random.seed(seed)
    random_data = random.sample(sorted_data, n)
    
    # init tree
    heap = BinaryHeap(random_data, args.type)

    # print initial heap
    print('Initial heap')
    print(heap)
    print('Heap length: {}'.format(len(heap)))
    print('-------------------')

    # insert element
    x = 1
    print('Insert {}'.format(x))
    heap.insert(x)
    print(heap)
    print('Heap length: {}'.format(len(heap)))
    print('-------------------')

    x = 50
    print('Insert {}'.format(x))
    heap.insert(x)
    print(heap)
    print('Heap length: {}'.format(len(heap)))
    print('-------------------')

    # remove element
    i = 25
    print('Remove index {}'.format(i))
    heap.remove(i)
    print(heap)
    print('Heap length: {}'.format(len(heap)))
    print('-------------------')