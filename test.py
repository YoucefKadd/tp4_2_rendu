# test_script.py

import unittest
from unittest.mock import patch
from script import main

class TestScript(unittest.TestCase):
    
    @patch('builtins.print')
    def test_main_function(self, mock_print):
        main()
        mock_print.assert_called_with("Hello from your Python script!")

if __name__ == '__main__':
    unittest.main()
