import math
import unittest
from test_common import *
import task2
import task4

small_content = ["Yossarian decided",
                "not to utter",
                "another word."]

small2_content = ["Line 1",
                  "Line 2",
                  "Line 3",
                  "Line 4"]

class TestTask4(unittest.TestCase):
  def test_read(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    self.assertTrue(equal_lines(ed, test_content), msg =  "File not correctly read.")

  def test_print(self):
    pass

  def test_delete(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    ed.delete_num("1")
    self.assertTrue(equal_lines(ed, test_content[1:]), msg =  "Failed to delete first line.")
   
    for index in ["-5"]:
      with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail."):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)


    # MY TESTING
    # Delete all lines should have an empty list
    ed.delete_num('')
    self.assertEqual(len(ed.text_lines), 0, 'Did not delete all lines')

    # Delete frome empty editor
    with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail, empty editor."):
        ed.delete_num('5')

    # Delete last line with positive index
    ed.read_filename('small.txt')
    ed.delete_num('3')
    self.assertTrue(equal_lines(ed, small_content[:2]), msg =  "Failed to delete last line, positive index.")

    # Delete last line with negative index
    ed.read_filename('small.txt')
    ed.delete_num('-1')
    self.assertTrue(equal_lines(ed, small_content[:2]), msg =  "Failed to delete last line, positive index.")


  def test_insert(self):
    ed = task4.Editor()
    ed.insert_num_strings("1", ToListADT(task2.ListADT, [test_content[0]]))
    self.assertTrue(equal_lines(ed, [test_content[0]]), msg =  "Failed to insert single line.")

    ed = task4.Editor()
    ed.insert_num_strings("-1", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))
    self.assertTrue(equal_lines(ed, [test_content[2], test_content[3]]), msg =  "Incorrect handling of negative insertion")


    # MY TESTING
    # Insert at end with positive index
    ed = task4.Editor()
    ed.read_filename('small.txt')
    ed.insert_num_strings("4", ToListADT(task2.ListADT, [small2_content[2], small2_content[3]]))
    self.assertTrue(equal_lines(ed, small_content + [small2_content[2], small2_content[3]]), msg =  "Incorrect handling of positive insertion")
    
    # Insert at end with negative index
    ed = task4.Editor()
    ed.read_filename('small.txt')
    ed.insert_num_strings("-1", ToListADT(task2.ListADT, [small2_content[2], small2_content[3]]))
    self.assertTrue(equal_lines(ed, small_content + [small2_content[2], small2_content[3]]), msg =  "Incorrect handling of negative insertion")

    # Insert at start
    ed = task4.Editor()
    ed.read_filename('small.txt')
    ed.insert_num_strings("1", ToListADT(task2.ListADT, [small2_content[2], small2_content[3]]))
    self.assertTrue(equal_lines(ed, [small2_content[2], small2_content[3]] + small_content), msg =  "Incorrect handling of inserting at start")

    # Insertb at 0 should error
    ed = task4.Editor()
    with self.assertRaises(IndexError, msg = "Inserting out-of-bounds lines should fail, 0 index."):
        ed.insert_num_strings('0', ToListADT(task2.ListADT, [small2_content[2], small2_content[3]]))

    
if __name__ == '__main__':
  unittest.main()
