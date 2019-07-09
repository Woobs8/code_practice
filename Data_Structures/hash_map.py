import argparse
from linked_list import LinkedList


class HashMap():
    """
    A class encapsulating a hash map data structure

    Attributes
    ----------
    size (int)
        Size of the hash map

    hash_table (list)
        List structure containing the hash table

    Methods
    -------
    hash
        Hashes a key and turns it into an index to a list representing a hash map

    insert
        Inserts a key-value pair

    delete
        Delete the key-value pair specified by key

    search
        Search for the value indexed by key

    __search_ll
        Searches a linked list for the element containing key
    """
    def __init__(self, size):
        self.size = size
        self.hash_table = [LinkedList() for __ in range(size)]


    def __repr__(self):
        print_list = []
        for i in range(self.size):
            ll = self.hash_table[i]
            node = ll.front
            while node:
                data = node.data
                print_list.append('{}:{}'.format(data[0], data[1]))
                node = node.next
        return '{' + ', '.join(print_list) + '}'


    def hash(self, key):
        """
        Hashes a key and turns it into an index to a list representing a hash map

        Parameters:
            key (Object): unhashed key to hash table

        Returns:
            None
        """
        hash_key = hash(key) % (self.size)
        return hash_key
    

    def insert(self, key, value):
        """
        Inserts a key-value pair

        Parameters:
            key (Object): unhashed key to hash table
            value (Object): data value to insert

        Returns:
            None
        """
        hash_key = self.hash(key)
        data = [key, value]
        self.hash_table[hash_key].append(data)


    def delete(self, key):
        """
        Delete the key-value pair specified by key

        Parameters:
            key (Object): unhashed key to hash table
            value (Object): data value to insert

        Returns:
            None
        """
        hash_key = self.hash(key)
        ll = self.hash_table[hash_key]
        node = self.__search_ll(ll, key)
        if node:
            value = node.data[1]
            ll.delete([key, value], True)


    def search(self, key):
        """
        Search for the value indexed by key

        Parameters:
            key (Object): unhashed key to hash table

        Returns:
            None
        """
        hash_key = self.hash(key)
        ll = self.hash_table[hash_key]
        node = self.__search_ll(ll, key)
        if node:
            return node.data[1]
        else:
            return None       


    def __search_ll(self, ll, key):
        """
        Searches a linked list for the element containing key

        Parameters:
            ll (LinkedList): linked list object
            key (Object): unhashed key to hash table

        Returns:
            None
        """
        node = ll.front
        while node:
            print(node)
            if node.data[0] == key:
                break
            node = node.next
        return node

    # [] read operator
    def __getitem__(self, key):
        hash_key = self.hash(key)
        ll = self.hash_table[hash_key]
        node = self.__search_ll(ll, key)
        if node:
            return node.data[1]
        else:
            return None

    # [] assignment operator
    def __setitem__(self, key, value):
        hash_key = self.hash(key)
        ll = self.hash_table[hash_key]
        node = self.__search_ll(ll, key)
        if node:
            node.data[1] = value
        else:
            ll.append([key, value])

    # del operator
    def __delitem__(self, key):
        hash_key = self.hash(key)
        ll = self.hash_table[hash_key]
        node = self.__search_ll(ll, key)
        if node:
            value = node.data[1]
            ll.delete([key, value], True)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of a hash map')
    parser.add_argument('len', help='size of hash map', type=int)
    args = parser.parse_args()    
    n = args.len

    # initialize hash map
    print('Initial hash table')
    hash_map = HashMap(n)
    print(hash_map)
    print('-------------------')

    # insert using method
    print('Inserting using method')
    hash_map.insert('Thomas', 27)
    hash_map.insert('Mette', 22)
    hash_map.insert('Bitten', 57)
    hash_map.insert('Stig', 57)
    print(hash_map)
    print('-------------------')

    # search using method
    key = 'Thomas'
    print('Searching for {} using method'.format(key))
    val = hash_map.search(key)
    print(val)
    print('-------------------')

    # delete using method
    key = 'Thomas'
    print('Deleting {} using method'.format(key))
    hash_map.delete(key)
    print(hash_map)
    print('-------------------')

    # inserting using index operator
    print('Inserting using operator')
    hash_map['Thomas'] = 20
    print(hash_map)
    print('-------------------')

    # updating using index operator
    print('Updating using operator')
    hash_map['Thomas'] = 27
    print(hash_map)
    print('-------------------')

    # searching using index operator
    key = 'Thomas'
    print('Searching for {} using operator'.format(key))
    val = hash_map['Thomas']
    print(val)
    print('-------------------')

    # deleting using index operator
    key = 'Thomas'
    print('Deleting {} using operator'.format(key))
    del hash_map['Thomas']
    print(hash_map)
    print('-------------------')