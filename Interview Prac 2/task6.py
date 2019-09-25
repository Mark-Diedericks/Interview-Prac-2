"""
ListADT based implementation of a line based editor,
task6 functionality is coded directly into task4's Editor
class as suggested by Graeme;
https://lms.monash.edu/mod/forum/discuss.php?d=1740300

@author         Mark Diedericks 30572738
@since          23/09/2019
@modified       24/09/2019
"""


from task4 import Editor
from task4 import StackADT

if __name__ == '__main__':
    ed = Editor()
    while ed.poll_user():
        print('')


