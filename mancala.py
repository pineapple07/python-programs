def PlayMove(board, start, player):
  stones = board[0][start]
  board[0][start] = 0
  EndsOnMancala = False
  j = 0
  for i in range(stones):
    if not player and start + i + 1 == 6:
      board[1][0] += 1
      EndsOnMancala = True
      j += 1
      continue
    if player and start + i - j + 1 == 12:
      start = - i + j - 1
      board[2][0] += 1
      EndsOnMancala = True
      j += 1
      continue
    if start + i - j + 1 == 12: start = - i + j - 1
    EndsOnMancala = False
    board[0][start + i - j + 1] += 1
  start = start + i - j + 1
  if board[0][start] != 1 and board[0][start] != 4 and not EndsOnMancala:
    return PlayMove(board, start, player)
  else: return board

board = [[4 for i in range(12)], [0], [0]]
for i in range(5):
  move = input("Enter line: ").split(', ')
  board = PlayMove(board, int(move[0]) - 1, i % 2)
  if move[1] == 'A': place = [1, 0]
  elif move[1] == 'B': place = [2, 0]
  else: place = [0, int(move[1]) - 1]
  print(board[place[0]][place[1]])