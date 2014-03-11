import unittest
import os.path

from manipulate import companyData, print_result

class ManipulateTestCases(unittest.TestCase):
   """ Test cases for `mani.py` """
   
   def setUp(self):
      self.desoutput = companyData("data.csv")

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
   
   def test_expected_result_Honda(self):
      Honda = ['Feb1990 9']
      self.assertEqual(self.desoutput.get("Honda"),Honda)

   def test_expected_result_Maruti(self):
      Maruti = None
      self.assertEqual(self.desoutput.get("Maruti"),Maruti)
   
   def test_expected_result_Duster(self):
      Duster = ['Mar2014 90']
      self.assertEqual(self.desoutput.get("Duster"),Duster)

   def test_expected_result_Hyundai(self):
      Hyundai = None
      self.assertEqual(self.desoutput.get("Hyundai"),Hyundai)

   def test_expected_result_Fiat(self):
      Fiat = ['Jan1990 5']
      self.assertEqual(self.desoutput.get("Fiat"),Fiat)

   def test_expected_result_Tata(self):
      Tata = ['Jan2014 99']
      self.assertEqual(self.desoutput.get("Tata"),Tata)
      

   def test_print(self):
      print_result("data.csv")

  


if __name__ == '__main__':
   unittest.main()