import math
import unittest
from test_common import *
import task2
import task5

class TestTask5(unittest.TestCase):
  def test_search(self):
    ed = task5.Editor()
    ed.read_filename('TestFile.txt')
    
    queries = [ ("is a", [1, 2]), # Multi-word
                ("is", [1, 2]) ]  # Multiple occurrences
    for query, lines in queries: 
      ed_lines = ed.search_string(query)
      self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))


    # MY TESTING
    ed = task5.Editor()
    ed.read_filename('1984.txt')
    
    # Find all occurances of 'He had a' in 1984 by George Orwell (1984.txt)
    query = 'He had a'
    lines = [337, 2045, 2758, 3235, 3571, 5217, 7374, 7377, 8117, 9741]
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))
    
    # Find all occurances of 'George Orwell' in 1984 by George Orwell (1984.txt)
    query = 'George Orwell'
    lines = [8, 33]
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))


    ed = task5.Editor()
    ed.read_filename('small.txt')
    
    # Find all occurances of 'not' in small.txt
    query = 'not'
    lines = [2, 3]
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))
    
    # Find all occurances of 'not ' in small.txt
    query = 'not '
    lines = [2]
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))

    # Check for recognition of 'abc' in 'aaabccc' and not 'abc ' in 'aaabccc'
    ed = task5.Editor()
    ed.insert_num_strings('1', ToListADT(task2.ListADT, ["aaabccc"]));

    query = 'abc'
    lines = [1]
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))

    query = 'abc '
    lines = []
    ed_lines = ed.search_string(query)
    self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))


if __name__ == '__main__':
  unittest.main()
