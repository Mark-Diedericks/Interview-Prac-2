import math
import unittest
from Testing.test_common import *
import task1

class TestTask1(unittest.TestCase):
  # Check that initialisation doesn't fail
  def test_init(self):
    y = task1.ListADT(10)

  def test_str(self):
    # Check str for non-empty lists
    x = task1.ListADT(10)
    append(x, [1, 2, 3])
    self.assertEqual(str(x).strip('\n'), '1\n2\n3')

    # MY TESTING
    # Check str for non-empty lists
    x = task1.ListADT(10)
    append(x, ['A', 'B', 'C'])
    self.assertEqual(str(x).strip('\n'), 'A\nB\nC')
    # Check str for non-empty lists
    x = task1.ListADT(10)
    append(x, [5, 4, 3, 2, 1])
    self.assertEqual(str(x).strip('\n'), '5\n4\n3\n2\n1')

  def test_len(self):
    # Test length of an empty list
    x = task1.ListADT(20)
    self.assertEqual(len(x), 0, msg="Length of empty list should be 0")
    # And for a non-empty one
    x.insert(0, 2)
    self.assertEqual(len(x), 1, msg="Length should be 1")

    # MY TESTING
    #Test length of 3
    x.append(3)
    x.append(4)
    self.assertEqual(len(x), 3, msg="Length should be 3")
    #Test length of 2
    x.delete(2);
    self.assertEqual(len(x), 2, msg="Length should be 2");

  def test_get(self):
    x = task1.ListADT(10)
    append(x, [0, 1, 2, 3, 4])
    
    # Check both positive and negative indices
    for index, value in [ (1, 1), (-2, 3)]:
      self.assertEqual(x[index], value, msg="Incorrect _getitem_.")

    # MY TESTING
    # Test negative indices
    x = task1.ListADT(10)
    append(x, [7, 6, 5, 4, 3])
    self.assertEqual(x[-2], 4, msg="Incorrect _getitem_.")
    # Test positive indices
    x = task1.ListADT(10)
    append(x, [7, 6, 5, 4, 3])
    self.assertEqual(x[2], 5, msg="Incorrect _getitem_.")
    # Test out of bounds indices
    x = task1.ListADT(10)
    append(x, [7, 6, 5, 4, 3])
    with self.assertRaises(IndexError):
        x[10]


  def test_set(self):
    x1 = task1.ListADT(10)
    append(x1, [1, 2, 3])
    # Testing assignment (and implicitly _getitem_)
    x1[0] = 8
    self.assertTrue(equal(x1, [8, 2, 3]), msg = "Incorrect assignment at index 0")

    # MY TESTING
    # Test negative indices
    x1[1] = 7
    self.assertEqual(x1[1], 7, msg="Incorrect assignment at index 1.")
    # Test positive indices
    x1[-1] = 5
    self.assertEqual(x1[-1], 5, msg="Incorrect assignment at index -1.")
    # Test out of bounds indices
    with self.assertRaises(IndexError):
        x1[10] = 3;


  def test_eq(self):
    x1 = task1.ListADT(10)
    x2 = task1.ListADT(20)
    # Check equality for lists of different size
    self.assertTrue(x1 == x2, msg =  "Lists with different capacity should still be equal.")
    # Check that equality tests for List type.
    append(x1, [1, 2, 3])
    self.assertFalse(x1 == [1, 2, 3], "Equality test doesn't check type.")

    # MY TESTING
    # Check values
    append(x2, [7, 8, 9])
    self.assertFalse(x1 == x2, "Equality doesn't check values")
    # Check type
    self.assertFalse(x2 == [7, 8, 9], "Equality doesn't check type")
    # Ensure same
    x1 = task1.ListADT(10)
    x2 = task1.ListADT(20)
    append(x1, [1, 2, 3])
    append(x2, [1, 2, 3])
    self.assertTrue(x1 == x2, "Equality not matching values")

  def test_insert(self):
    x = task1.ListADT(10)
    # Check insertion at beginning
    x.insert(0, 1)
    self.assertTrue(equal(x, [1]), msg =  "Insertion in empty list failed")
    # And at end.
    x.insert(1, 2)
    self.assertTrue(equal(x, [1, 2]), msg =  "Insertion at end failed")

    # Check insertion out-of-bounds
    with self.assertRaises(IndexError, msg = "Inserting out of bounds should fail"):
      x.insert(6, 8)

    with self.assertRaises(Exception, msg = "Inserting above capacity should raise an exception."):
      append(x, [1 for i in range(20) ])

    # MY TESTING
    x = task1.ListADT(10)
    append(x, [1 for i in range(10)])
    self.assertTrue(equal(x, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

    x1 = task1.ListADT(10)
    append(x1, [1, 2, 3])
    x1.insert(1, 7)
    self.assertTrue(equal(x1, [1, 7, 2, 3]), "Insert with positive index not working")

    x1.insert(-1, 7)
    self.assertTrue(equal(x1, [1, 7, 2, 7, 3]), "Insert with negative index not working")

  def test_delete(self):
    x = task1.ListADT(10)
    append(x, [0,1,2,3,4,5])
    # Test deletion from the middle.
    x.delete(2)
    self.assertTrue(equal(x, [0,1,3,4,5]), msg =  "Delete from middle failed")
    # And from a negative index.
    x.delete(-4)
    self.assertTrue(equal(x, [0,3,4,5]), msg =  "Negative deletion failed")

    #MY TESTING
    x.delete(-1)
    self.assertTrue(equal(x, [0,3,4]), msg =  "Negative deletion failed")
    x.delete(0)
    self.assertTrue(equal(x, [3,4]), msg =  "Negative deletion failed")
    with self.assertRaises(IndexError):
        x.delete(3)

if __name__ == '__main__':
  unittest.main()
