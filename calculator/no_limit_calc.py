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

def initializeTable(seats, table, options):

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

  if seats <= 9:
    for i in seats:
      newPlayer = Player(i, False, 0)
      table.append(newPlayer)
  else:
    return "Too many players"
  
  tableInfo = TableInfo(seats, seats, 0, 0, 0, 0, 0, seats, cap, dealerPosition)