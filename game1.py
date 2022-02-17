from random import choice

items = {
    "Rock": ["Scissors", "Lizard"],
    "Scissors": ["Paper", "Lizard"],
    "Paper": ["Rock", 'Spock'],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Scissors", "Rock"]
}

player_score = 0
computer_score = 0


def main():
    global computer_score
    global player_score

    player_input = input("Rock, Scissors, Paper, Lizard or Spock?\n>>> ")

    if player_input not in items:
        print("Wrong!")
        main()
    else:
        computer_input = choice("Rock/Scissors/Paper/Lizard/Spock".split("/"))
        print('Computer:', computer_input)

        if items[computer_input] == player_input:
            print("+1 point to computer")
            computer_score += 1
        elif player_input == computer_input:
            print('Points not received! (Draw)')
        elif items[player_input] == computer_input:
            print("+1 point to user")
            player_score += 1
        else:
            print("+1 point to user")
            player_score += 1

    a = input("Continue? y/n\n>>> ")

    while True:
        if a == "y":
            main()
        elif a == "n":

            print(str(computer_score) + " - computer score")
            print(str(player_score) + " - user score")

            if computer_score > player_score:
                print("Computer win!")
            elif computer_score < player_score:
                print("User win!")
            else:
                print("Draw!")
            break


main()

#запись в файл не получился, несовсем понял как он работает