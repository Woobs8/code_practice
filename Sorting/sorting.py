class BaseSort():
    """
    A base class for sorting algorithms

    Attributes
    ----------
    -

    Methods
    -------
    sort(arr, in_place=False)
        Sorts an array using built-in sort method

    """
    def sort(self, arr: list, in_place=False) -> list:
        """
        Sorts an array using the built-in sort method

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
        
        work_arr.sort()
        return work_arr