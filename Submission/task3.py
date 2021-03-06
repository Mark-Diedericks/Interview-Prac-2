"""
Basic implementation of reading file into list on a line-by-line basis

@author         Mark Diedericks 30572738
@since          18/09/2019
@modified       18/09/2019
"""

import task2

def read_text_file(name):
    """
    Set the element in the list at index

    @param          None
    @return         None
    @complexity     O(1) for both best and worst case
    @precondition   The index is within then list bounds; -self.length <= index <= self.length-1
    @exception      Index is out of bounds 
    @postcondition  The element located at the index will be item
    """
    
    # Instantiate a list for the lines
    line_list = task2.ListADT()

    # Open the file, read each line and append to the line_list
    with open(name) as f:
        for line in f:
            line_list.append(line)

    # Ensure file is closed
    if not f.closed:
        raise IOError('File is not closed.')

    # Return the list of lines
    return line_list

