import random
import os
from art import logo

clear = lambda: os.system('cls')

def dealCard():
    #       ace,                   j,  q, k
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    
    return random.choice(deck)

def calculateScore(cards):
    if (sum(cards) == 21) and (len(cards) == 2):
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(playerScore, computerScore):
    
    if playerScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Computer wins"
    elif playerScore == 0:
        return "Player wins"
    elif playerScore > 21:
        return "Computer wins"
    elif computerScore > 21:
        return "Player wins"
    elif playerScore > computerScore:
        return "Player wins"
    else:
        return "Computer wins"

def game():
    isGameOver = False
    playerCards = []
    computerCards = []

    #Dealing cards
    for _ in range(2):
        playerCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver: 
        playerScore = calculateScore(playerCards)
        computerScore = calculateScore(computerCards)

        print(f"Player cards: {playerCards}, Player Score: {playerScore}")
        print(f"Computer cards: {computerCards}, Computer Score: {computerScore}")

        if playerScore == 0 or computerScore == 0 or playerScore > 21:
            isGameOver = True
            
        else:
            option = input("Deal another card? (y) or (n)")
            if option == "y":
                playerCards.append(dealCard())
            else:
                isGameOver = True
            
    while computerScore < 17 and computerScore != 0:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)

    print(f"Player cards: {playerCards}, Player Score: {playerScore}")
    print(f"Computer cards: {computerCards}, Computer Score: {computerScore}")

    print(compare(playerScore, computerScore))

while input("Do you want to play blackjack? (y) or (n)") == "y":
    clear()
    print(logo)
    game()