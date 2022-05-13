from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
def add_bidder(bidder_name, bid_given):
  bidders[bidder_name] = bid_given
  
other_bidder = True
while other_bidder:
  name = input("What is your name?: ")
  bid_value = int(input("what's your bid?: ₹"))
  check = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  add_bidder(name, bid_value)
  if check == "no":
    other_bidder = False
    max_bid = 0
    for bid in bidders:
      score = bidders[bid]
      if score >= max_bid:
        max_bid = score
        max_bidder = bid
    print(f"The winner is {max_bidder} with a bid of ₹{max_bid}.")
  elif check == "yes":
    clear()
  else:
    print("Wrong key pressed.")

