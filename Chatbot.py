def main():
  while True:
    print ("Hi there!  I'm called Chatty!")
    name = input("What's your name?")
    print ("Pleased to meet you!")
    print ("Right now, I can only play Rock-Paper-Scissors...")
    choice = input("(Press 1 for Rock-Paper-Scissors, and 2 to exit.) ")
    if choice == '1':
        rps()
    if choice == '2':
        quit()
    else:
        print ("I'm sorry.  Could you say that again?")
        choice = input("(Press 1 for Rock-Paper-Scissors, and 2 to exit.) ")

def rps():
    from random import randint
    t = ["Rock", "Paper", "Scissors"]
    computer =t[randint(0,2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play.")

def quit():
    exit()

main()
rps()
quit()
exit()
