import unittest
import os.path

from manipulate import print_companyData

class ManipulateTestCases(unittest.TestCase):
   """ Test cases for `mani.py` """
   
   def test_for_data_file(self):
      """ Check if the file exsists"""
      self.assertTrue(os.path.isfile("data.csv"))

   def test_if_returnList_isEmpty(self):
      """ Check the return list it should not be empty"""
      self.assertTrue(len(print_companyData("data.csv")))

   


if __name__ == '__main__':
   unittest.main()