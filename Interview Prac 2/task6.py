"""
ListADT based implementation of a line based editor,
task6 functionality is coded directly into task4's Editor
class as suggested by Graeme;
https://lms.monash.edu/mod/forum/discuss.php?d=1740300

@author         Mark Diedericks 30572738
@since          23/09/2019
@modified       23/09/2019
"""

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
        return self.top == None

    def push(self, item):
        n = Node(self.top, item)
        self.top = n

    def pop(self)
        if is_empty():
            raise IndexError('Stack is empty')
        
        n = self.top
        self.top = n.next

        return n

    ### END STACK CLASS ###



from task4 import Editor

if __name__ == '__main__':
    ed = Editor()
    while ed.poll_user():
        print('')


