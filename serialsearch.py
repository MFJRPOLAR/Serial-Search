def search (a, first:int, size:int, target:int):
    """Searches for a desired element in an list of elements 
    starting at a[first].

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search 
        target (int): the element to search for

    Returns:
        int: If traget appears in the list, index of the, 
        element that contains target; else -1.
    """    
    # Set and int variable i to 0 
    i = 0

    # set a boolean variable foun to false
    found = False 

    # while there are more elements to search 
    # and the target hasn't been found 
    while ((i<size) and not found):
        # if the current element is the target
        if(a[i+first] == target):
            # set found to true
            found = True
        else:
            # increment i by 1
            i += 1
    # check if the target was found 
    if (found):
        # Return index of the target 
        return i + first 
    else:
        # Return negative 1
        return -1 