import math
import unittest
from test_common import *
import task2
import task3
import task6

small_content = ["Yossarian decided",
                "not to utter",
                "another word."]

small2_content = ["Line 1",
                  "Line 2",
                  "Line 3",
                  "Line 4"]

class TestTask6(unittest.TestCase):
  def test_undo(self):
    ed = task6.Editor()
    
    extra_lines = [ "These are some extra lines.", "They are will be added to the string." ]

    ed.read_filename('TestFile.txt')
    ed.delete_num("")
    ed.insert_num_strings("1", ToListADT(task2.ListADT, extra_lines))

    ed.undo()
    self.assertTrue(equal_lines(ed, []))
    ed.undo()
    self.assertTrue(equal_lines(ed, test_content))
    with self.assertRaises(Exception, msg = "Undoing past the beginning of history should have failed."):
      ed.undo()


    # MY TESTING
    # Undo an insert at positive index
    ed.read_filename('small.txt')
    ed.insert_num_strings("2", ToListADT(task2.ListADT, extra_lines))
    ed.undo()
    self.assertTrue(equal_lines(ed, small_content), msg =  "Incorrect handling of positive insert undo")

    # Undo an insert at negative index
    ed.read_filename('small.txt')
    ed.insert_num_strings("-2", ToListADT(task2.ListADT, extra_lines))
    ed.undo()
    self.assertTrue(equal_lines(ed, small_content), msg =  "Incorrect handling of negative insert undo")

    # Undo an empty insert
    ed.read_filename('small.txt')
    ed.insert_num_strings("-2", task2.ListADT())
    ed.undo()
    self.assertTrue(equal_lines(ed, small_content), msg =  "Incorrect handling of empty insert undo")
    
    # Undo an delete at positive index
    ed.read_filename('small.txt')
    ed.delete_num('1')
    ed.undo()
    self.assertTrue(equal_lines(ed, small_content), msg =  "Incorrect handling of positive delete undo")

    # Undo an delete at negative index
    ed.read_filename('small.txt')
    ed.delete_num('-1')
    ed.undo()
    self.assertTrue(equal_lines(ed, small_content), msg =  "Incorrect handling of negative delete undo")

    # Undo entire file delete, of large file; 1984
    ed.read_filename('1984.txt')
    loaded_lines = task3.read_text_file('1984.txt')

    ed.delete_num('')
    ed.undo()
    self.assertTrue(ed.text_lines == loaded_lines, msg =  "Incorrect handling of full delete undo")


if __name__ == '__main__':
  unittest.main()
