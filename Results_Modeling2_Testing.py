# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:02:38 2020

@author: darak
"""

import unittest
import pandas as pd
from pandas._testing import assert_frame_equal
from Results_Modeling2 import *

class Results_Modeling2TestCase(unittest.TestCase):
    
    def test_cleanNumeric_comma(self):
        print("Testing: test_cleanNumeric_comma")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': ['15,000', '2500', '36,000', '180']})
        print("Starting DataFrame is: \n" + str(df))

        # Try cleaning dataframe
        cleaned = cleanNumeric(df, ['ID'])
        print("New DataFrame is: \n " + str(cleaned))

        # Check if dataframes match
        dfClean = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': [float(15000), float(2500), float(36000), float(180)]})
        print("Expected DataFrame is: \n " + str(dfClean))
        assert_frame_equal(cleaned, dfClean)
        
        
    def test_cleanNumeric_positive(self):
        print("Testing: test_cleanNumeric_positive")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': ['+15000', '+2500', '36000', '180']})
        print("Starting DataFrame is: \n" + str(df))

        # Try cleaning dataframe
        cleaned = cleanNumeric(df, ['ID'])
        print("New DataFrame is: \n " + str(cleaned))

        # Check if dataframes match
        dfClean = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': [float(15000), float(2500), float(36000), float(180)]})
        print("Expected DataFrame is: \n " + str(dfClean))
        assert_frame_equal(cleaned, dfClean)
        
        
    def test_cleanNumeric_percent(self):
        print("Testing: test_cleanNumeric_percent")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': ['15000', '2500%', '36000', '180%']})
        print("Starting DataFrame is: \n" + str(df))

        # Try cleaning dataframe
        cleaned = cleanNumeric(df, ['ID'])
        print("New DataFrame is: \n " + str(cleaned))

        # Check if dataframes match
        dfClean = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': [float(15000), float(2500), float(36000), float(180)]})
        print("Expected DataFrame is: \n " + str(dfClean))
        assert_frame_equal(cleaned, dfClean)
        
        
    def test_cleanNumeric_float(self):
        print("Testing: test_cleanNumeric_float")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': [str(15000), str(2500), str(36000), str(180)]})
        print("Starting DataFrame is: \n" + str(df))
        
        # Try cleaning dataframe
        cleaned = cleanNumeric(df, ['ID'])
        print("Cleaned DataFrame is: \n" + str(cleaned))

        # Check if dataframes match
        dfClean = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num': [float(15000), float(2500), float(36000), float(180)]})
        print("Expected DataFrame is: \n " + str(dfClean))
        assert_frame_equal(cleaned, dfClean)
        
        
    def test_divideDf_division(self):
        print("Testing: test_divideDf")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num1': [15000, 2500, 3600, 180],
                           'num2': [10000, 1000, 100, -100]})
        print("Starting DataFrame is: \n" + str(df))
        
        # Try dividing dataframe
        divided = divideDf(df, 'num1', 'num2')
        print("Divided DataFrame is: \n" + str(divided))

        # Check if dataframes match
        dfDiv = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num1': [15000, 2500, 3600, 180],
                           'num2': [10000, 1000, 100, -100],
                           'num1%': [150.0,250.0, 3600.0, -180.0]})
        print("Expected DataFrame is: \n " + str(dfDiv))
        assert_frame_equal(divided, dfDiv)
    
    
    def test_divideDf_colName(self):
        print("Testing: test_divideDf")

        # Set up
        df = pd.DataFrame({'ID' : ['a', 'b', 'c', 'd'], 
                           'num1': [15000, 2500, 3600, 180],
                           'num2': [10000, 1000, 100, -100]})
        dfCols = list(df.columns)
        print("Starting column names are: \n" + str(dfCols))
        
        # Try dividing dataframe
        divided = divideDf(df, 'num1', 'num2')
        dividedCols = list(divided.columns)
        print("Divided DataFrame columns are: \n" + str(dividedCols))

        # Check if column names match
        divCol = ['ID', 'num1', 'num2', 'num1%']
        print('Expected DataFrame columns are: \n' + str(divCol))
        self.assertEqual(divCol, dividedCols)
        
        
if __name__ == '__main__':
    unittest.main()