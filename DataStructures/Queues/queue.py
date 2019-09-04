import argparse
import random
import math


class Queue():
    """
    A class encapsulating a queue data structure

    Attributes
    ----------
    queue (list)
        The list representing the ordered queue

    len (int)
        The current length of the queue

    max_len (int)
        The maximum allowed length of the queue

    Methods
    -------
    append
        Insert an element at the end of the queue

    pop
        Remove an element from the front of the queue

    """
    def __init__(self, iterable, max_len=None):
        self.queue = []
        self.len = 0
        self.max_len = max_len if max_len else math.inf

        # fill queue with elements in iterable if supplied
        if iterable:
            for x in iterable:
                if self.len < self.max_len:
                    self.queue.append(x)
                    self.len += 1


    def __repr__(self):
        return str(self.queue)


    def append(self, data):
        """
        Insert an element at the end of the queue

        Parameters:
            data (Object): element to insert

        Returns:
            None
        """ 
        if self.len < self.max_len:
            self.queue.append(data)
            self.len += 1
        else:
            raise IndexError


    def pop(self):
        """
        Removes an element from the front of the queue

        Parameters:
            -
        
        Returns:
            Object: value of popped element
        """ 
        if self.len > 0:
            elmt = self.queue[-1]
            self.queue = self.queue[1:]
            self.len -= 1
            return elmt
        else:
            raise IndexError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of a standard and double-ended queue')
    parser.add_argument('len', help='length of queue', type=int)
    args = parser.parse_args()    
    n = args.len

    # init standard queue
    std_queue = Queue(range(n))

    # print initial queue
    print(std_queue)
    print('Queue length: {}'.format(std_queue.len))

    # add elements to queue
    std_queue.append(50)
    std_queue.append(51)

    # print extended queue
    print(std_queue)
    print('Queue length: {}'.format(std_queue.len))

    # pop elements from queue
    std_queue.pop()
    std_queue.pop()

    # print extended queue
    print(std_queue)
    print('Queue length: {}'.format(std_queue.len))