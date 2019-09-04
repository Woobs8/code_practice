import argparse
import random


class LinkedListElement():
    """
    A class encapsulating an element in a linked list

    Attributes
    ----------
    data (Object)
        Value to assign to element

    next (LinkedListElement)
        Reference to the next element in the linked list

    Methods
    -------
    -
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

    def __repr__(self):
        next_data = self.next.data if self.next else None
        return '{} -> {}'.format(self.data, next_data)


class LinkedList():
    """
    A class encapsulating a linked list data structure

    Attributes
    ----------
    front (LinkedListElement)
        Element at the front of the list

    back (LinkedListElement)
        Element at the back of the queue

    Methods
    -------
    append
        Insert an element at the end of the linked list

    append_left
        Insert an element at the front of the linked list

    contains
        Determine whether the data value exist in the linked list

    __search
        Searches for the element with the specified value

    insert
        Inserts an element with the specified data at the position following 
        the first element containing the value prev. Raises exception if previous
        element does not exist.
    
    delete
        Delete an element in the linked list with the value specified by data.
        If specified, delete all elements with the value data.
    """
    def __init__(self, iterable=None):
        self.front = None
        self.back = None
        
        if iterable:
            for x in iterable:
                self.append(x)


    # print()
    def __repr__(self):
        node = self.front
        ll = []
        while node:
            ll.append(str(node.data))
            node = node.next
        return '->'.join(ll)


    # len
    def __len__(self):
        node = self.front
        length = 0
        while node:
            node = node.next
            length += 1
        return length


    def append(self, data):
        """
        Insert an element at the end of the linked list

        Parameters:
            data (Object): element to insert

        Returns:
            None
        """
        new_node = LinkedListElement(data)
        if len(self) == 0:
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node


    def append_left(self, data):
        """
        Insert an element at the front of the linked list

        Parameters:
            data (Object): element to insert

        Returns:
            None
        """
        new_node = LinkedListElement(data)
        new_node.next = self.front
        self.front = new_node

        if len(self) == 0:
            self.back = new_node


    def contains(self, data):
        """
        Determine whether the data value exist in the linked list

        Parameters:
            data (Object): value to search for

        Returns:
            Bool: whether an element with the value data exists
        """
        node = self.__search(data)
        return True if node else False


    def __search(self, data):
        """
        Searches for the element with the specified value

        Parameters:
            data (Object): value to search for

        Returns:
            node: first element with specified value
        """
        node = self.front
        while node:
            if node.data == data:
                break
            
            node = node.next
        return node


    def insert(self, prev, data):
        """
        Inserts an element with the specified data at the position following 
        the first element containing the value prev. Raises exception if previous
        element does not exist.

        Parameters:
            prev (Object): value of element to insert new element after
            data (Object): value to insert

        Returns:
            None
        """
        node = self.__search(prev)
        if not node:
            raise IndexError

        new_node = LinkedListElement(data)
        new_node.next = node.next
        node.next = new_node

        if self.back == node:
            self.back = new_node

    
    def delete(self, data, delete_all=False):
        """
        Delete an element in the linked list with the value specified by data.
        If specified, delete all elements with the value data.

        Parameters:
            data (Object): value to delete elements by
            delete_all (Bool): whethet to delete all elements with the value data

        Returns:
            None
        """
        node = self.front
        prev = None
        while node:
            if node.data == data:
                if node == self.front:
                    self.front = node.next
                else:
                    prev.next = node.next
                node = node.next
                if not delete_all:
                    break
            
            if node:   
                prev = node
                node = node.next
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of a standard queue')
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

    # append end
    x = 999
    print('Append {} to back'.format(x))
    ll.append(x)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # append front
    x = 999
    print('Append {} to front'.format(x))
    ll.append_left(x)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # is contained
    x = 999
    print('Verify that {} is contained in list'.format(x))
    ret = ll.contains(x)
    print('Is {} contained in list: {}'.format(x, ret))
    print('-------------------')

    # is not contained
    x = 1000
    print('Verify that {} is not contained in list'.format(x))
    ret = ll.contains(x)
    print('Is {} contained in list: {}'.format(x, ret))
    print('-------------------')

    # insert value after exisitng element
    prev = 15
    x = 999
    print('Insert {} after {}'.format(x, prev))
    ll.insert(prev, x)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # insert value after non-existing elemen t
    prev = 2000
    x = 999
    print('Insert {} after {}'.format(x, prev))
    try:
        ll.insert(prev, x)
    except IndexError:
        pass
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # delete first occurrence of element
    x = 999
    print('Delete first occurrence of {}'.format(x))
    ll.delete(x)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')

    # delete all occurrences of element
    x = 999
    print('Delete all occurrences of {}'.format(x))
    ll.delete(x, delete_all=True)
    print(ll)
    print('List length: {}'.format(len(ll)))
    print('-------------------')