"""
ListADT based implementation of a line based editor

@author         Mark Diedericks 30572738
@since          18/09/2019
@modified       25/09/2019
"""

import task2
import task3

# Command class
class Command:
    def __init__(self, cmd, arg, data):
        self.cmd = cmd
        self.arg = arg
        self.data = data

# Node class
class Node:
    def __init__(self, next, item):
        self.next = next
        self.item = item

    ### END NODE CLASS ###

# Linked node based stack implementation
class StackADT:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None

    def push(self, item):
        n = Node(self.top, item)
        self.top = n

    def pop(self):

        if self.is_empty():
            raise IndexError('Stack is empty')

        n = self.top
        self.top = n.next
        return n.item

    ### END STACK CLASS ###

class Editor:
    def __init__(self):
        """
        Instantiates a new instance of the ListADT class with a specified capacity, size.

        @param          None
        @return         None
        @complexity     O(1) for both best and worst case.
        @postcondition  An empty list of lines is created for the instance, an empty command stack is created
        """
        self.text_lines = task2.ListADT()
        self.cmd_stack = StackADT()

    def read_filename(self, file_name):
        """
        Read the lines of a text file as elements into self.text_lines

        @param          File_name; The full name of the file
        @return         None
        @complexity     O(n) for both best and worst case, where n is the number of lines of the file
        @precondition   The file, name, exists
        @exception      File does not exist, file handle cannot be obtained, file handle cannot be disposed.
        @postcondition  self.text_lines will contain, in order, the line of the file from top to bottom. Excluding new-line characters
                        The command stack will be reset as previous commands are no longer relevant and undo-able.
        """
        self.text_lines = task3.read_text_file(file_name)
        self.cmd_stack = StackADT();
        
    def print_num(self, line_num):
        """
        Prints the line at the specified line number or all lines if no line_num is empty.

        @param          Line_num; string representation of inputted line number
        @return         None
        @complexity     O(1) for best case - single line, O(n) for worst case - all lines, where n is the length of text_lines
        @postcondition  All lines will be printed for no argument, a single line will be printed for a valid argument.
        """

        # No line number given, print all lines in the list
        if len(line_num.strip()) == 0:
            for i in range(len(self.text_lines)):
                print('  ' + self.text_lines[i])     # Print each line individually, print will append new-line character to each
        
        # An input value was given, attempt to parse it and print
        else:
            # Calculate index and print line
            num = int(line_num.strip())
            if num == 0:
                raise IndexError()

            i = num if num < 0 else num - 1

            print('  ' + self.text_lines[i])


    def delete_num(self, line_num, is_undo = False):
        """
        Deletes the line at the specified line number or all lines if no line_num is empty.

        @param          Line_num; string representation of inputted line number
        @return         None
        @complexity     O(1) for best case - single line at back, O(n) for worst case - all lines or single line not at back, 
                        where n is the length of text_lines
        @postcondition  All lines will be deleted for no argument, a single line will be deleted for a valid argument.
        """

        # Create a data stack to store deleted line(s)
        data = task2.ListADT()

        # No line number given, delete all lines in the list.
        # Delete from the back forwards so that no shuffling is required
        # therefore the delete function runs in O(1) making the overall
        # complexity of this only O(n) instead O(n^2), where n is the number
        # of lines in the list. The same applies to the insert, we insert
        # at the rear of the list to avoid shuffling items, keeping the
        # complexity at O(n). However, because of this we must iteratre
        # twice, once to save all the lines, and another to delete all the
        # lines. This increases the constant factor but complexity stays O(n).
        # As the list is used by reference, it would be bad practice to simply
        # set data equal to the text_lines and then set text_lines to a new
        # ListADT as this would change the object we refer to without changing
        # other possible references. However, it would work in this case and
        # it would certainly be much faster to execute.
        if len(line_num.strip()) == 0:
            for i in range(len(self.text_lines)):
                data.insert(-1, self.text_lines[i])      # Store each line we delete, from front to back

            for i in range(len(self.text_lines), 0, -1):
                self.text_lines.delete(i - 1)            # Delete each line individually, from back to front
        
        # An input value was given, attempt to parse it and delete
        else:
            # Calculate index and delete line
            num = int(line_num.strip())
            if num == 0:
                raise IndexError()
            
            i = num if num < 0 else num - 1

            data.insert(-1, self.text_lines[i]) # Store the line which we delete
            self.text_lines.delete(i)           # Delete the line

        if not is_undo:
            # Calculate adjusted line number for insert to work
            adj_line_num = '1' if len(line_num.strip()) == 0 else line_num

            # Create a command list and store information required for undo
            cmd = Command('insert', adj_line_num, data)

            # Push the command to the command stack
            self.cmd_stack.push(cmd);

    def insert_num(self, line_num):
        """
        Inserts, in order, the inputted lines at the specified index

        @param          Line_num; string representation of inputted line number
        @return         None
        @complexity     O(m*n) for both best and worst case, where n is the length of text_lines and m is the length of lines
        @postcondition  text_lines will contain, in order, the lines at the specified index.
        """

        # Have user input line(s) and append them to a list,
        # later insert this list using insert_num_strings
        lines = task2.ListADT()
        l = input('  ')
        while l.strip() != '.':
            lines.append(l.replace('\n', ''))   # Ensure no new-line characters for consistency
            l = input('  ')

        # Use insert_num_strings to insert lines
        self.insert_num_strings(line_num, lines)

    def insert_num_strings(self, line_num, lines, is_undo = False):
        """
        Inserts, in order, the inputted lines at the specified index

        @param          Line_num; string representation of inputted line number 
        @param          Lines; the list of line strings to be inserted
        @return         None
        @complexity     O(m*n) for both best and worst case, where n is the length of text_lines and m is the length of lines
        @postcondition  text_lines will contain, in order, the lines at the specified index.
        """
        
        # An input value was given, attempt to parse it and delete
        # Calculate index, ensure not 0
        num = int(line_num.strip())
        if num == 0:
            raise IndexError()

        i = num if num < 0 else num - 1
        
        # Insert the lines into their positions, however, since
        # insert places the element before, it shuffles the remaining
        # items down, we want to insert the lines stepping forward,
        # each time increasing the insert index by 1. This will ensure
        # the number of elements which must be shuffled up to make
        # space is constant. Thus the time complexity will be O(m*n)
        # instead of O(m*(n+m)) where n is the number of elements past
        # the index and m is the size of lines.    Note; when using
        # negative indices, elements are inserted after, hence the
        # index at which we insert is constant
        for j in range(len(lines)):
            pos = i if num < 0 else j + i
            self.text_lines.insert(pos, lines[j].replace('\n', ''))    # Ensure new-line characters are removed for consistency

        if not is_undo:
            # Create a command list and store information required for undo
            cmd = Command('delete', line_num, len(lines))

            # Push the command to the command stack
            self.cmd_stack.push(cmd);

    def search_string(self, query):
        """
        Searches through the list of lines to find all lines which contain the query term, returns their line numbers.

        @param          Query; the query term which to search for, case sensitive.
        @return         Returns a list (ListADT) of all line numbers whose lines contain the query term
        @complexity     O(n*m) for best - single or no match, and O(n*m^2) for worst case - each character matches first of query,
                        where n is the length of text_lines and m is the average length of each line
        @precondition   The provided query is not an empty string
        @postcondition  line_nums will contain all the line numbers of lines which contain the query term at least once, case sensitive.
        """

        # Define the length of the query as a variable
        n = len(query);

        # Ensure the query isn't empty
        if n == 0:
            raise ValueError('Invalid query.')

        # Initialize a list to store line numbers
        line_nums = task2.ListADT()

        # Iterate over each line, and search for the query term in the
        # line. If it exists within the line, append the line number to
        # the line_nums list. This will be returned and used to print
        # the relevant lines
        for i in range(len(self.text_lines)):
            # Get line contents
            line = self.text_lines[i]
            matches = task2.ListADT()
            match = False

            # Define the length of the line as a variable
            m = len(line)
            
            # Iterate over each character in the line, compare with the query
            for j in range(m):
                # If a match has already been found on this line, don't keep looking
                # the index will already be added to the line number list
                if match:
                    break

                # If the character in the line matches the beginning of our query,
                # save the index as a possible match
                if line[j] ==  query[0]:
                    matches.insert(-1, j)
                
                # For each possbile query match, ensure it is still a valid match,
                # the reason we store all matches as opposed to just keeping track
                # of the latest match is because we may miss some instances. For
                # example;    finding 'nnot' in the line 'nnnot' would not work
                # if we did not keep track of every possible match's start index.
                # The reason we loop backwards through matches is purely to improve
                # time complexity. Assuming some matches may need to be deleted, we
                # want to delete the ones at the back first, this will reduce the
                # number of elements that require shuffling for matches earlier in
                # the matches list.
                k = len(matches)
                while k > 0:
                    # Calculate the character index in the query
                    l = j - matches[k - 1]

                    # Check if each character in the sequence is the same, if not
                    # reset k to 0 and restart the sequence and check if the first
                    # characters match, perhaps starting the sequence again
                    if line[j] != query[l]:
                        matches.delete(k - 1)
                        k -= 1
                        continue

                    # If a sequence of characters, with length n, is found to be the
                    # same then there is a match. Add the line number and end the loop.
                    if l + 1 == n:
                        matches.delete(k - 1)
                        match = True
                        line_nums.append(i + 1)     # Line number = index + 1
                        break

                    # Decrement the index for matches
                    k -= 1

        # Return the list of line numbers where the query was found
        return line_nums

    def undo(self):
        """
        Gets the complementary commmand from the top of the command stack and undoes the last insert/delete command

        @param          None
        @return         None
        @complexity     O(m*n) for both best and worst case, where n is the length of text_lines and m is the length of lines
                        to be inserted or deleted.
        @postcondition  text_lines will be restored to its state before the execution of the insert/delete command being undone.
        """
        
        # If there are no commands to undo, raise exception
        if self.cmd_stack.is_empty():
            raise IndexError('Stack is empty.')

        # Get the command which must be undone
        cmd = self.cmd_stack.pop()

        # Execute command
        if cmd.cmd == 'delete':
            # Delete each line that was inserted
            for _ in range(cmd.data):
                self.delete_num(cmd.arg, True)

        elif cmd.cmd == 'insert':
            # Insert each line that was deleted
            self.insert_num_strings(cmd.arg, cmd.data, True)

        else:
            raise ValueError('Unknown complementary command.')

    
    def poll_user(self):

        # Print the menus
        print('Menu:')
        print('  read   file_name')
        print('  print  line_num')
        print('  delete line_num')
        print('  insert line_num')
        print('  search fnd_term')
        print('  undo')
        print('  quit')
        print('')

        try: 
            # Get user input and parse
            user_input = input(">> ") + ' '              # Get user input and strip the whitespace, but ensure it always ends with whitespace
            index = user_input.index(' ')                # Get the index of the first space, will be the end of the string if no arg is given
            end = len(user_input) - 1                    # Enter will add a space at the end of the search term, remove this space
            cmd = user_input[:index].strip().lower()     # Everything from the start to the first space is the command, convert to lower case
            arg = user_input[index+1:end]                # Everything from the first space is the argument, this can be nothing once stripped

            # Execute given command, not case sensitive to command
            if cmd == 'read' or cmd == 'r' or cmd == 'load' or cmd == 'l':              
                self.read_filename(arg.strip())                  # Read can be called by the commands; 'read', 'r', 'load' and 'l'
                                                            # Read requires a file name to provided as the argument

            elif cmd == 'print' or cmd == 'p':           # Print can be called by the command 'print' or 'p'
                self.print_num(arg.strip())                         # Print has an optional line number as the argument

            elif cmd == 'delete' or cmd == 'd':          # Delete can be called by the command 'delete' or 'd'
                self.delete_num(arg.strip())                        # Delete has an optional line number as the argument

            elif cmd == 'insert' or cmd == 'i':          # Insert can be called by the command 'insert' or 'i'
                self.insert_num(arg.strip())                        # Insert requires a line number to provided as the argument

            elif cmd == 'search' or cmd == 's':          # Search can be called by the command 'search' or 's'
                nums = self.search_string(arg)              # Search requires a search term to provided as the argument
                
                # Print lines
                for i in range(len(nums)):
                    print('  ' + str(nums[i]))

            elif cmd == 'undo' or cmd == 'u':            # Undo can be called by the command 'undo' or 'u'
                self.undo()                                 # No argument required

            elif cmd == 'quit' or cmd == 'exit' or cmd == 'q' or cmd == 'e':
                # False indicates exit requested         #  Quit can be called by the commands; 'quit', 'q', 'exit' and 'e'
                return False                                # No Argument required

            else:                                        # Inputted command is not a known command or action
                print('?')
        except:
            # Invalid argument
            print('?')

        # True indicates exit not requested
        return True

    ### END EDITOR CLASS ###



if __name__ == '__main__':
    ed = Editor()
    while ed.poll_user():
        print('')