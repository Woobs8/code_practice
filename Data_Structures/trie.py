import argparse


class Trie():
    """
    A class encapsulating a trie structure

    Attributes
    ----------
    _root_char (str)
        Character reserved for root of trie

    _end_char (str)
        Character reserved for end of tries

    trie (dict)
        dictionary representing trie

    Methods
    -------
    insert
        Insert a key-value pair

    search
        Search for the value indexed by key

    delete
        Delete the key-value pair specified by key
    """
    def __init__(self):
        self._root_char = '@'
        self._end_char = '*'
        self.trie = {'@':dict()}


    def __repr__(self):
        return repr(self.trie)


    def insert(self, key, val):
        """
        Insert a key-value pair

        Parameters:
            key (str): key to index val by
            val (Object): value to insert

        Returns:
            None
        """
        cur_dict = self.trie['@']
        for letter in key:
            if letter == self._end_char:
                raise IndexError
            
            if letter in cur_dict:
                cur_dict = cur_dict[letter]
            else:
                cur_dict[letter] = dict()
                cur_dict = cur_dict[letter]
        cur_dict[self._end_char] = val

    
    def search(self, key):
        """
        Search for the value indexed by key

        Parameters:
            key (str): key to search value by

        Returns:
            None
        """
        cur_dict = self.trie['@']
        for letter in key:          
            if letter not in cur_dict:
                raise IndexError
            else:
                cur_dict = cur_dict[letter]
        if self._end_char in cur_dict:
            return cur_dict[self._end_char]
        else:
            return None


    def delete(self, key):
        """
        Delete the key-value pair specified by key

        Parameters:
            key (str): key to delete value by

        Returns:
            None
        """
        cur_dict = self.trie['@']
        for letter in key:          
            if letter in cur_dict:
                cur_dict = cur_dict[letter]
        if self._end_char in cur_dict:
            del cur_dict[self._end_char]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Implementation of a trie for data retrieval')
    args = parser.parse_args()    

    # initialize trie
    print('Initial trie')
    trie = Trie()
    print(trie)
    print('-------------------')

    # insert non-overlapping keys
    print('Inserting non-overlapping keys')
    trie.insert('Thomas', 27)
    trie.insert('Mette', 22)
    trie.insert('Bitten', 57)
    trie.insert('Stig', 57)
    print(trie)
    print('-------------------')

    # insert overlapping keys
    print('Inserting overlapping keys')
    trie.insert('Thor', 35)
    trie.insert('Merete', 56)
    trie.insert('Bo', 24)
    trie.insert('Søren', 29)
    print(trie)
    print('-------------------')

    # search for key
    key = 'Thomas'
    print('Searching for {}'.format(key))
    val = trie.search(key)
    print(val)
    print('-------------------')

    # delete key
    key = 'Thor'
    print('Deleting {}'.format(key))
    trie.delete(key)
    print(trie)
    print('-------------------')

    # search for key
    key = 'Thor'
    print('Searching for {}'.format(key))
    val = trie.search(key)
    print(val)
    print('-------------------')