# test_script.py

import unittest
from unittest.mock import patch
from script import main

class TestScript(unittest.TestCase):
    
    @patch('builtins.print')
    def test_main_function(self, mock_print):
        # Testons si la fonction main affiche correctement le message
        main()
        mock_print.assert_called_with("Hello Jon Snow, you know nothing!")

if __name__ == '__main__':
    unittest.main()
