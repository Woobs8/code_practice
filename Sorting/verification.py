import unittest
from bubble_sort import BubbleSort
from counting_sort import CountingSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from radix_sort import RadixSort
from bucket_sort import BucketSort
import random
from sorting import BaseSort
import numpy as np

class SortingTestWrapper():
    def __init__(self, algo: BaseSort , n: int, seed: int):
        self.algo = algo
        self.seed = seed
        self.n = n

    def __repr__(self):
        return 'SortingTestWrapper for {}'.format(self.algo)

    def integer_sort(self):
        # prepare randomly shuffled integer data from seed
        sorted_data = list(range(self.n))
        random.seed(self.seed)
        random_data = random.sample(sorted_data, self.n)
        return self.algo.sort(random_data)

    def float_sort(self):
        # prepare randomly shuffled float data from seed
        np.random.seed(self.seed)
        random_data = np.random.rand(1,self.n).tolist()[0]
        return self.algo.sort(random_data)

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.n = 5000
        self.seed = 42
        self.verification = SortingTestWrapper(BaseSort(), self.n, self.seed)

    def test_bubble_sort(self):
        algo = SortingTestWrapper(BubbleSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())
    
    def test_counting_sort(self):
        algo = SortingTestWrapper(CountingSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_heap_sort(self):
        algo = SortingTestWrapper(HeapSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_insertion_sort(self):
        algo = SortingTestWrapper(InsertionSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_merge_sort(self):
        algo = SortingTestWrapper(MergeSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_quick_sort(self):
        algo = SortingTestWrapper(QuickSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_radix_sort(self):
        algo = SortingTestWrapper(RadixSort(), self.n, self.seed)
        self.assertListEqual(algo.integer_sort(), self.verification.integer_sort())

    def test_bucket_sort(self):
        algo = SortingTestWrapper(BucketSort(), self.n, self.seed)
        self.assertListEqual(algo.float_sort(), self.verification.float_sort())

if __name__ == '__main__':
    unittest.main()