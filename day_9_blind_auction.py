import os 

bids = {}
    
def clear(): os.system("clear")

while True:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))

    bids[name] = bid

    restart = input("Type \"yes\" if there are other users who want to place bids: ").lower()

    if restart != "yes":
        break

    clear()

winner = None
largest = 0
for name in bids:
    if bids[name] > largest:
        largest = bids[name]
        winner = name

print(f"{winner} won the blind auction with a bid of ${'{0:.2f}'.format(largest)}!")
print(bids)