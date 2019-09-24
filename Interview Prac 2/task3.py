"""
Basic implementation of reading file into list on a line-by-line basis

@author         Mark Diedericks 30572738
@since          18/09/2019
@modified       18/09/2019
"""

import task2

def read_text_file(name):
    """
    Read the lines of a text file as elements into a list

    @param          Name; The full file name
    @return         A ListADT instance where each element is a line from the provided text file
    @complexity     O(n) for both best and worst case, where n is the number of lines of the file
    @precondition   The file, name, exists
    @exception      File does not exist, file handle cannot be obtained, file handle cannot be disposed.
    @postcondition  The line_list will contain, in order, the line of the file from top to bottom. Excluding new-line characters
    """
    
    # Instantiate a list for the lines
    line_list = task2.ListADT()

    # Open the file, read each line and append to the line_list
    with open(name) as f:
        for line in f:
            line_list.append(line.replace('\n', ''))    # Remove new-line characters

    # Ensure file is closed
    if not f.closed:
        raise IOError('File is not closed.')

    # Return the list of lines
    return line_list

