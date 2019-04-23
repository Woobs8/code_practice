import argparse
import os
import timeit
from functools import partial
import random
from sorting import BaseSort

class MergeSort(BaseSort):
    """
    A class used to encapsulate the Merge Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the merge sort algorithm

    __recursive_sort(arr)
        Recursively splits the array into smaller segments until each segment is a single element, which are then
        merged while sorting the merging elements until the entire array is merged and sorted

    __merge(a,b)
        Merges two lists while sorting the elements in the lists
    """

    def __repr__(self):
        return "Merge Sort"

    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the merge sort algorithm

        Parameters:
            arr (list): list to be sorted
            in_place (bool): whether the list should be sorted in place

        Returns:
            list: the sorted list
        """ 
        if in_place:
            work_arr = arr
        else:
            work_arr = arr.copy()
        
        return self.__recursive_sort(work_arr)
    
    def __recursive_sort(self, arr: list) -> list:   
        """
        Recursively splits the array into smaller segments until each segment is a single element, which are then
        merged while sorting the merging elements until the entire array is merged and sorted

        Parameters:
            arr (list): the array to be sorted

        Returns:
            list: the sorted list
        """    
        n = len(arr)

        # if array is a single element there is no sorting to do
        if n == 1:
            return arr
        # otherwise it must be sorted
        else:
            middle = n // 2

            # split array into two approx. equal sized segments and sort recursively
            l = self.__recursive_sort(arr[:middle])
            r = self.__recursive_sort(arr[middle:])

            # merge the two sorted segments
            return self.__merge(l,r)

    def __merge(self, a: list,b: list) -> list:
        """
        Merges two lists while sorting the elements in the lists

        Parameters:
            a (list): sorted list
            b (list): sorted list

        Returns:
            list: sorted list consisting of all elements in a and b
        """ 
        i = 0               # index for a
        j = 0               # index for b
        k = 0               # index for merged array
        n = len(a)+len(b)
        arr = [None]*n

        # lists are compared iteratively and the smallest element at each comparison is added to the array
        while i < len(a) and j<len(b):
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        
        # remaining elements from either a or b are inserted into the array
        if i < len(a):
            arr[k:] = a[i:]
        else:
            arr[k:] = b[j:]
        
        return arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge sorting algorithm')

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
    sorting_algo = MergeSort()

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