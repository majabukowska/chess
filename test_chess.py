import unittest
import chess


class TestChess(unittest.TestCase):

    def test_number_of_elements(self):
        board = []
        result = chess.gen_board(board)
        self.assertEqual(result, [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])

    def test_k(self):
        list = [0, 1, 2, 3, 4, 5]
        self.assertIn(chess.k, list)

    def test_queen(self):
        self.assertNotEqual(chess.queen, [])

    def test_pawn(self):
        self.assertNotEqual(chess.pawn, [])


if __name__ == '__main__':
    unittest.main()
