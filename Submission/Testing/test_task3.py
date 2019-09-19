import math
import unittest
from Testing.test_common import *
import task2
import task3

class TestTask3(unittest.TestCase):
  def test_read_file(self):
    #test_lines = task3.read_text_file('TestFile.txt')
    #self.assertEqual([ l.strip('\n') for l in ToList(test_lines) ], test_content, msg = "File not correctly read.")
    
    l = task2.ListADT()
    l.append('Yossarian decided\n')
    l.append('not to utter\n')
    l.append('another word.')
    self.assertTrue(task3.read_text_file('small.txt') == l)
    
    l = task2.ListADT()
    l.append('Line 1\n')
    l.append('Line 2\n')
    l.append('Line 3\n')
    l.append('Line 4')
    self.assertTrue(task3.read_text_file('small2.txt') == l)
    
if __name__ == '__main__':
  unittest.main()
