import unittest
import tictactoe


class TestTicTacToe(unittest.TestCase):
  def test_indexToBoard(self):
    self.assertEqual(tictactoe.indexToBoard(1), (0,0))
    self.assertEqual(tictactoe.indexToBoard(2), (0,1))
    self.assertEqual(tictactoe.indexToBoard(3), (0,2))
    self.assertEqual(tictactoe.indexToBoard(4), (1,0))
    self.assertEqual(tictactoe.indexToBoard(5), (1,1))
    self.assertEqual(tictactoe.indexToBoard(6), (1,2))
    self.assertEqual(tictactoe.indexToBoard(7), (2,0))
    self.assertEqual(tictactoe.indexToBoard(8), (2,1))
    self.assertEqual(tictactoe.indexToBoard(9), (2,2))

  def test_isWinner_row(self):
    testBoard = [
        ["X","X","X"],
        ["-","-","-"],
        ["-","-","-"],
    ]

    self.assertEqual(tictactoe.isWinner(testBoard), "X")

  def test_isWinner_diagonal(self):
    testBoard = [
      ["O","-","-"],
      ["-","O","-"],
      ["-","-","O"],
    ]

    self.assertEqual(tictactoe.isWinner(testBoard), "O")

  def test_isWinner_still_in_progress(self):
    testBoard = [
      ["-","X","-"],
      ["-","O","-"],
      ["X","-","O"],
    ]

    self.assertEqual(tictactoe.isWinner(testBoard), None)

  def test_isWinner_no_one(self):
    testBoard = [
      ["X","X","O"],
      ["O","O","X"],
      ["X","O","O"],
    ]

    self.assertEqual(tictactoe.isWinner(testBoard), "NO ONE")

if __name__ == '__main__':
    unittest.main()