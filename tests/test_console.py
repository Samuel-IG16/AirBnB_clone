#!/usr/bin/env python3
"""Unittest console module.

Test cases for console class and methods documentation and instances.
"""
import unittest

import console


Console = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing console docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = console.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = Console.__doc__
        self.assertIsNotNone(doc)
    
    def test_quit_doc(self):
        """...documentation for quit command"""
        self.assertIsNotNone(Console.do_quit.__doc__)
    
    def test_EOF_doc(self):
        """...documentation for EOF command"""
        self.assertIsNotNone(Console.do_EOF.__doc__)
    
    def test_create_doc(self):
        """...documentation for create command"""
        self.assertIsNotNone(Console.do_create.__doc__)
    
    def test_show_doc(self):
        """...documentation for show command"""
        self.assertIsNotNone(Console.do_show.__doc__)
    
    def test_destroy_doc(self):
        """...documentation for destroy command"""
        self.assertIsNotNone(Console.do_destroy.__doc__)

    def test_all_doc(self):
        """...documentation for all command"""
        self.assertIsNotNone(Console.do_all.__doc__)

    def test_update_doc(self):
        """...documentation for quit command"""
        self.assertIsNotNone(Console.do_update.__doc__)


class TestFeatures(unittest.TestCase):
    """Class for testing Console Features"""
    def test_create(self):
        self.assertIsInstance()
