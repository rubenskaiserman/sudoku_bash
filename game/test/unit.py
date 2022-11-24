import unittest
import sys
import os

sys.path.append('./game/')
from src.helper import helper

class TestStringMethods(unittest.TestCase):

    def test_le_funcao(self):
        print(helper.le_sudoku('./game/boards/imagem1.csv'))
        self.assertEqual(
            helper.le_sudoku('./game/boards/imagem1.csv'), '530070000600195000098000060800060003400803001700020006060000280000419005000080079')

if __name__ == '__main__':
    unittest.main()