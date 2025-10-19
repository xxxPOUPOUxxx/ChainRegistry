# test_chainregistry.py
"""
Tests for ChainRegistry module.
"""

import unittest
from chainregistry import ChainRegistry

class TestChainRegistry(unittest.TestCase):
    """Test cases for ChainRegistry class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainRegistry()
        self.assertIsInstance(instance, ChainRegistry)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainRegistry()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
