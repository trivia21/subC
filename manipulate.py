import csv
def print_companyData(fname):
   rownum = 0
   company= ""
   max = 0
   desoutput = {}
   try:
      f = open(fname,"rb")
      reader = csv.reader(f)
      
      for row in reader:
         colnum = 0
         if rownum == 0:
            header = row[2:]
            rownum+=1
         else:
            finYrMonth=row[0]+row[1]
            for col in row[2:]:
               if colnum == 0:
                  max = col
                  company = header[colnum]
               else:
                  if col > max:
                     max = col
                     company = header[colnum]
               colnum+=1
            if company not in desoutput:
               desoutput[company] = [finYrMonth]
            else:
               desoutput.get(company).append(finYrMonth)       
   finally:
      f.close()
      print '/n'
      print desoutput
      return desoutput


