from art_logo import logo

print(logo)



bidding_network = {}

other_bidders = True
while other_bidders:
    print("Welcome to the Bidding Network")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))


    bidding_network[name] = bid


    other_bidders = input(
        "Are there any others who want to bid? Type 'yes' if there are, otherwise type 'no': ").lower()

    print("\n" * 30)


    if other_bidders == 'no':
        break  # Exit the loop


def find_highest_bidder():
    max_bidder = max(bidding_network, key=bidding_network.get)  # Get the key (name) with the highest value (bid)
    highest_bid = bidding_network[max_bidder]  # Get the highest bid value
    print(f"{max_bidder} has the highest bid amount of ${highest_bid}")


find_highest_bidder()

