import unittest
from bubble_sort import BubbleSort
from counting_sort import CountingSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from radix_sort import RadixSort
import random
from sorting import BaseSort

class SortingTestWrapper():
    def __init__(self, algo: BaseSort , n: int, seed: int):
        self.algo = algo
        self.seed = seed
        self.n = n

    def __repr__(self):
        return 'SortingTestWrapper for {}'.format(self.algo)

    def sort(self):
        # prepare randomly shuffled data from seed
        sorted_data = list(range(self.n))
        random.seed(self.seed)
        random_data = random.sample(sorted_data, self.n)
        return self.algo.sort(random_data)

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.n = 5000
        self.seed = 42
        self.verification = SortingTestWrapper(BaseSort(), self.n, self.seed)

    def test_bubble_sort(self):
        algo = SortingTestWrapper(BubbleSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())
    
    def test_counting_sort(self):
        algo = SortingTestWrapper(CountingSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

    def test_heap_sort(self):
        algo = SortingTestWrapper(HeapSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

    def test_insertion_sort(self):
        algo = SortingTestWrapper(InsertionSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

    def test_merge_sort(self):
        algo = SortingTestWrapper(MergeSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

    def test_quick_sort(self):
        algo = SortingTestWrapper(QuickSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

    def test_radix_sort(self):
        algo = SortingTestWrapper(RadixSort(), self.n, self.seed)
        self.assertListEqual(algo.sort(), self.verification.sort())

if __name__ == '__main__':
    unittest.main()