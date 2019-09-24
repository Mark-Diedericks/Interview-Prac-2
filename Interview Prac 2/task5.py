"""
ListADT based implementation of a line based editor,
task5 functionality is coded directly into task4's Editor
class as suggested by Graeme;
https://lms.monash.edu/mod/forum/discuss.php?d=1740300

@author         Mark Diedericks 30572738
@since          23/09/2019
@modified       23/09/2019
"""

from task4 import Editor

if __name__ == '__main__':
    ed = Editor()
    while ed.poll_user():
        print('')