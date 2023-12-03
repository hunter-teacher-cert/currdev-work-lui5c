# blankman (hangman)


words = []

with open('assets/words.txt') as file:
  for line in file:
    words.append(line.strip())


import random 
word = words[random.randint(0, len(words)-1)]

to_show = ["_" for i in range(len(word))]
guessed = []

done = False

while not done:
  print(f"guesses: {len(guessed)} ({' '.join(guessed)})")
  print("".join(to_show))
  guess = input("type a letter to guess:")
  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        to_show[i] = guess
  else:
    guessed.append(guess)
  if "_" not in to_show:
    done = True

print(word)
