import random 
def hangman(word):
  rletters = list(word)
  wrong = 0
  stages = [
    '',
    '___________          ',
    '|                    ',
    '|          |         ',
    '|          0         ',
    '|         /|\        ',
    '|         / \        ',
    '|                    '
  ]
  board = ['_'] * len(word)
  win = False
  print('Игра началась')
  while wrong < len(word) - 1:
    msg = input('Введите букву')
    if msg in rletters:
      print('Вы угадали букву!')
      for i in range(len(rletters)):
        if rletters[i] == msg:
          board[i] = msg
      print(board)
    else:
      print('Вы не угадали букву:(')
      wrong += 1
    if '_' not in board:
      print('Вы выйграли!')
      win = True
      break
  if not win:
    print(':(')

word_list = ['слон', 'собака', 'кот']
random_word = random.choice(word_list)
hangman(random_word)