from insertion_sort import InsertionSort
from itertools import chain
from functools import partial
import argparse
import timeit
import numpy as np


class BucketSort():
    """
    A class used to encapsulate the Bucket Sort algorithm

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr)
        Sorts an array using the bucket sort algorithm
    """
    def __repr__(self):
        return 'Bucket sort'


    def sort(self, arr: list) -> list:
        """
        Sorts an array using the bucket sort algorithm

        Parameters:
            arr (list): list to be sorted

        Returns:
            list: the sorted list
        """ 
        n = len(arr)

        buckets = []
        for i in range(n):
            buckets.append([])

        for x in arr:
            index = int(n*x)
            buckets[index].append(x)

        ins_sort = InsertionSort()
        for i in range(n):
            buckets[i] = ins_sort.sort(buckets[i])
        return list(chain.from_iterable(buckets))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bucket sorting algorithm')
    parser.add_argument('-data', help='parameters for generating random data [len, seed]', nargs=2, type=int)
    parser.add_argument('-t', help='measure the execution time', nargs=2, required=False, type=int)
    args = parser.parse_args()
    
    n = args.data[0]
    seed = args.data[1]
    t = args.t

    # shuffle data randomly with seed
    np.random.seed(seed)
    random_data = np.random.rand(1,n).tolist()[0]
    sorted_data = sorted(random_data)
    sorting_algo = BucketSort()

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