from enum import Enum

class Street(Enum):
  PREFLOP = 0
  FLOP = 1
  TURN = 2
  RIVER = 3

class Player():
  def __init__(self, position, folded, streetBet):
    self.position = position # int, Seat position 
    self.folded = folded # bool, true = not in hand, false = in hand
    self.streetBet = streetBet # int, Amount bet in current street

class TableInfo():
  def __init__(self, players, street, toCall, pot, potWithBets, streetTotal, handPlayers, cap, dealerPosition):
    self.players = players # int, Number of players in game
    self.street = street # enum, Street
    self.toCall = toCall # int, Bet amount, amount to call
    self.pot = pot # int, Amount in pot
    self.potWithBets = potWithBets # int, Amount in pot, including bets in current street
    self.streetTotal = streetTotal # int, Amount in bets in current street
    self.handPlayers = handPlayers # int, Number of players in current hand
    self.cap = cap # int, Max bet that hand, empty for no limit cap
    self.dealerPosition = dealerPosition #int, Position of the dealer button

class Options():
  def __init__(self, dealerPosition, cap):
    self.dealerPosition = dealerPosition # Dealer position
    self.cap = cap # street cap

def initializeTable(seats, options):

  # Dealer position (option)
  if options.dealerPosition:
    dealerPosition = options.dealerPosition
  else:
    dealerPosition = seats

  # Cap (option)
  if options.cap:
    cap = options.cap
  else:
    cap = None

  table = []

  if seats <= 9: # Max 9 seats
    for i in seats:
      newPlayer = Player(i, False, 0)
      table.append(newPlayer)
  else:
    return "Too many players" # Catch too many players
  
  tableInfo = TableInfo(seats, seats, 0, 0, 0, 0, 0, seats, cap, dealerPosition)

  table.append(tableInfo)

options = Options(None, None)

seats = input("Input number of seats: ")
dealerPositionInput = input("Input dealer's seat position if any: ")

# Set dealer position to user's input, unless it was not possible, then default to seat var.
options.dealerPosition = dealerPositionInput if (0 < dealerPositionInput and dealerPositionInput <= seats) else seats

cap = input("Input street raise cap, if any: ")

# Set cap, default to None
