import random

# Game symbols
symbols: dict[str, str] = {'rock': '🪨',  # rock
                           'paper': '📄',  # paper
                           'scissors': '✂️'}  # scissors

initiate: str = input("Welcome to Rock, Paper, Scissor Game. Ready to Play? (Y/n)").strip().lower()

control = None

if initiate == "y":
    control = True
    while control == True:
        # Get user input:
        player_choice: str = input('\nChoose rock (🪨), paper (📄), or scissors (✂️): ').strip().lower()
        computer_choice: str = random.choice(tuple(symbols))

        # Display choices:
        print('\nResults')
        print('----------------')
        print(f'You:      {symbols[player_choice]}  {player_choice}')
        print(f'Computer: {symbols[computer_choice]}  {computer_choice}')
        print('----------------')

        # Determine the winner
        if player_choice == computer_choice:
            print('It\'s a tie!')
        elif player_choice == 'rock' and computer_choice == 'scissors':
            print('You won with rock! 🪨')
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('You won with paper! 📄')
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('You won with scissors! ✂️')
        else:
            print('Computer wins! 🤖')

        replay = input('\nWanna play again? (Y/n)').strip().lower()
        if replay == "y":
            control = True
        else:
            print('\nGoodbye.')
            break
else:
    control = False
    print("Goodbye.")