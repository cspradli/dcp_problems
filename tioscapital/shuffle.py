def shuffle(amount, total_amount, deck, flag1, flag2):
    new_deck = []
    ## Base case for recursive call ##
    if(amount == 0):
        return new_deck
    bottom_half = deck[:26]
    top_half = deck[26:]
    ## Interleave the two halves together into deck ##
    for card in range(len(bottom_half)):
        new_deck.append(top_half[card])
        new_deck.append(bottom_half[card])
    print("%d / %d" % (total_amount - amount+1, total_amount))
    print(new_deck)
    if(flag2):
        ## Flag 2 represents to look for top and bottom cards touching problem ##
        for card in range(52):
            if new_deck[card] == 52 and (new_deck[card-1] == 1 or new_deck[card+1] == 1):
                print("Top and bottom are touching on shuffle number %d" % (total_amount+1 - amount))
                return new_deck
    if(flag1 and new_deck[0] == 52):
        ## Flag 1 represents to look for 52 on bottom ##
        print("52 on bottom at shuffle number %d" % (total_amount+1 - amount))
        return new_deck
    shuffle(amount-1, total_amount, new_deck, flag1, flag2)





## Initialize deck of cards
deck = []
set_number = 1
for _ in range(52):
    deck.append(set_number)
    set_number += 1
##What is the position of the first card after the 7th shuffle? ##
print("Look for first card on 7th shuffle")
shuffle(7, 7, deck, 0, 0)
## How many times must one perform the shuffle so that the top card is the bottom card ##
shuffle(50, 50, deck, 1, 0)
## When do the first and last cards touch
shuffle(50, 50, deck, 0, 1)