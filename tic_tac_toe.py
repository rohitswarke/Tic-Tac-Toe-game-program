#!/usr/bin/python3

### Tic-Tac-Toe game program ###
### Written by: Rohit Warke  ###
### Date: May 30, 2016       ###

import sys
try:
  from clint.textui import colored
except ImportError:
  print ("clint module is missing, please install it using\nsudo pip-python install clint")
  sys.exit(0)

def print_board(m):
  global p1, p2, p1_score, p2_score
  print ("<" + colored.red('Tic') + colored.green('-Tac-') + colored.blue('Toe') + ">", end= "\t")
  print (colored.red(p1) + " : "+ repr(p1_score) + " | "+ colored.blue(p2) + " : "+ repr(p2_score))
  for i in range(0,3):
    print ("+---" * 3 + "+")
    for j in range(0,3):
      if (m[i][j] == 1):
        print ("|",colored.red(m[i][j]),end=" ")
      elif (m[i][j] == 2):
        print ("|",colored.blue(m[i][j]),end=" ")
      else:
        print ("|",m[i][j],end=" ")
    print ("|")
  print ("+---" * 3 + "+")
#end of print_board function

def check_board(m):
  global p1_score, p2_score, won
  for i in range(0,3):
    if ((m[i][0] != 0) and (m[i][0] == m[i][1] == m[i][2])):
      print (colored.green("Row matched. winner is : " + repr(m[i][0])))
      if m[i][0] == 1:
        p1_score+=1
      else:
        p2_score+=1
      won = 1
      return
    elif ((m[0][i] != 0) and (m[0][i] == m[1][i] == m[2][i])):
      print (colored.green("Column matched. winner is : " + repr(m[0][i])))
      if m[0][i] == 1:
        p1_score+=1
      else:
        p2_score+=1
      won = 1
      return
    elif ((m[0][0] != 0) and (m[0][0] == m[1][1] == m[2][2])):
      print (colored.green("First diagonal matched. winner is : " + repr(m[0][0])))
      if m[0][0] == 1:
        p1_score+=1
      else:
        p2_score+=1
      won = 1
      return
    elif ((m[2][0] != 0) and (m[2][0] == m[1][1] == m[0][2])):
      print (colored.green("Second diagonal matched. winner is : " + repr(m[2][0])))
      if m[2][0] == 1:
        p1_score+=1
      else:
        p2_score+=1
      won = 1
      return
#end of check_board function

def draw(m):
  print ("\033c")
  check_board(m)
  print_board(m)

def clear_matrix(m):
  for i in range(0,3):
    for j in range(0,3):
      m[i][j] = 0

def game(m):
  global p1, p2, won
  for chance in range(1,10,2): #9 are the total number of places to play in this game
    if won == 1:
      break
    while (1):
      try:
        i, j = [int(x) for x in input(colored.red(p1) + "! Enter row and column indexes: ").split()]
        if i > 2 or i < 0 or j > 2 or j < 0 or m[i][j] > 0:
          print ("Wrong indexes entered. Try again...")
        else:
          m[i][j] = 1
          draw(m)
          break

      except ValueError:
        print ("Oops! That was not valid input. Try again..")
      except (KeyboardInterrupt,EOFError):
        print ("Keyboard Interrupt. Program is closing...")
        sys.exit(1)

    if won == 1:
      break
#if maximum number of chances reached
    if chance >= 9:
      print ("Draw No Bet")
      break

#take input coordinates for player 2
    while (1):
      try:
        i, j = [int(x) for x in input(colored.blue(p2) + "! Enter row and column indexes: ").split()]
        if i > 2 or i < 0 or j > 2 or j < 0 or m[i][j] > 0:
          print ("Wrong indexes entered. Try again...")
        else:
          m[i][j] = 2
          draw(m)
          break

      except ValueError:
        print ("Oops! That was not valid input. Try again..")
      except (KeyboardInterrupt,EOFError):
        print ("Keyboard Interrupt. Program is closing...")
        sys.exit(1)

  #end of for loop
#end of game function

#Program starts here
m = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

print ("\033c")
p1 = input("Enter Player 1 name: ")
p2 = input("Enter Player 2 name: ")
p1_score = 0
p2_score = 0
won = 0
while (1):
  print ("\033c")
  print_board(m)
  game(m)
  try:
#    play_again = input("Play again? (y/n) : ")
#    if play_again == "n":
    print ("Plag again? (yes or no)")
    if input().lower().startswith('n'):
      break #from infinite while loop
    else:
      won = 0
      clear_matrix(m)
  except (KeyboardInterrupt,EOFError):
    print ("Keyboard Interrupt. Program is closing...")
    sys.exit(1)

