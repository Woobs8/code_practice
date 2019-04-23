import argparse
import os
import timeit
from functools import partial
import random
from itertools import accumulate
from sorting import BaseSort

class QuickSort(BaseSort):
    """
    A class used to encapsulate the QuickSort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the QuickSort algorithm


    """

    def __repr__(self):
        return "QuickSort"

    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the QuickSort algorithm

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

        # start the recursive QuickSort algorithm
        self.__quick_sort(work_arr,0,len(work_arr)-1)

        return work_arr

    def __quick_sort(self, arr: list, low: int, high: int):
        """
        Recursive implementation of the QuickSort algorithm

        Parameters:
            arr (list): list to be sorted
            low (int): start index of current subarray
            high (int): end index of current subarray

        Returns:
            None
        """ 
        # sorting is only required if the current subarray (arr[low:high]) is longer than a single element
        if low < high:
            # partition array by finding the index of the correctly placed partition element
            pi = self.__partition(arr, low, high)

            # recursively sort each subarray on either side of partition
            self.__quick_sort(arr, low, pi-1)
            self.__quick_sort(arr, pi+1, high)

    
    def __partition(self, arr: list, low: int, high: int):
        """
        Partitions the input subarray and returns the index of the correctly placed partition

        Parameters:
            arr (list): list to be sorted
            low (int): start index of current subarray
            high (int): end index of current subarray

        Returns:
            partition index
        """ 
        i = low - 1             # index of rightmost element smaller than pivot
        pivot = arr[high]       # last element is used as pivot

        # iterate all elements in subarray
        for j in range(low,high):
            """
            If the current element is smaller than the pivot, i is incremented and the current element is swapped with the element at index i. 
            The result is that after one pass, every element up to and including element i will be smaller than the pivot.
            """
            if arr[j] <= pivot:
                i += 1                              
                arr[i], arr[j] = arr[j], arr[i]     # swap elements
        
        # when all element up to index i are smaller than the pivot, i+1 must be the correct place for the pivot
        arr[i+1], arr[high] = arr[high], arr[i+1]

        # return the pivot index
        return i+1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='QuickSort algorithm')

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
    sorting_algo = QuickSort()

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