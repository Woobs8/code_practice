import argparse
import os
import timeit
from functools import partial
import random
from sorting import BaseSort

class HeapSort(BaseSort):
    """
    A class used to encapsulate the Heap Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the heap sort algorithm

    __max_heapify(arr)
        Builds a max heap from the input array using root_idx as the root element and tree depth determined by size n

    __parent_index
        Find parent index of index i for array representation of max heap

    __left_child_index
        Find left child index of index i for array representation of max heap

    __right_child_index
        Find right child index of index i for array representation of max heap

    """

    def __repr__(self):
        return "Heap Sort"

    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the heap sort algorithm

        Parameters:
            arr (list): list to be sorted
            in_place (bool): whether the list should be sorted in place

        Returns:
            list: the sorted list
        """ 
        n = len(arr)
        if in_place:
            work_arr = arr
        else:
            work_arr = arr.copy()

        # build the max heap structure from the data
        for i in range(n-1,-1,-1):
            self.__max_heapify(work_arr, n, i)

        # iteratively extract the root element (lartgest) and swap the last element in its place, the re-heapify the remaining array
        for i in range(n-1, 0, -1):
            work_arr[i], work_arr[0] = work_arr[0], work_arr[i]     # swap first and last elements
            self.__max_heapify(work_arr, i, 0)                      # re-heapify the array, but without including the extracted last element

        return work_arr
    
    def __max_heapify(self, arr: list, n: int, root_idx: int) -> list:
        """
        Builds a max heap from the input array using root_idx as the root element and tree depth determined by size n

        Parameters:
            arr (list): list to be sorted
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
    parser = argparse.ArgumentParser(description='Heap sorting algorithm')

    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int)
    parser.add_argument('-t', help='measure the execution time', nargs=2, required=False, type=int)
    args = parser.parse_args()
    
    n = args.data[0]
    seed = args.data[1]
    t = args.t

    # shuffle data randomly with seed
    sorted_data = list(range(n))
    random.seed(seed)
    random_data = random.sample(sorted_data, n)
    sorting_algo = HeapSort()

    # verify that list is sorted correctly
    if not sorting_algo.sort(random_data) == sorted_data:
        print('Error sorting array using <{}>'.format(sorting_algo))
        exit(1)

    # measure execution time
    if args.t:
        times = timeit.Timer(partial(sorting_algo.sort, random_data)).repeat(t[1], t[0])
        
        # average time taken
        time_taken = min(times) / t[0]

        print('Timing analysis')
        print('Sorting method: {}'.format(sorting_algo))
        print('Data length: {}'.format(n))
        print('Executions: {}'.format(t[0]))
        print('Average time: {}s'.format(time_taken))