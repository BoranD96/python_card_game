"""User interface functions for the card game.

This module contains console-based input and output functions used to
display game information, collect player input, and show round or game
summaries.
"""

__author__ = "BR"


def trick_infobar(round_num, trick_num, bonus, player, played_cards):
    print(f'+++ Now is Trick {trick_num} in Round {round_num}. +++')
    print(f'Bonus suit in this round is *** {bonus} ***')
    print(f'Now it\'s {player.name}\'s turn.')
    print(f'Cards played in this trick:')
    for card in played_cards.values():
        print(card)


def trick_act(player, score_round):
    print(f'Player {player.name} has cards in hand: {player.hand}')
    print('You can choose from following actions:\n' \
          'Press \'s\' to check your scores in current round.\n' \
          'Press \'p\' to play your card this trick.')
    while True:
        choice = input()
        if choice == 's':
            print(f'{player.name}\'s scores so far in this round are: {score_round}')
        elif choice == 'p':
            break
        else:
            print('Please enter a valid value.')


def trick_choose_card(hand_size):
    while True:
        try:
            choice = int(input(
                        'Which card would you like to play?: \n'
                        '(Please enter the index of the card: 1,2,3...)'))
            if 1 <= choice <= hand_size:
                return choice
            else:
                print(f'Please enter a number between 1 and {hand_size}.')
        except ValueError:
            print('Please enter an integer.')


def trick_show_scores(trick_num, round_num, played_cards, winner, score_dict):
    print(f'+++  Trick {trick_num} has ended!  +++')
    print(f'=== Round {round_num} Trick {trick_num} Summary ===')
    print('Cards played by all players in this trick are:')
    for player, card in played_cards.items():
        print(f'{player.name:<15} {card}')
    print(f'The winner is {winner.name}')
    print('The score table for this trick is shown below:')
    for player, score in score_dict.items():
        print(f'{player.name:<15} Trick Score: {score}')


def round_infobar(round_num, order):
    print(f'====  Now begins Round {round_num}!  ====')
    print(f'Starting order of this round goes: \n'
          f'{order}.')
    print('Dealing cards ......')

def round_bonus(bonus_suit):
    print('Everyone\'s hand cards have been dealed!')
    print(f'Bonus suit in this round is *** {bonus_suit} ***.')

def round_show_scores(round_num, player_list):
    print(f'+++  Round {round_num} has ended!  +++')
    print('The score table this round is shown below:')
    print(f'===== Round {round_num} Summary =====')
    for player in player_list:
        print(f'{player.name:<15}'
              f'Round: {player.score_round:<5} '
              f'Total: {player.score_total}')
        
def game_players():
    player_names = []
    print('+++   Welcome to Card Game!   +++')
    print('The game can be played by 2 to 5 players, including robots!')
    print('Do you want to also play with computer players?') # not finished, dont have robots yet!

    while len(player_names) < 5:
        print(f'Please enter the name of player {len(player_names) + 1}:')
        print('(Already set up all players? Press 0 to quit this process.)')
        name = input().strip()
        if name == '0' and len(player_names) >= 2:
            break
        elif name == '0' and len(player_names) < 2:
            print('Sorry, this game should be played by at least 2 players :(.')
        elif name == '':
            print('Please enter a valid name!')
        else:
            player_names.append(name)
    
    return player_names

def game_summary(player_list, winner):
    print('====== Game Summary ======')
    print('The game has ended and we\'ve got a winner!')
    print('=== Final Scores ===')
    for player in player_list:
        print(f'{player.name:<15} '
              f'Total Score: {player.score_total}')
    print(f'The winner is: {winner.name} with total score: {winner.score_total}')

def game_restart():
    print('Do you want to play for another time?')
    while True:
        choice = input('Please enter \'r\' to restart the game. '
                       'Enter \'q\' to quit the game.').strip().lower()
        if choice == 'r' or choice == 'q':
            return choice
        else:
            print('Please enter a valid input!')

