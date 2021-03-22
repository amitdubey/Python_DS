import download_large_file_split as dl
import mean_media_class as mc
import performance_testing_function as pt
import pandas as pd

# Python code to demonstrate working of unittest 
import unittest 
from pandas.core.dtypes.common import is_numeric_dtype

l =  pd.DataFrame(data=None)

class TestMethods(unittest.TestCase): 
    def setUp(self): 
        pass
    '''Generic test regarding file data types, length and empty values'''
    def test_is_file_has_numbers_median(self):	
        self.assertEqual(is_numeric_dtype(m2.l),False) 
       
    def test_is_file_has_numbers_mean(self):	
        self.assertEqual(is_numeric_dtype(m1.l),False) 
        #with self.assertRaises(TypeError): 
        print(m1.l)
	# Returns True if the string contains 4 a. 
    def test_zero_length(self): 
        self.assertEqual(len(m1.l),505) 
     
	# Returns True if the mean is equal to 1 for single element 1. 
    def test_mean(self):
        self.assertEqual(m1.mean1(),3184.2657425742573)
        print(m1.mean1()) 
    
    def test_mean(self):
        self.assertEqual(m1.mean2(),3184.2657425742573) 
        print(m1.mean2())
    def test_mean(self):
        self.assertEqual(m1.mean3(),3184.2657425742573)
        print(m1.mean3()) 
    def test_mean(self):
        self.assertEqual(m1.mean4(),3184.2657425742577)
        print(m1.mean4()) 
    # def test_mean(self):
    #     self.assertEqual(m1.mean5(),[3184.26574257])
    #     print(m1.mean5) 
	# #return True if the  
    # def test_ODD_even_element_mean(self):		 
	#     self.assertEqual(len(m2.l)//2,0) 
    #  #''' Test cases for median value'''
    
	# Returns True if the string contains zero elements. 
    def test_zero_length_median(self): 
        self.assertEqual(m2.median1(),[3115.3])
        print (m2.median1())
    def test_zero_length_median(self): 
        self.assertEqual(m2.median2(),[3115.3])
        print (m2.median2()) 
    def test_zero_length_median(self): 
        self.assertEqual(m2.median3(),[3115.3])
        print (m2.median3()) 
    def test_zero_length_median(self): 
        self.assertEqual(m2.median4(),[3115.3])
        print (m2.median4()) 
    # def test_zero_length_median(self): 
    #     self.assertEqual(m2.median5(),[3115.3]) 
    #     print (m2.median5()) 

	# Returns True if the mean is equal to 1 for single element 1. 
    def test_one_element_median(self):		 
	    self.assertEqual(len(m1.l),505) 

	
    

if __name__ == '__main__': 
    d1 = dl.downloadHistoryStockData()
    result =d1.downloadfile(dl.number_of_chunks, dl.STOCK_NAME, dl.START_DATE, dl.END_DATE, dl.INTERVAL, dl.FOLDER_LOCATION)
    t =TestMethods()
    t.l=result
    m1 = mc.Mean()
    m2 =mc.Median()
    m1.l = result
    m2.l =result
    
    unittest.main() 
