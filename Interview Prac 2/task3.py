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



### SMALL TESTS ###
if __name__ == '__main__':
    l = task2.ListADT()
    l.append('Yossarian decided\n')
    l.append('not to utter\n')
    l.append('another word.')
    assert read_text_file('small.txt') == l
    
    l = task2.ListADT()
    l.append('Line 1\n')
    l.append('Line 2\n')
    l.append('Line 3\n')
    l.append('Line 4')
    assert read_text_file('small2.txt') == l
    
    print('Both tests passed.')