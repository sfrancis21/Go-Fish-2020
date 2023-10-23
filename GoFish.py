import random

deck=["Ace of Spades","2 of Spades","3 of Spades","4 of Spades","5 of Spades","6 of Spades","7 of Spades","8 of Spades","9 of Spades","10 of Spades","Jack of Spades","Queen of Spades","King of Spades","Ace of Diamonds","2 of Diamonds","3 of Diamonds","4 of Diamonds","5 of Diamonds","6 of Diamonds","7 of Diamonds","8 of Diamonds","9 of Diamonds","10 of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds", "Ace of Clubs","2 of Clubs","3 of Clubs","4 of Clubs","5 of Clubs","6 of Clubs","7 of Clubs","8 of Clubs","9 of Clubs","10 of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs","Ace of Hearts","2 of Hearts","3 of Hearts","4 of Hearts","5 of Hearts","6 of Hearts","7 of Hearts","8 of Hearts","9 of Hearts","10 of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts"]
random.shuffle(deck)

winner=1
player = 1
p1hand = []
p2hand = []
p1wins= 0
p2wins= 0 


def give_hand():
  for num in range (0,7):
    p1hand.append(deck[num])
  for num in range (7,14):
    p2hand.append(deck[num])
  for elem in range (0,15):
    deck.pop(0)
    elem=elem+1
  print("Player 1 please write down your hand: " + str(p1hand))
  ready=input("Ready to see your hand Player 2? ")
  if ready=="yes":
    print("Player 2 please write down your hand: " + str(p2hand))

def go_fish():
  go_fish = 0
  if player==1:
    if (card + " of Spades") in p2hand:
      print("Player 1 has taken the card " + card + " of Spades")
      p1hand.append(card + " of Spades")
      p2hand.remove(card + " of Spades")
      go_fish=go_fish + 1
    if (card + " of Hearts") in p2hand:
      print("Player 1 has taken the card " + card + " of Hearts")
      p1hand.append(card + " of Hearts")
      p2hand.remove(card + " of Hearts")
      go_fish=go_fish + 1
    if (card + " of Clubs") in p2hand:
      print("Player 1 has taken the card " + card + " of Clubs")
      p1hand.append(card + " of Clubs")
      p2hand.remove(card + " of Clubs")
      go_fish=go_fish + 1
    if (card + " of Diamonds") in p2hand:
      print("Player 1 has taken the card " + card + " of Diamonds")
      p1hand.append(card + " of Diamonds")
      p2hand.remove(card + " of Diamonds")
      go_fish=go_fish + 1
    if go_fish==0:
      print("Go Fish!")
      draw_card()

  if player==2:
    if (card + " of Spades") in p1hand:
      print("Player 2 has taken the card " + card + " of Spades")
      p2hand.append(card + " of Spades")
      p1hand.remove(card + " of Spades")
      go_fish=go_fish + 1
    if (card + " of Hearts") in p1hand:
      print("Player 2 has taken the card " + card + " of Hearts")
      p2hand.append(card + " of Hearts")
      p1hand.remove(card + " of Hearts")
      go_fish=go_fish + 1
    if (card + " of Clubs") in p1hand:
      print("Player 2 has taken the card " + card + " of Clubs")
      p2hand.append(card + " of Clubs")
      p1hand.remove(card + " of Clubs")
      go_fish=go_fish + 1
    if (card + " of Diamonds") in p1hand:
      print("Player 2 has taken the card " + card + " of Diamonds")
      p2hand.append(card + " of Diamonds")
      p1hand.remove(card + " of Diamonds")
      go_fish=go_fish + 1
    if go_fish==0:
      print("Go Fish!")
      draw_card()
 
def draw_card():
  if player==1:
    p1hand.append(deck[0])
    deck.pop(0)
    print("New Hand: " + str(p1hand))
  if player==2:
    p2hand.append(deck[0])
    deck.pop(0)
    print("New Hand " + str(p2hand))

def draw_set():
  if player==1:
    for num in range (0,3):
      p1hand.append(deck[num])
    for elem in range (0,5):
      deck.pop(0)
      elem = elem +1
    print("New Hand:" + str(p1hand))
  if player==2:
    for num in range (0,3):
      p1hand.append(deck[num])
    for elem in range (0,3):
      deck.pop(0)
      elem = elem +1
    print("New Hand: " + str(p2hand))

def check_sets():
  if player==1:
    global p1wins
    for num in range (11):
      if (str(num) + " of Spades" in p1hand) and (str(num) + " of Hearts" in p1hand) and (str(num) + " of Diamonds" in p1hand) and (str(num) + " of Clubs" in p1hand):
        p1wins = p1wins + 1
        p1hand.remove(str(num) + " of Spades")
        p1hand.remove(str(num) + " of Hearts")
        p1hand.remove(str(num) + " of Diamonds")
        p1hand.remove(str(num) + " of Clubs")
        draw_set()
    if ("Ace of Spades" in p1hand) and ("Ace of Hearts" in p1hand) and ("Ace of Diamonds" in p1hand) and ("Ace of Clubs" in p1hand):
        p1wins = p1wins + 1
        p1hand.remove("Ace of Spades")
        p1hand.remove("Ace of Hearts")
        p1hand.remove("Ace of Diamonds")
        p1hand.remove("Ace of Clubs")
        draw_set()
    if ("Jack of Spades" in p1hand) and ("Jack of Hearts" in p1hand) and ("Jack of Diamonds" in p1hand) and ("Jack of Clubs" in p1hand):
        p1wins = p1wins + 1
        p1hand.remove("Jack of Spades")
        p1hand.remove("Jack of Hearts")
        p1hand.remove("Jack of Diamonds")
        p1hand.remove("Jack of Clubs")
        draw_set()
    if ("Queen of Spades" in p1hand) and ("Queen of Hearts" in p1hand) and ("Queen of Diamonds" in p1hand) and ("Queen of Clubs" in p1hand):
        p1wins = p1wins + 1
        p1hand.remove("Queen of Spades")
        p1hand.remove("Queen of Hearts")
        p1hand.remove("Queen of Diamonds")
        p1hand.remove("Queen of Clubs")
        draw_set()
    if ("King of Spades" in p1hand) and ("King of Hearts" in p1hand) and ("King of Diamonds" in p1hand) and ("King of Clubs" in p1hand):
        p1wins = p1wins + 1
        p1hand.remove("King of Spades")
        p1hand.remove("King of Hearts")
        p1hand.remove("King of Diamonds")
        p1hand.remove("King of Clubs")
        draw_set()
  if player==2:
    global p2wins
    for num in range (11):
      if (str(num) + " of Spades" in p2hand) and (str(num) + " of Hearts" in p2hand) and (str(num) + " of Diamonds" in p2hand) and (str(num) + " of Clubs" in p2hand):
        p2wins = p2wins + 1
        p2hand.remove(str(num) + " of Spades")
        p2hand.remove(str(num) + " of Hearts")
        p2hand.remove(str(num) + " of Diamonds")
        p2hand.remove(str(num) + " of Clubs")
        draw_set()
    if ("Ace of Spades" in p2hand) and ("Ace of Hearts" in p2hand) and ("Ace of Diamonds" in p2hand) and ("Ace of Clubs" in p2hand):
        p2wins = p2wins + 1
        p2hand.remove("Ace of Spades")
        p2hand.remove("Ace of Hearts")
        p2hand.remove("Ace of Diamonds")
        p2hand.remove("Ace of Clubs")
        draw_set()
    if ("Jack of Spades" in p2hand) and ("Jack of Hearts" in p2hand) and ("Jack of Diamonds" in p2hand) and ("Jack of Clubs" in p2hand):
        p2wins = p2wins + 1
        p2hand.remove("Jack of Spades")
        p2hand.remove("Jack of Hearts")
        p2hand.remove("Jack of Diamonds")
        p2hand.remove("Jack of Clubs")
        draw_set()
    if ("Queen of Spades" in p2hand) and ("Queen of Hearts" in p2hand) and ("Queen of Diamonds" in p2hand) and ("Queen of Clubs" in p2hand):
        p2wins = p2wins + 1
        p2hand.remove("Queen of Spades")
        p2hand.remove("Queen of Hearts")
        p2hand.remove("Queen of Diamonds")
        p2hand.remove("Queen of Clubs")
        draw_set()
    if ("King of Spades" in p2hand) and ("King of Hearts" in p2hand) and ("King of Diamonds" in p2hand) and ("King of Clubs" in p2hand):
        p2wins = p2wins + 1
        p2hand.remove("King of Spades")
        p2hand.remove("King of Hearts")
        p2hand.remove("King of Diamonds")
        p2hand.remove("King of Clubs")
        draw_set()

def check_winner():
  if p1wins > 5:
    return "1"
  if p2wins > 5:
    return "2"

play = input("Would you like to play Go Fish? ")
if (play == "yes"):
  give_hand()
while check_winner() is None:
  card=input("Player " + str(player) + " what card would you like to fish for? ")
  go_fish()
  check_sets()
  check_winner()
  if player==1:
    player=2
  else:
    player=1
print("Player " + check_winner() + " wins!")
  
  
