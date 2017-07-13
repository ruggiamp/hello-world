# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:32:59 2017

@author: ruggero
"""

import unittest
from nose.tools import assert_equal

#import modules to be testited
import simplemodule

class TestHelloWorld(unittest.TestCase):
    def test_simple(self):
        assert_equal(4, 2+2)
        
#    def test_fail(self):
#        self.assertEqual(5, 2+2, msg="Of course 2+2 != 5")
     
    def test_summer(self):
        assert_equal(8, simplemodule.int_sum(5, 3)) #define an object of the class you want to test