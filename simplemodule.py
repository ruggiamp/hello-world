# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:54:41 2017

@author: ruggero
"""

def int_sum(first, second):
    return first+second

class prova(object):
    
    #thing here are common for all object: if you modify them for one object
    # then is modified for all the others as well.
    
    def __init__(self): #thing here can be changed in the different objects
        prova.attr = 'dog'

    def Multiply_2factors(self, factor1, factor2):
        return factor1*factor2
    
    def NewAttributes(self):
        self.attr = 'newdog'
        
