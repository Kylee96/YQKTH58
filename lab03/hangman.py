secret_phrase = open('secret_phrase.txt', 'r')
read_phrase = secret_phrase.read()

shown_phrase = '_ ' '_ ' '_ ' '_ ' '_ ' '_'

word = read_phrase
guesses = ''

print "Welcome to Hangman! We hope that you have fun and good luck!"
print 'Begin the game by guessing a letter at a time.'
print 'The word that you have to guess:'

turns = 20

# Creating the while loop
while turns > 0:
  count = 0
  missed = 0
#If the letter is in the phrase, print it, and add 1 to the number count
  for letter in read_phrase:
    if letter in guesses:
      print letter,
      count +=1
# If the letter is not in the phrase, leave the _, but still add 1 to the number count
    else:
      print '_',
      count += 1
      missed += 1

  print
  if missed == 0:
    print 'Well done, you have guessed it correctly!'
    print "Number of rounds taken:", count
    break

# Allow the players to key in their guesses
  guess = raw_input('Guess a letter:')
  guesses += guess

# Condition that only one letter is guessed
  if len(guess) != 1 :
      print("Please enter only one letter.")
      count += 1
# Condition that the letter must be an alphabet
  elif guess not in 'abcdefghijklmnopqrstuvwxyz':
      print "Enter a letter, not a number!"
      count += 1
# If the letter guessed is not in the phrase, it is incorrect
  elif guess not in read_phrase:
      print "Incorrect, try again!"
      count +=1


