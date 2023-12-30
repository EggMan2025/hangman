import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_____        ",
              "|            ",
              "|     |      ",
              "|     0      ",
              "|    /|\     ",
              "|    / \     ",
              "|            "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HANGMAN!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one word"
        char = input(msg)
        while len(char) != 1:
            print("Enter ONLY ONE word!")
            char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! Correct Answer is {}.".format(word))

animals = ["dog", "bird", "fish", "pig", "cow", "bear", "cat", "rabbit", "horse", "wolf",
            "whale", "bat", "gorilla", "monkey", "tiger", "sheep", "goat", "lion"]
rword = random.choice(animals)

hangman(rword)