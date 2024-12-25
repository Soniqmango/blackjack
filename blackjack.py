import random

def createDeck():
    """Create a standard 52-card deck."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    return [rank for rank in ranks for _ in suits]

def shuffleDeck(deck):
    """Shuffle the deck."""
    random.shuffle(deck)

def calcHandVal(hand):
    """Calculate the total value of a hand."""
    value = 0
    ace_count = 0
    
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            value += 10
        elif card == "Ace":
            ace_count += 1
            value += 11
        else:
            value += int(card)
    
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1

    return value

def giveCard(deck):
    """Deal a card from the deck."""
    return deck.pop()

def displayHand(hand, hidden=False):
    """Display the player's or dealer's hand."""
    if hidden:
        print(f"Dealer's hand: [{hand[0]}, ?]")
    else:
        print(f"Hand: {', '.join(hand)}")


deck = createDeck()
shuffleDeck(deck)

# Initial hands
playerHand = [giveCard(deck), giveCard(deck)]
dealerHand = [giveCard(deck), giveCard(deck)]

# Player's turn
print("\nYour turn:")
displayHand(playerHand)
displayHand(dealerHand, hidden=True)

while True:
    playerValue = calcHandVal(playerHand)
    if playerValue > 21:
        print(f"You bust! Your hand value is {playerValue}.")
        break
    choice = input("Do you want to (h)it or (s)tand? ").lower()
    if choice == 'h':
        playerHand.append(giveCard(deck))
        print("\nYou drew a card:")
        displayHand(playerHand)
    elif choice == 's':
        print("\nYou chose to stand.")
        break
    else:
        print("Invalid choice. Please choose 'h' or 's'.")

# Dealer's turn
print("\nDealer's turn:")
displayHand(dealerHand)

while calcHandVal(dealerHand) < 17:
    dealerHand.append(giveCard(deck))
    print("\nDealer drew a card:")
    displayHand(dealerHand)

dealerValue = calcHandVal(dealerHand)
playerValue = calcHandVal(playerHand)

# Determine winner
print("\nFinal results:")
print(f"Your hand value: {playerValue}")
print(f"Dealer's hand value: {dealerValue}")

if dealerValue > 21 and playerValue <= 21 or 21 >= playerValue > dealerValue:
    print("You win!")
elif playerValue == dealerValue or dealerValue > 21 and playerValue > 21:
    print("It's a tie!")
else:
    print("Dealer wins!")