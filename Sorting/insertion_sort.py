import argparse
import os
import timeit
from functools import partial
import random
from collections import defaultdict
from itertools import accumulate
from sorting import BaseSort

class InsertionSort(BaseSort):
    """
    A class used to encapsulate the Insertion Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the insertion sort algorithm

    """

    def __repr__(self):
        return "Insertion Sort"

    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the insertion sort algorithm

        Parameters:
            arr (list): list to be sorted

        Returns:
            list: the sorted list
        """ 
        n = len(arr)
        if in_place:
            work_arr = arr
        else:
            work_arr = arr.copy()
        
        # iterate through all elements and sort along the way (elements [0:i-1] will be sorted at any given time)
        for i in range(1,n):
            # from the leftmost unsorted element (i), iterate in reverse to find the sorted position of the element
            for j in range(i,0,-1):
                # the  unsorted element is swapped to the left until it is in its correct position
                if work_arr[j] < work_arr[j-1]:
                    work_arr[j], work_arr[j-1] = work_arr[j-1], work_arr[j]
                else:
                    break
        return work_arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insertion sorting algorithm')

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
    sorting_algo = InsertionSort()

    # verify that list is sorted correctly
    if not sorting_algo.sort(random_data) == sorted_data:
        print('Error sorting array using <{}>'.format(sorting_algo))
        exit(1)

    # measure execution time
    if args.t:
        times = timeit.Timer(partial(sorting_algo.sort, random_data)).repeat(t[1], t[0])

        # average time taken
        time_taken = min(times) / t[0]

        print('Timing analysis:')
        print('\tSorting method: {}'.format(sorting_algo))
        print('\tData length: {}'.format(n))
        print('\tExecutions: {}'.format(t[0]))
        print('\tAverage time: {}s'.format(time_taken))