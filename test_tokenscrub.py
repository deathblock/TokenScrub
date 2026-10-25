# test_tokenscrub.py
"""
Tests for TokenScrub module.
"""

import unittest
from tokenscrub import TokenScrub

class TestTokenScrub(unittest.TestCase):
    """Test cases for TokenScrub class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenScrub()
        self.assertIsInstance(instance, TokenScrub)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenScrub()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
