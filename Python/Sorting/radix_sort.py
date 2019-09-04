import argparse
import os
import timeit
from functools import partial
import random
from itertools import accumulate
from sorting import BaseSort


class RadixSort(BaseSort):
    """
    A class used to encapsulate the Radix Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the radix sort algorithm

    __digit_counting_sort(arr, exp)
        Counting sort implementation that sorts the array based on the element digit specified by exp

    """
    def __repr__(self):
        return "Radix Sort"


    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the radix sort algorithm

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
        
        max_elmt = max(work_arr)    # max element is used for stopping criteria

        # sort every digit until the largest element is reduced to a decimal (assuming array consists of integers only)
        exp = 1  
        while max_elmt/exp >= 1:
            # counting sort is used for every digit
            work_arr = self.__digit_counting_sort(work_arr, exp)

            # digits are represented using exp = 10^i, where i is the i'th digit
            exp *= 10

        return work_arr
    

    def __digit_counting_sort(self, arr: list, exp: int) -> list:
        """
        Counting sort implementation that sorts the array based on the element digit specified by exp

        Parameters:
            arr (list): list to be sorted
            exp (int): specifies the digit to sort by (exp=10^i for digit i)

        Returns:
            list: the list sorted by the digit specified by exp
        """ 
        n = len(arr)
        work_arr = [None]*n

        # initialize counting array (assuming base 10)
        count_arr = [0]*10

        # count occurrences of each element digit in array
        for x in arr:
            # find digit index
            digit_index = int((x / exp) % 10)
            count_arr[digit_index] += 1

        # do an accumulative sun of the elements digit occurences in the counting array
        count_arr = list(accumulate(count_arr))

        # iterate array elements in reverse and place in sorted array based on occurences in counting array
        # reverse iteration ensures that in the case of equality, the elements occuring first in the unsorted array will occur first in the sorted array
        for x in arr[::-1]:
            digit_index = int((x / exp) % 10)
            work_arr[count_arr[digit_index]-1] = x
            count_arr[digit_index] -= 1
        return work_arr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Radix sorting algorithm')

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
    sorting_algo = RadixSort()

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