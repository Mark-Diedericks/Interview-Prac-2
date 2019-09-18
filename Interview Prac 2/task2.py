"""
Array-based implementation of the List Abstract Data Type, dyanmic capacity.

@author         Mark Diedericks 30572738
@since          17/09/2019
@modified       17/09/2019
"""

import math

class ListADT:
    def __init__(self, size = 100):
        """
        Instantiates a new instance of the ListADT class with a specified capacity, size.

        @param          Size; the capcity of the list or 100 by default; must always be 40 or above
        @return         None
        @complexity     O(1) for both best and worst case.
        @postcondition  An empty list with capacity size is instantiated.
        """
        self.length = 0
        self.the_array = [None] * max(40, size)
    
    def __str__(self):
        """
        Returns a string representation of the list, with one element per line

        @param          None
        @return         String representation of the lit
        @complexity     O(n) for both best and worst case
        """
        res = ""

        # Loop through each element and append it as a line to the final string
        for i in range(self.length):
            res += str(self.the_array[i])
            res += '\n'

        return res

        
    def __len__(self):
        """
        Returns the length of the list; self.length

        @param          None
        @return         Length of the list
        @complexity     O(1) for both best and worst case
        """
        return self.length
        
    def __getitem__(self, index):
        """
        Returns the element in the list at index

        @param          None
        @return         The item contained at index in the list
        @complexity     O(1) for both best and worst case
        @precondition   The index is within then list bounds; -self.length <= index <= self.length-1
        @exception      Index is out of bounds 
        """

        # Enforce index bounds
        if index < -self.length or index >= self.length:
            raise IndexError('Index out of bounds')

        # Calculate index, account for negative indexing
        i = self.length + index if index < 0 else index

        return self.the_array[i]
        
    def __setitem__(self, index, item):
        """
        Set the element in the list at index

        @param          None
        @return         None
        @complexity     O(1) for both best and worst case
        @precondition   The index is within then list bounds; -self.length <= index <= self.length-1
        @exception      Index is out of bounds 
        @postcondition  The element located at the index will be item
        """

        # Enforce index bounds
        if index < -self.length or index >= self.length:
            raise IndexError('Index out of bounds')

        # Calculate index, account for negative indexing
        i = self.length + index if index < 0 else index

        self.the_array[i] = item
        
    def __eq__(self, other):
        """
        Checks whether or not the list is equal to the other object

        @param          Other; another object to compare against the list
        @return         True if other is a ListADT type with the same elements as this list, otherwise False
        @complexity     O(1) for best case - different type/length, O(n) for worst case - check elements, where n is elf.length
        """

        # Ensure that other is of type ListADT
        if not isinstance(other, ListADT):
            return False

        # Ensure the lists have the same length
        # Capacity can be different between the two
        if self.length != len(other):
            return False

        # Ensure the elements are the same
        for i in range(self.length):
            if self.the_array[i] != other[i]:
                return False

        return True
        
    def __contains__(self, item):
        """
        Checks whether or not an item is contained within the list.

        @param          Item; the item whose existance within the list is being checked
        @return         True if item is in the list, otherwise false
        @complexity     O(n) for both best and worst case, where n is self.length
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False
        
    def insert(self, index, item):
        """
        Inserts the item at the index from the list, shuffliing next elements up

        @param          Index; the position at which to insert the item
        @param          Item; the value to be inserted at index
        @return         None
        @complexity     O(1) for best case - last element, and O(n) and worst case - first element, where n is self.length
        @precondition   The list is not full
        @precondition   The index is within then list bounds; -self.length <= index <= self.length-1
        @exception      Appending item to a full list
        @exception      Index is out of bounds 
        @postcondition  The list will contain the item at index and the lenth will be increased by 1
        """

        # Ensure the list isn't full
        if self.is_full():
            self.enforce_size()

        # Enforce index bounds
        if index < -self.length-1 or index > self.length:
            raise IndexError('Index out of bounds')

        # Calculate index, account for negative indexing
        i = self.length + index if index < 0 else index

        # Shuffle elements with from position i up to make space for new item to be inserted at position i
        for j in range(self.length, i, -1):
            self.the_array[j] = self.the_array[j - 1]
        
        # Increment the length
        self.length += 1

        # Get the item at the index
        self.the_array[i] = item 

        #Enforce size rules for the list
        self.enforce_size()
        
    def delete(self, index):
        """
        Removes the item at the index from the list

        @param          Index; the position of the item to remove
        @return         The item at the index, being removed.
        @complexity     O(1) for best case - last element, and O(n) and worst case - first element, where n is self.length
        @precondition   The index is within then list bounds; -self.length <= index <= self.length-1
        @exception      Index is out of bounds 
        @postcondition  The list will no longer contain the item at index and the lenth will be decreased by 1
        """

        # Enforce index bounds
        if index < -self.length or index >= self.length:
            raise IndexError('Index out of bounds')

        # Calculate index, account for negative indexing
        i = self.length + index if index < 0 else index

        # Get the item at the index
        item = self.the_array[i]

        # Shuffle elements with position greater than i down to remove item at position i
        for j in range(i, self.length - 1):
            self.the_array[j] = self.the_array[j + 1]

        # Decrement the length
        self.length -= 1

        #Enforce size rules for the list
        self.enforce_size(True)

        return item
        
    def is_empty(self):
        """
        Checks whether or not the list contains any elements.

        @param          None
        @return         False if list contains elements, otherwise true
        @complexity     O(1) for both best and worst case.
        """
        return self.length == 0
        
    def is_full(self):
        """
        Checks whether or not the list has reached it's size capcity

        @param          None
        @return         True if length is the same as the capcity, otherwise false
        @complexity     O(1) for both best and worst case.
        """
        return self.length == len(self.the_array)
        
    def append(self, item):
        """
        Adds an item to the rear of the lisd
        @param          Item; the item to be added to the list
        @return         None
        @complexity     O(1) for both best and worst case
        @precondition   The list is not full
        @exception      Appending item to a full list
        @postcondition  The list will contain the item at the rear
        """
        if self.is_full():
            #Enforce size rules for the list
            self.enforce_size()

        # Add the item to the end of the list
        self.the_array[self.length] = item
        self.length += 1

        #Enforce size rules for the list
        self.enforce_size()
        
    def enforce_size(self, shrink = False):
        """
        Enforces the resizing rules associated with the list's capacity;
        capacity must be 40 or above
        capacity should be multiplied by 1.9 when list becomes completely full (rounded up)
        capacity should be multiplied by 0.5 when list becomes less than 1/4 full (rounded up)
        Should be called when appending, deleting or inserting an item, not when instantiating a list.

        @param          Shrink; indicates that a list operating resulting in a decrease in list length has occured, avoids resizing a new list to the minimum of 40
        @return         None
        @complexity     O(1) for best - no resizing condition met, and O(n) worst case - resizing condition met, where n is self.length
        @exception      Will ensure the list capacity is 40 or above, less than or equal 4 times the length and greater than the length of the list
        @postcondition  The list will not be full, it's capacity will be greater than length but less than or equal to length*4
        """
        arr_size = len(self.the_array)
        new_size = arr_size

        if self.is_full():
            # Calculate new size; 1.9*old_size rounded up
            # Casting to an int will always round down, so add one to round up
            new_size = math.ceil(arr_size * 1.9)
        elif self.length * 4 < max(40, arr_size) and shrink:
            # Calculate new size; 0.5*old_size rounded up
            # Casting to an int will always round down, so add one to round up
            new_size = math.ceil(arr_size * 0.5)
        elif arr_size < 40:
            new_size = 40
        else:
            # Neither conditions for resizing are met so skip resizing
            return

        # Store the old array and create a new array of the larger size
        old_array = self.the_array;
        self.the_array = [None] * max(40, new_size)
        
        # Copy the items from the old array into the current array
        for i in range(self.length):
            self.the_array[i] = old_array[i];

        
    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')
			
        self.the_array = array
        self.length = length
