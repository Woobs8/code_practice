import argparse
import random

class LinkedListElement():
    def __init__(self, data, next_elmnt=None):
        self.data = data
        self.next_elmnt = next_elmnt
    
    def __repr__(self):
        if self.next_elmnt:
            return '{} -> {}'.format(self.data, self.next_elmnt.data)
        else:
            return '{} -> {}'.format(self.data, None)


class LinkedList():
    def __init__(self, iterable):
        self.linked_list = []
        
        for x in iterable:
            self.append(x)

    # print()
    def __repr__(self):
        return str(self.linked_list)

    # [] access
    def __getitem__(self, key):
        return self.linked_list[key]

    # [] assignment
    def __setitem__(self, key, value):
        self.linked_list[key].data = value

    # [] deletion
    def __delitem__(self, key):
        if key <= (len(self)-1):
            if (key-1) > 0:
                self.linked_list[key-1].next_elmnt = self.linked_list[key+1]
            self.linked_list = self.linked_list[:key]+self.linked_list[key+1:]

    # +
    def __add__(self, other):
        self.linked_list[-1].next_elmnt = other[0]
        return LinkedList(self.linked_list + other.linked_list)

    # len
    def __len__(self):
        return len(self.linked_list)

    def append(self, data):
        self.linked_list.append(LinkedListElement(data))
        i = len(self)-1
        if (i-1) >= 0:
            self.linked_list[i-1].next_elmnt = self.linked_list[i]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Implementation of a standard and double-ended queue')
    parser.add_argument('len', help='length of list', type=int)
    args = parser.parse_args()    
    n = args.len

    # initialize linked list
    ll = LinkedList(range(n))

    # print initial linked list
    print('Initial list')
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # index access operator
    print('Index access')
    print(ll[5])
    print('-------------------')

    # index assignment operator
    print('Index assignment')
    ll[5] = 999
    print(ll)
    print('-------------------')

    # index deletion operator
    print('Index deletion')
    del ll[5]
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # addition operator
    print('Addition')
    print(ll + ll)
    print('-------------------')

    # equality operator
    print('Compare with self: {}'.format(ll == ll))
    print('Compare with other: {}'.format(ll == 5))
    print('-------------------')

    # append
    x = 999
    print('Append {}'.format(x))
    ll.append(x)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')