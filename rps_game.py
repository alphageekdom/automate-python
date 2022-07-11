import random
import sys

print('ROCK, PAPER, SCISSORS')

def game():
    wins = 0
    losses = 0
    ties = 0
    # main game loop
    while True:
        print('%s Wins, %s Losses, %s Ties \n' % (wins, losses, ties))
        # player input
        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move = input()
            if player_move == 'q':
                sys.exit()
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break
            print('Type one of r, p, s, or q.')
        
        # display player's choice
        if player_move == 'r':
            print('Rock versus...')
        elif player_move == 'p':
            print('Paper versus...')
        elif player_move == 's':
            print('Scissors versus...')
        
        
        # display computer's choice
        random_number = random.randint(1, 3)
        if random_number == 1:
            computer_move = 'r'
            print('ROCK')
        elif random_number == 2:
            computer_move = 'p'
            print('PAPER')
        elif random_number == 3:
            computer_move = 's'
            print('SCISSORS')
        
        
        # display and record win/loss/tie
        if player_move == computer_move:
            print('It is a tie!\n')
            ties += 1
        elif player_move == 'r' and computer_move == 's':
            print('You win!\n')
            wins += 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win!\n')
            wins += 1
        elif player_move == 's' and computer_move == 'p':
            print('You win!\n')
            wins += 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!\n')
            losses += 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!\n')
            losses += 1
        elif player_move == 's' and computer_move == 'r':
            print('You lose!\n')
            losses += 1


game()