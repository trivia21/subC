import unittest
import os.path

from manipulate import companyData, print_result

class ManipulateTestCases(unittest.TestCase):
   """ Test cases for `mani.py` """

   def test_dataFile(self):
      """ Check if the file exsists"""
      self.assertTrue(os.path.isfile("data.csv"))

   def test_if_returnList_isEmpty(self):
      """ Check the return list it should not be empty"""
      self.assertTrue(len(companyData("data.csv")))

   def test_no_companies_wmaxPrice(self):
      """No. of companies in return data should be 4"""
      No_of_Companies_WMaxPrice = 4
      self.assertTrue(len(companyData("data.csv")) == No_of_Companies_WMaxPrice)

   def test_print(self):
      print_result("data.csv")


if __name__ == '__main__':
   unittest.main()