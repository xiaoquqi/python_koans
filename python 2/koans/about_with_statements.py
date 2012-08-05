#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutSandwichCode in the Ruby Koans
#

from runner.koan import *

import re  # For regular expression string comparisons


class AboutWithStatements(Koan):
    def count_lines(self, file_name):
        try:
            f = open(file_name)
            try:
                count = 0
                for line in f.readlines():
                    count += 1
                return count
            finally:
                f.close()
        except IOError:
            # should never happen
            self.fail()
    
    def test_counting_lines(self):
        self.assertEqual(4, self.count_lines("example_file.txt"))
    
    # ------------------------------------------------------------------
        
    def find_line(self, file_name):
        try:
            f = open(file_name)
            try:
                for line in f.readlines():
                    match = re.search('e', line)
                    if match:
                        return line
            finally:
                f.close()
        except IOError:
            # should never happen
            self.fail()
    
    def test_finding_lines(self):
        self.assertEqual("test\n", self.find_line("example_file.txt"))
    
    ## ------------------------------------------------------------------
    ## THINK ABOUT IT:
    ##
    ## The count_lines and find_line are similar, and yet different.
    ## They both follow the pattern of "sandwich code".
    ##
    ## Sandwich code is code that comes in three parts: (1) the top slice
    ## of bread, (2) the meat, and (3) the bottom slice of bread.  The
    ## the bread part of the sandwich almost always goes together, but
    ## the meat part changes all the time.
    ##
    ## Because the changing part of the sandwich code is in the middle,
    ## abstracting the top and bottom bread slices to a library can be
    ## difficult in many languages.
    ##
    ## (Aside for C++ programmers: The idiom of capturing allocated
    ## pointers in a smart pointer constructor is an attempt to deal with
    ## the problem of sandwich code for resource allocation.)
    ##
    ## Python solves the problem using Context Managers. Consider the
    ## following code:
    ##
    ## http://docs.python.org/release/2.5.2/lib/typecontextmanager.html
    ## Python's with statement supports the concept of a runtime context defined by a context manager. This is implemented using two separate methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends.
    ## The context management protocol consists of a pair of methods that need to be provided for a context manager object to define a runtime context:
    ## __enter__()
    ## Enter the runtime context and return either this object or another object related to the runtime context. The value returned by this method is bound to the identifier in the as clause of with statements using this context manager.
    ## __exit__(exc_type, exc_val, exc_tb)
    ## Exit the runtime context and return a Boolean flag indicating if any expection that occurred should be suppressed. If an exception occurred while executing the body of the with statement, the arguments contain the exception type, value and traceback information. Otherwise, all three arguments are None.
    
    class FileContextManager():
        def __init__(self, file_name):
            self._file_name = file_name
            self._file = None
        
        def __enter__(self):
            self._file = open(self._file_name)
            return self._file
        
        def __exit__(self, cls, value, tb):
            self._file.close()
    
    # Now we write:
    
    def count_lines2(self, file_name):
        with self.FileContextManager(file_name) as f:
            count = 0
            for line in f.readlines():
                count += 1
        return count
    
    def test_counting_lines2(self):
        self.assertEqual(4, self.count_lines2("example_file.txt"))
    
    # ------------------------------------------------------------------
    
    def find_line2(self, file_name):
        with self.FileContextManager(file_name) as f:
            match = None
            for line in f.readlines():
                match = re.search('e', line)
                if match:
                    return line
    
    def test_finding_lines2(self):
        self.assertEqual("test\n", self.find_line2("example_file.txt"))
        self.assertNotEqual(None, self.find_line2("example_file.txt"))
    
    # ------------------------------------------------------------------
    
    def count_lines3(self, file_name):
        with open(file_name) as f:
            count = 0
            for line in f.readlines():
                count += 1
            return count
    
    def test_open_already_has_its_own_built_in_context_manager(self):
        self.assertEqual(4, self.count_lines3("example_file.txt"))
