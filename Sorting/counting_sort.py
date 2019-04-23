import argparse
import os
import timeit
from functools import partial
import random
from collections import defaultdict
from itertools import accumulate
from sorting import BaseSort

class CountingSort(BaseSort):
    """
    A class used to encapsulate the Counting Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the counting sort algorithm

    """

    def __repr__(self):
        return "Counting Sort"

    def sort(self, arr: list) -> list:
        """
        Sorts an array using the counting sort algorithm

        Parameters:
            arr (list): list to be sorted

        Returns:
            list: the sorted list
        """ 
        n = len(arr)
        work_arr = [None]*n
        minElmt = min(arr)
        maxElmt = max(arr)

        # initialize counting array to have room for the entire range of elements
        count_arr = [0]*(maxElmt-minElmt+1)

        # count occurrences of each element in array
        for x in arr:
            count_arr[x+minElmt] += 1

        # do an accumulative sun of the element occurences in the counting array
        count_arr = list(accumulate(count_arr))

        # iterate elements in array and place in sorted array based on occurences in counting array
        for x in arr:
            work_arr[count_arr[x+minElmt]-1] = x
            count_arr[x+minElmt] -= 1
        return work_arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Counting sorting algorithm')

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
    sorting_algo = CountingSort()

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