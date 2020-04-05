# Abalone Game

def ConvertToBoard():
  markers = input("Enter Line: ").split(', ')
  board = []
  for letter in range(65,74):
    row = []
    for space in range(row_length[chr(letter)][0]):
      row.append('')
    board.append(row)
  color = ['B', 'W']
  start = 0
  for i in range(2):
    for marker in range(int(markers[start])):
      board[ord(markers[marker + start + 1][0]) - 65][int(markers[marker + start + 1][1]) - 1 - row_length[markers[marker + start + 1][0]][1]] = color[i]
    start += int(markers[start]) + 1
  return board

def FindAdjacent(row):
  adj = []
  current_adj = []
  spaces = []
  for space in range(len(row)):
    if row[space] == '':
      if current_adj != []:
        adj.append([current_adj, spaces])
        current_adj = []
        spaces = []
      continue
    current_adj.append(row[space])
    spaces.append(space)
  if current_adj != []:
    adj.append([current_adj, spaces])
  return adj        

def FindPush(adjacent):
  for adj in adjacent:
    if len(adj[0]) < 3:
      continue
    possible_push = (
    (['B','B','W'],['B','B','B','W'],['B','B','B','W','W']),
    (['W','B','B'],['W','B','B','B'],['W','W','B','B','B']),
    (['B','W','W'],['B','W','W','W'],['B','B','W','W','W']),
    (['W','W','B'],['W','W','W','B'],['W','W','W','B','B']))
    Found = False
    color = ['B', 'W']
    for i in range(2):
      current_adj = adj[0][:]
      space = adj[1][:]
      Slice = [None, None]
      Slice[i] = 0
      while len(current_adj) >= 3:
        if current_adj in possible_push[2 * i]:
          yield [space, color[i]]
          Found = True
          break
        elif current_adj in possible_push[-2 * i + 3]:
          yield [space, color[-i + 1] + '+']
          Found = True
          break
        else:
          Slice[i] += -2 * i + 1
          current_adj = current_adj[Slice[0]:Slice[1]]
          space = space[Slice[0]:Slice[1]]

      if Found:break
  return

def EvaluatePush(pushes, row):
  IsGeneratorNotEmpty = False
  for push in pushes:
    IsGeneratorNotEmpty = True
    solution = 'Y'
    if push[1] == 'B' and push[0][-1] == row_length[chr(row + 65)][0] - 1:
      solution += ', 1, W'
    elif push[1] == 'B+' and push[0][0] == 0:
      solution += ', 1, W'
    elif push[1] == 'W' and push[0][0] == 0:
      solution += ', 1, B'
    elif push[1] == 'W+' and push[0][-1] == row_length[chr(row + 65)][0] - 1:
      solution += ', 1, B'
    else: solution += ', 0'
    print(solution)
  return IsGeneratorNotEmpty

    
row_length = {'A': [5, 0], 'B': [6, 0], 'C': [7, 0], 'D': [8, 0],
'E': [9, 0], 'F': [8, 1], 'G': [7, 2], 'H': [6, 3],'I': [5, 4]}
for i in range(10):
  board = ConvertToBoard()
  SolutionNotThere = True
  for row in range(len(board)):
    result = EvaluatePush(FindPush(FindAdjacent(board[row])), row)
    if result:
      SolutionNotThere = False
  if SolutionNotThere:
    print('N')