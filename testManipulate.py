import unittest
import os.path

from manipulate import companyData

class ManipulateTestCases(unittest.TestCase):
   """ Test cases for `mani.py` """
   def setUp(self):
        self.No_of_Companies_WMaxPrice = 4

   def test_for_data_file_printOutput(self):
      """ Check if the file exsists and print result in formated way"""
      desoutput = companyData("data.csv")
      print "\n"+"Company:"+"\t"+"MonYear, "+"MaxPrice"
      print "---------------------------------"
      for company,data in desoutput.items():
         for value in data:
            print company+":\t\t"+', '.join(value.split())
      self.assertTrue(os.path.isfile("data.csv"))

   def test_if_returnList_isEmpty(self):
      """ Check the return list it should not be empty"""
      self.assertTrue(len(companyData("data.csv")))

   def test_no_companies_wmaxPrice(self):
      """No. of companies in return data should be 4"""
      self.assertTrue(len(companyData("data.csv")) == self.No_of_Companies_WMaxPrice)

   


if __name__ == '__main__':
   unittest.main()