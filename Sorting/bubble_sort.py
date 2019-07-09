import argparse
import timeit
from functools import partial
import random
from sorting import BaseSort


class BubbleSort(BaseSort):
    """
    A class used to encapsulate the Bubble Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using the bubble sort algorithm by iteratively comparing each element with its adjacent element
        swapping the two if the sort condition is satisfied.
    """
    def __repr__(self):
        return 'Bubble Sort'


    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the bubble sort algorithm by iteratively comparing each element with its adjacent element
        swapping the two if the sort condition is satisfied.

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

        # outer pass: n passes required to guarantee the array is sorted
        for i in range(n):
            swapped = False
            # inner pass: iterate all 0:n-i elements, as last i elements will already be sorted
            for j in range(n-i-1):
                if work_arr[j] > work_arr[j+1]:
                    work_arr[j], work_arr[j+1] = work_arr[j+1], work_arr[j]
                    swapped = True

            # if no swaps in inner loop, the array is sorted
            if not swapped:
                break
        
        return work_arr


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bubble sorting algorithm')
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
    sorting_algo = BubbleSort()

    # verify that list is sorted correctly
    if not sorting_algo.sort(random_data) == sorted_data:
        print('Error sorting array using <{}>'.format(sorting_algo))
        exit(1)

    if args.t:
        times = timeit.Timer(partial(sorting_algo.sort, random_data)).repeat(t[1], t[0])
        
        # average time taken
        time_taken = min(times) / t[0]

        print('Timing analysis')
        print('Sorting method: {}'.format(sorting_algo))
        print('Data length: {}'.format(n))
        print('Executions: {}'.format(t[0]))
        print('Average time: {}s'.format(time_taken))