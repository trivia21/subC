import csv
""" Function returns List for each Company year and
    month in which the share price was highest"""
def companyData(fname):
   rownum = 0
   desoutput = {}
   """Open the CSV file to read, format and manipulate the data"""
   with open(fname,"rb") as my_file:
      reader = csv.reader(my_file)
      for row in reader:
         colnum = 0
         if rownum == 0:
            header = row[2:]
            rownum+=1
         else:
            MP_finYrMonth=row[1]+row[0]
            for price in row[2:]:
               if colnum == 0:
                  max_price = price
                  company = header[colnum]
               else:
                  if price > max_price:
                     max_price = price
                     company = header[colnum]
               colnum+=1
            MP_finYrMonth+=" "+max_price
            if company not in desoutput:
               desoutput[company] = [MP_finYrMonth]
            else:
               desoutput.get(company).append(MP_finYrMonth)
   return desoutput

"""Prints result from function 'compantData' in a readble format"""
def print_result(fname):
   desoutput = companyData(fname)
   print "\n"+"Company:"+"\t"+"MonYear, "+"MaxPrice"
   print "---------------------------------"
   for company,data in desoutput.items():
      for value in data:
         print company+":\t\t"+', '.join(value.split())

 


