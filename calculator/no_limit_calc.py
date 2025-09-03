from enum import Enum

class Street(Enum):
  PREFLOP = 0
  FLOP = 1
  TURN = 2
  RIVER = 3

class Player():
  def __init__(self, position, folded, street_bet):
    self.position = position # int, Seat position 
    self.folded = folded # bool, true = not in hand, false = in hand
    self.street_bet = street_bet # int, Amount bet in current street

class Table_info():
  def __init__(self, players, street, to_call, pot, pot_with_bets, street_total, hand_players, cap, dealer_position):
    self.players = players # int, Number of players in game
    self.street = street # enum, Street
    self.to_call = to_call # int, Bet amount, amount to call
    self.pot = pot # int, Amount in pot
    self.pot_with_bets = pot_with_bets # int, Amount in pot, including bets in current street
    self.street_total = street_total # int, Amount in bets in current street
    self.hand_players = hand_players # int, Number of players in current hand
    self.cap = cap # int, Max bet that hand, empty for no limit cap
    self.dealer_position = dealer_position #int, Position of the dealer button

def initialize_table(seats, table, options):

  # Dealer position (option)
  if options.dealer_position:
    dealer_position = options.dealer_position
  else:
    dealer_position = seats

  # Cap (option)
  if options.cap:
    cap = options.cap
  else:
    cap = None

  if seats <= 9:
    for i in seats:
      new_player = Player(i, False, 0)
      table.append(new_player)
  else:
    return "Too many players"
  
  table_info = Table_info(seats, seats, 0, 0, 0, 0, 0, seats, cap, dealer_position)