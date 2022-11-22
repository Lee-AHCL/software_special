import unittest 
from csvprinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    
  
    def test_read1(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))
        
    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual(" bbb2", line[1][1])
        
    def test_read3(self):
        try:
            printer = CSVPrinter("sample3.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except Exception as e: 
            raise Exception  
            
        
        
c = TestCSVPrinter() 
c.test_read1()
c.test_read2()
c.test_read3() 
