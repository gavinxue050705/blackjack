'''
Gavin Xue
Markham, ON, Canada
August 2022
CS50p - Final Project - Blackjack
'''

import sys
import random

deck = {            # dictionary of deck of cards and their values
    'A': 11,        # for simplicity, ace will only be 11
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

dealerCard = []         # initialize dealer and player decks
dealerNum = []
playerCard = []
playerNum = []

suiteD = []         # initialize the suites for cards of decks
suiteP = []

def main():
    score = begin_game()

    choice(score)


def begin_game():       # read score in from txt file and output to user
    with open('balance.txt', 'r') as file:
        score = int(file.read())

    line()
    print('Welcome to Blackjack ♠️ ♣️ ♥️ ♦️')
    print(f'Your current balance is: {score}')

    return score


def choice(score):      # prompt user for a valid action and call corresponding function
    while True:
        user = input('What would you like to do? (play/exit/load) ')

        if user == 'play':
            play(score)

        elif user == 'exit':
            exit(score)

        elif user == 'load':
            load(score)

        else:
            print('Invalid choice')


def play(score):        # start a round
    line()

    while True:         # prompt user for valid bet and remove from balance
        try:
            bet = int(input('Place your bet: '))

            if bet > score or bet <= 0:
                print('Invalid amount')

            else:
                score -= bet
                break

        except ValueError:
            print('Invalid amount')

    a = draw_card()         # draw 2 random cards for dealer and 2 for player
    b = draw_card()
    c = draw_card()
    d = draw_card()

    dealerCard.append(a)        # add card symbol, value, and suite to dealer deck
    dealerNum.append(deck[a])
    dealerCard.append(b)
    dealerNum.append(deck[b])
    suiteD.append(suite())
    suiteD.append(suite())

    playerCard.append(c)        # add card symbol, value, and suite to player deck
    playerNum.append(deck[c])
    playerCard.append(d)
    playerNum.append(deck[d])
    suiteP.append(suite())
    suiteP.append(suite())

    valueP = value(playerNum)   # determine total value of player cards
    valueD = dealerNum[0]       # only determine value of first dealer card since other is hidden

    line()          # display dealer and player cards to user
    print('Dealer\'s hand:')
    print(f'{dealerCard[0]} {suiteD[0]} ?')
    print(f'Value: {valueD}\n')

    print('Your hand:')

    for i in range(len(playerCard)):
        print(f'{playerCard[i]} {suiteP[i]} ', end='')

    print(f'\nValue: {valueP}')
    line()

    while True:         # prompt user for a valid action
        user = input('What would you like to do? (stand/hit) ')

        if user == 'stand':     # break loop if user wants to stand
            break

        elif user == 'hit':
            x = draw_card()         # draws a new card for user and add to player deck
            playerCard.append(x)
            playerNum.append(deck[x])
            suiteP.append(suite())

            valueP = value(playerNum)       # get new total value of player deck

            if valueP > 21:         # check if user has bust
                bust(score, valueP)

            line()          # display new player cards to user
            print('Dealer\'s hand:')
            print(f'{dealerCard[0]} {suiteD[0]} ?')
            print(f'Value: {valueD}\n')

            print('Your hand:')

            for i in range(len(playerCard)):
                print(f'{playerCard[i]} {suiteP[i]} ', end='')

            print(f'\nValue: {valueP}')
            line()

        else:
            print('Invalid move')
            continue

    valueD = value(dealerNum)           # get total value of dealer deck

    while valueD < 17:          # dealer keeps drawing cards until total value over 17
        x = draw_card()
        dealerCard.append(x)
        dealerNum.append(deck[x])
        suiteD.append(suite())

        valueD = value(dealerNum)

    line()          # display the final hands of dealer and player
    print('Dealer\'s hand:')

    for i in range(len(dealerCard)):
        print(f'{dealerCard[i]} {suiteD[i]} ', end='')

    print(f'\nValue: {valueD}\n')

    print('Your hand:')

    for i in range(len(playerCard)):
        print(f'{playerCard[i]} {suiteP[i]} ', end='')

    print(f'\nValue: {valueP}')
    line()

    if valueD > 21:         # player win if dealer bust
        win = bet * 2
        score += win

        print(f'Dealer bust! You win {win}!')

    elif valueD == valueP:          # tie if same value
        win = bet
        score += win

        print(f'You broke even! You win {win}!')

    elif valueD > valueP:           # player lose if smaller value
        print(f'You lost!')

    elif valueD < valueP:           # player win id larger value
        win = bet * 2
        score += win

        print(f'You win {win}!')

    print(f'Your current balance is: {score}')          # display new balance

    reset()         # reset player and dealer decks

    choice(score)           # prompt user again for action


def load(score):        # allow user to add valid amount into balance
    line()

    while True:
        try:
            user = int(input('Enter the amount to load into your balance: '))
            break

        except ValueError:
            print('Invalid amount')

    score += user

    print(f'Your updated balance is: {score}')

    choice(score)


def exit(score):        # write new score to txt file and exit program
    with open('balance.txt', 'w') as file:
        file.write(f'{score}')

    line()
    sys.exit('Thank you for playing Blackjack!')


def bust(score, valueP):
    valueD = value(dealerNum)

    while valueD < 17:          # dealer draws cards until total value over 17
        x = draw_card()
        dealerCard.append(x)
        dealerNum.append(deck[x])
        suiteD.append(suite())

        valueD = value(dealerNum)

    line()          # displays final hands of dealer and player
    print('Dealer\'s hand:')

    for i in range(len(dealerCard)):
        print(f'{dealerCard[i]} {suiteD[i]} ', end='')

    print(f'\nValue: {valueD}\n')

    print('Your hand:')

    for i in range(len(playerCard)):
        print(f'{playerCard[i]} {suiteP[i]} ', end='')

    print(f'\nValue: {valueP}\n')
    line()

    print('Bust! You lost!')            # player loses from bust
    print(f'Your current balance is: {score}')

    reset()

    choice(score)


def reset():        # clear all values from decks
    dealerCard.clear()
    dealerNum.clear()
    playerCard.clear()
    playerNum.clear()
    suiteD.clear()
    suiteP.clear()


def draw_card():        # draw random card
    return random.choice(list(deck))


def value(person):          # sum up all values of deck
    return sum(person)


def suite():        # assign random suite to card
    symbol = ['♠️', '♣️', '♥️', '♦️']

    return random.choice(list(symbol))


def line():         # prints a dividing line
    print('-----------------------------------------------------------')


if __name__ == '__main__':
    main()