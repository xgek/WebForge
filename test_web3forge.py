# test_web3forge.py
"""
Tests for Web3Forge module.
"""

import unittest
from web3forge import Web3Forge

class TestWeb3Forge(unittest.TestCase):
    """Test cases for Web3Forge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Forge()
        self.assertIsInstance(instance, Web3Forge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Web3Forge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
