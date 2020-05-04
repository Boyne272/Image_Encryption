# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:59:01 2020

@author: Boyne
"""

import pytest
from utils import str2bin, bin2str

SOME_STRS = ['test',
             'qwertyuiopasdfghjklzxcvbnm',
             'QWERTYUIOPASDFGHJKLZXCVBNM',
             '1234567890!"£$%^&*(){}:@[];,.<>#|\¬`',
             '''
             The Zen of Python, by Tim Peters\n
             Beautiful is better than ugly.
             Explicit is better than implicit.
             Simple is better than complex.
             Complex is better than complicated.
             Flat is better than nested.
             Sparse is better than dense.
             Readability counts.
             Special cases aren't special enough to break the rules.
             Although practicality beats purity.
             Errors should never pass silently.
             Unless explicitly silenced.
             In the face of ambiguity, refuse the temptation to guess.
             There should be one-- and preferably only one --obvious way
             to do it.
             Although that way may not be obvious at first unless you're Dutch.
             Now is better than never.
             Although never is often better than *right* now.
             If the implementation is hard to explain, it's a bad idea.
             If the implementation is easy to explain, it may be a good idea.
             Namespaces are one honking great idea -- let's do more of those!
             ''']

@pytest.mark.parametrize("test_string", *SOME_STRS)
def test_str2bin_sanity(test_string):
    'test the output is of correct length and all binary'
    binary = str2bin(test_string)
    assert len(binary) % 16 == 0
    assert set(binary) == {'0', '1'}
    

#@pytest.mark.parametrize('non_string_var', [
#        100,
#        {},
#        ['a', 'b']])
#@pytest.mark.xfail(raises=AssertionError)
#def test_str2bin_assert(test_string):
#    'test the function breaks if you dont pass a string'
#    str2bin(100)
    

    
    
    
    