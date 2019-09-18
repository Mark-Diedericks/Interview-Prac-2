"""
ListADT based implementation of a line based editor

@author         Mark Diedericks 30572738
@since          18/09/2019
@modified       18/09/2019
"""

class Editor:
    def __init__(self):
        raise NotImplementedError

    def read_filename(self, file_name):
        raise NotImplementedError
        
    def print_num(self, line_num):
        raise NotImplementedError

    def delete_num(self, line_num):
        raise NotImplementedError

    def insert_num(self, line_num, lines):
        raise NotImplementedError

    def search_string(self, query):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
