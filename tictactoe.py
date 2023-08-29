import os
import random
from functools import partial
from time import sleep


def main():
  intro()
  board = setupBoard()
  players = initPlayers()
  playGame(board, players)


def intro():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(
"""
-------------------
    TIC TAC TOE
-------------------
The board is arranged similar to the number keypad:

 7 | 8 | 9
-----------
 4 | 5 | 6
-----------
 1 | 2 | 3

You can play against another person or the computer (or have computers duke it out).
""")


def setupBoard():
  return [
      ["-", "-", "-"],
      ["-", "-", "-"],
      ["-", "-", "-"],
  ]


def initPlayers():
  # Associate player types with functions that can be called
  # during the game
  p1 = chooseHumanOrComputer(1)
  p2 = chooseHumanOrComputer(2)
  playerToFunc = {
    'H': humanPlay,
    'C': compPlay
  }
  return [playerToFunc[p1], playerToFunc[p2]]


def chooseHumanOrComputer(p_number):
  # Prompts the user for the type of player (human or comp)
  assert p_number in [1, 2]
  player = None
  ordinal = {
    1: "First",
    2: "Second"
  }
  while player is None:
    player = input(f"{ordinal[p_number]} player: (H)uman or (C)omputer? ").upper()
    if player not in ['H', 'C']:
      print("Error: Please enter 'h' or 'c'")
      player = None
    else:
      return player


def playGame(board, players):
  turn = 0
  while True:
    displayBoard(board, turn)
    board = playerPlays(board, players, turn)
    if isWinner(board) is not None:
      showWinnerAndQuit(board)
    turn += 1


def playerPlays(board, players, turn):
  if turn % 2 == 0:
    return players[0](board, "X")
  else:
    return players[1](board, "O")


def humanPlay(board, XorO):
  pos = None
  open_spots = [pos for pos in range(1, 10) if boardVal(board, pos) == "-"]
  while pos is None:
    pos = input(f"Where to play {open_spots}? ")
    try:
      assert int(pos) in open_spots
    except (ValueError, AssertionError):
      print(f"Error: Please enter one of the following values: {open_spots}")
      pos = None
    else:
      return setPos(board, int(pos), XorO)


def compPlay(board, XorO):
  open_spots = [pos for pos in range(1, 10) if boardVal(board, pos) == "-"]
  if 5 in open_spots:
    pos = 5
  else:
    pos = random.choice(open_spots)
  sleep(0.5)
  return setPos(board, int(pos), XorO)


def isWinner(board):
  # Returns X, O, "NO ONE" if end of game
  #  ...  or None if not game ended yet
  bV = partial(boardVal, board)
  # Check rows
  if bV(1) in ['X', 'O'] and bV(1) == bV(2) == bV(3):
    return bV(1)
  if bV(4) in ['X', 'O'] and bV(4) == bV(5) == bV(6):
    return bV(4)
  if bV(7) in ['X', 'O'] and bV(7) == bV(8) == bV(9):
    return bV(7)

  # Check columns
  if bV(1) in ['X', 'O'] and bV(1) == bV(4) == bV(7):
    return bV(1)
  if bV(2) in ['X', 'O'] and bV(2) == bV(5) == bV(8):
    return bV(2)
  if bV(3) in ['X', 'O'] and bV(3) == bV(6) == bV(9):
    return bV(3)

  # Check diagonals
  if bV(1) in ['X', 'O'] and bV(1) == bV(5) == bV(9):
    return bV(1)
  if bV(3) in ['X', 'O'] and bV(3) == bV(5) == bV(7):
    return bV(3)

  # Check if there are any open spots left to play
  if all([bV(x) in ['X', 'O'] for x in range(1,10)]):
    return "NO ONE"

  return None


def showWinnerAndQuit(board):
  displayBoard(board)
  print(f"\n{isWinner(board)} WINS!")
  quit()


def boardVal(board, pos):
  x, y = indexToBoard(pos)
  return board[x][y]


def displayBoard(board, turn=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  if turn:
    print(f"TURN: {turn}   PLAYER{turn%2+1} GOES")
  bV = partial(boardVal, board)
  print(f"{bV(7)} | {bV(8)} | {bV(9)}")
  print("----------")
  print(f"{bV(4)} | {bV(5)} | {bV(6)}")
  print("----------")
  print(f"{bV(1)} | {bV(2)} | {bV(3)}")


def indexToBoard(idx):
  # x = int((9 - idx)/3)
  # y = idx % 3
  x, y = divmod(idx - 1, 3)
  return (x, y)


def setPos(board, pos, XorO):
  x, y = indexToBoard(pos)
  board[x][y] = XorO
  return board


if __name__ == "__main__":
  main()