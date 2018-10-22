import sys
import random

class hangman():
  def __init__(self):
    word_list=["abjointed", "antiworld", "importance", "deliverance", "decrease", "increase", "disorganized", "unbelievable", "misunderstanding", "hopelessness", "beliefs", "tradition", "religion", "achievement", "unprecedented", "inhumane", "insanity", "disapproval", "hypocrisy", "babaric", "hippopotamus", "flabbergasted", "originated"]
    self.word=random.choice(word_list)
    self.word_list=list(self.word)
    self.game_word_list=["-"]*len(self.word)
    self.game_word="".join(self.game_word_list)
    self.guess=3
    return

  def check(self, letter_guess):
    if letter_guess in self.word:
      self.correct(letter_guess)
    else:
      self.wrong()

  def wrong(self):
    print("Wrong guess")
    self.guess-=1

  def correct(self, letter_guess):
    print("Correct guess")
    self.edit_list(letter_guess)

  def edit_list(self, letter_guess):
    while letter_guess in self.word_list:
      index=self.word_list.index(letter_guess)
      self.game_word_list[index]=letter_guess
      self.game_word="".join(self.game_word_list)
      self.word_list[index]="-"

    return
    
  def print_game_word_list(self):
    return self.game_word_list

  


a=hangman()
while a.guess>0 and a.game_word!=a.word:
  
  print("The word is "+str(a.game_word))
  letter_guess=input("You have "+str(a.guess)+" guesses left. Guess a letter.")
  a.check(letter_guess)
  

if a.guess==0:
  print("Guesses finished")
  print("The word was "+str(a.word))
  input()
  raise SystemExit


print("You WON!! \nYou're a STAR and you'll be successful in life")
input()



