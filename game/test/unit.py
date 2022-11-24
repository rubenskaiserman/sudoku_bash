import unittest
import sys
import os

sys.path.append('./game/')
from src.helper import board_builder
from src.helper import interaction

class TestStringMethods(unittest.TestCase):

    def test_le_funcao(self):
        self.assertEqual(board_builder.le_sudoku('./game/boards/imagem1.csv'), '5 , 3 , 0 , 0 , 7 , 0 , 0 , 0 , 0\n6 , 0 , 0 , 1 , 9 , 5 , 0 , 0 , 0\n0 , 9 , 8 , 0 , 0 , 0 , 0 , 6 , 0\n8 , 0 , 0 , 0 , 6 , 0 , 0 , 0 , 3\n4 , 0 , 0 , 8 , 0 , 3 , 0 , 0 , 1\n7 , 0 , 0 , 0 , 2 , 0 , 0 , 0 , 6\n0 , 6 , 0 , 0 , 0 , 0 , 2 , 8 , 0\n0 , 0 , 0 , 4 , 1 , 9 , 0 , 0 , 5\n0 , 0 , 0 , 0 , 8 , 0 , 0 , 7 , 9')

    def test_cria_tabuleiro(self):
        conteudo = board_builder.le_sudoku('./game/boards/imagem1.csv')
        self.assertEqual(board_builder.cria_tabuleiro(conteudo), ['530070000', '600195000', '098000060', '800060003', '400803001', '700020006', '060000280', '000419005', '000080079'])

    def test_posicoes_fixas(self):
        conteudo = board_builder.le_sudoku('./game/boards/imagem1.csv')
        self.assertEqual(board_builder.armazena_posicoes_fixas(conteudo), [(0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 7), (3, 0), (3, 4), (3, 8), (4, 0), (4, 3), (4, 5), (4, 8), (5, 0), (5, 4), (5, 8), (6, 1), (6, 6), (6, 7), (7, 3), (7, 4), (7, 5), (7, 8), (8, 4), (8, 7), (8, 8)])


if __name__ == '__main__':
    unittest.main()