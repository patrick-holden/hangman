from milestone_4 import Hangman

def play_game():
    num_lives = 5
    word_list = []
    for _ in range(5):
      word_list.append(input("Enter a word: "))

    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif len(game.letters_remaining) > 0:
            game.ask_for_input()
        else:
            print('Congratulations!  You won the game')
            break

play_game()