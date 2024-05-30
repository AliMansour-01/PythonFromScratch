#python Dictionaries, and Nesting


from secret_auction_art import logo

print(logo)

def clear():
    print("\n" * 100)

def find_winner(auction_record):
    highest_bid = 0
    for key in auction_record:
        current_bid = auction_record[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = key
    print(f"The winner is {winner} with a bid of {highest_bid}")


continue_bidding = True
while continue_bidding == True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    empty_bid = {}
    empty_bid[name] = bid
    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if continue_auction == "no":
        continue_bidding = False
        find_winner(empty_bid)
    else:
        clear()