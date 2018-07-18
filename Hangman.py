word = input("Type a word for someone to guess: ")
if(word.isalpha() == False):
  print("That's not a word!")

word = word.lower()
secret= []
secret.extend(word)

dashes=[]
for char in word:
    dashes.append("-")

guess = ''
maxfails = 7

while maxfails > 0:
    guess = input("Guess a letter: ")
    if guess in secret:
        print(guess)
    else:
        maxfails -= 1
