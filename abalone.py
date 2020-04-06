### Abalone Game ###

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

def PossiblePush(adjacent):
  if adjacent == []:return
  for adj in adjacent:
    if len(adj[0]) < 3:continue
    first_color = [adj[0][0]]
    color_count = [0]
    i = 0
    for space in adj[0]:
      if space == first_color[i]:
        color_count[i] += 1
      else:
        i += 1
        first_color.append(space)
        color_count.append(1)
    MultipleColors = False
    if len(first_color) >= 3:
      possible_push = ((first_color[:2],color_count[:2]),
      (first_color[-2:], color_count[-2:]))
      MultipleColors = True
    elif len(first_color) == 2: 
      possible_push = ((first_color[:], color_count[:]),)
    else: continue
    for push in range(len(possible_push)):
      v1 = possible_push[push][1][0]
      v2 = possible_push[push][1][1]
      if v1 == v2: continue
      if v1 < v2: vals = [v1, v2, 0]
      else: vals = [v2, v1, 1]
      if MultipleColors:
        if not push:new_vals = [v1, v2]
        else:new_vals = [v2, v1] 
        if new_vals != vals[:-1]:continue
      if vals[0] >= 3: continue
      solution = possible_push[0][vals[2]]
      if MultipleColors:
        if not vals[2]: side = [None, v1 + v2]
        else: side = [-v1 - v2, None]
      else: side = [None, None]
      spaces = adj[1][side[0]:side[1]] 
      if possible_push[push][0][0] != possible_push[push][0][1 - vals[2]]:Lside = True
      else: Lside = False
      if MultipleColors and (Lside and push or not Lside and not push): continue
      yield (possible_push[push][0], spaces, possible_push[push][0][1 - vals[2]], Lside)

def EvaluatePush(pushes, row):
  IsGeneratorNotEmpty = False
  for push in pushes:
    IsGeneratorNotEmpty = True
    solution = 'Y, '
    if push[3] and push[1][0] == 0: solution += '1, '+push[0][0]
    elif not push[3] and push[1][-1] == row_length[chr(row + 65)][0] - 1:
      solution += '1, '+ push[0][1]
    else: solution += '0'
    print(solution)
  return IsGeneratorNotEmpty
   
row_length = {'A': [5, 0], 'B': [6, 0], 'C': [7, 0], 'D': [8, 0],
'E': [9, 0], 'F': [8, 1], 'G': [7, 2], 'H': [6, 3],'I': [5, 4]}
i = 0
while i < 10:
  try:
    board = ConvertToBoard()
    SolutionNotThere = True
    for row in range(len(board)):
      result = EvaluatePush(PossiblePush(FindAdjacent(board[row])), row)
      if result:
        SolutionNotThere = False
    if SolutionNotThere:
        print('N')
  except Exception: print('Try again...')
  else: i += 1