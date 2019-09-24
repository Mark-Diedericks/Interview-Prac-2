"""
ListADT based implementation of a line based editor

@author         Mark Diedericks 30572738
@since          18/09/2019
@modified       23/09/2019
"""

import task2
import task3

class Editor:
    def __init__(self):
        """
        Instantiates a new instance of the ListADT class with a specified capacity, size.

        @param          None
        @return         None
        @complexity     O(1) for both best and worst case.
        @postcondition  An empty list of lines is created for the instance
        """
        self.text_lines = task2.ListADT()

    def read_filename(self, file_name):
        """
        Read the lines of a text file as elements into self.text_lines

        @param          File_name; The full name of the file
        @return         None
        @complexity     O(n) for both best and worst case, where n is the number of lines of the file
        @precondition   The file, name, exists
        @exception      File does not exist, file handle cannot be obtained, file handle cannot be disposed.
        @postcondition  self.text_lines will contain, in order, the line of the file from top to bottom. Excluding new-line characters
        """
        self.text_lines = task3.read_text_file(file_name)
        
    def print_num(self, line_num):
        """
        Prints the line at the specified line number or all lines if no line_num is empty.

        @param          Line_num; string representation of inputted line number
        @return         None
        @complexity     O(1) for best case - single line, O(n) for worst case - all lines, where n is the length of text_lines
        @postcondition  All lines will be printed for no argument, a single line will be printed for a valid argument, and a corresponding 
                        error message will be printed for an invalid argument.
        """

        # No line number given, print all lines in the list
        if len(line_num.strip()) == 0:
            for i in range(len(self.text_lines)):
                print(self.text_lines[i])     # Print each line individually, print will append new-line character to each
        
        # An input value was given, attempt to parse it and print
        else:
            try:
                # Calculate index and print line
                num = int(line_num.strip())
                if num == 0:
                    raise IndexError()

                i = num if num < 0 else - 1

                print(self.text_lines[i])
                
            except ValueError:
                # Input is not convertable to an integer
                print('Invalid input argument.')

            except IndexError:
                # Input index is not within list bounds
                print('Invalid line number.')


    def delete_num(self, line_num):
        """
        Deletes the line at the specified line number or all lines if no line_num is empty.

        @param          Line_num; string representation of inputted line number
        @return         None
        @complexity     O(1) for best case - single line at back, O(n) for worst case - all lines or single line not at back, 
                        where n is the length of text_lines
        @postcondition  All lines will be deleted for no argument, a single line will be deleted for a valid argument, and a corresponding 
                        error message will be printed for an invalid argument.
        """

        # No line number given, delete all lines in the list.
        # Delete from the back forwards so that no shuffling is required
        # therefore the delte function runs in O(1) making the overall
        # complexity of this only O(n) instead O(n^2), where n is the number
        # of lines of the file.
        if len(line_num.strip()) == 0:
            for i in range(len(self.text_lines), 0, -1):
                self.text_lines.delete(i - 1)     # Delete each line individually
        
        # An input value was given, attempt to parse it and delete
        else:
            try:
                # Calculate index and delete line
                num = int(line_num.strip())
                if num == 0:
                    raise IndexError()

                i = num if num < 0 else - 1

                self.text_lines[i].delete(i)
                
            except ValueError:
                # Input is not convertable to an integer
                print('Invalid input argument.')

            except IndexError:
                # Input index is not within list bounds
                print('Invalid line number.')

    def insert_num(self, line_num, text):
        """
        Inserts, in order, the inputted lines at the specified index

        @param          Line_num; string representation of inputted line number 
        @param          Text; string of lines to be inserted
        @return         None
        @complexity     O(m*n) for both best and worst case, where n is the length of text_lines and m is the length of lines
        @postcondition  text_lines will contain, in order, the lines at the specified index.
        """

        # Convert text string into lines array
        lines = task2.ListADT()
        for l in text.split('\n'):
            if l.strip() != '.':
                lines.append(l.replace('\n', ''))   # Ensure no new-line characters for consistency

        # Use insert_num_strings to insert lines
        insert_num_strings(line_num, lines)

    def insert_num_strings(self, num, lines):
        """
        Inserts, in order, the inputted lines at the specified index

        @param          Line_num; string representation of inputted line number 
        @param          Lines; the list of line strings to be inserted
        @return         None
        @complexity     O(m*n) for both best and worst case, where n is the length of text_lines and m is the length of lines
        @postcondition  text_lines will contain, in order, the lines at the specified index.
        """
        
        # An input value was given, attempt to parse it and delete
        try:
            # Calculate index
            num = int(line_num.strip())
            if num == 0:
                raise IndexError()

            i = num if num < 0 else - 1
            
            # Insert the lines into their positions, however, since
            # insert places the element at that shuffles the remaining
            # items down, we want to insert the lines stepping forward,
            # each time increasing the insert index by 1. This will ensure
            # the number of elements which must be shuffled up to make
            # space is constant. Thus the time complexity will be O(m*n)
            # instead of O(m*(n+m)) where n is the number of elements past
            # the index and m is the size of lines.
            for j in range(len(lines)):
                self.text_lines.insert(j + i, lines[j].replace('\n', ''))    # Ensure new-line characters are removed for consistency

        except IndexError:
            # Input index is not within list bounds
            print('Invalid line number.')

    def search_string(self, query):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
