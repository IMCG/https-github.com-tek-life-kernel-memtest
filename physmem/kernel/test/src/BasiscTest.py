#!/bin/env python
'''
This source code is distributed under the MIT License

Copyright (c) 2010, Jens Neuhalfen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import unittest
import fcntl
from ctypes import *

import physmem 

class Test(unittest.TestCase):


    def setUp(self):
        pass
 
    def tearDown(self):
        pass

    def test64Bit(self):
	self.assertEqual(sizeof(c_uint64),8,"Sizeof uint64 incorrect")
	self.assertEqual(sizeof(POINTER(physmem.Phys_mem_frame_request)),sizeof(c_uint64),"POINTERs not 64 bit")
	self.assertEqual(sizeof(physmem.Phys_mem_frame_request), 2 * sizeof(c_uint64),"Incorrect size for Phys_mem_frame_request")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
