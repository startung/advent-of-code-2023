hands = {}
with open("input", "r") as f:
    while line := f.readline():
        hands[line[:-1].split(" ")[0]] = int(line[:-1].split(" ")[1])

output = 0

def hand_value(hand):
    ordering = 0
    card_rank = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J': 1}
    for idx, card in enumerate(hand[::-1]):
        ordering += card_rank[card[0]]*100**idx
    # Five of a kind, where all five cards have the same label: AAAAA
    if hand.count(hand[0]) == 5:
        return 6 * 10000000000 + ordering
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        if hand.count('J') > 0: # Now five of a kind
            return 6 * 10000000000 + ordering
        return 5 * 10000000000 + ordering
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    if len(set(hand)) == 2:
        if 'J' in hand: # Now five of a kind
            return 6 * 10000000000 + ordering
        return 4 * 10000000000 + ordering
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
        if 'J' in hand: # Now four of a kind
            return 5 * 10000000000 + ordering
        return 3 * 10000000000 + ordering
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if len(set(hand)) == 3:
        if hand.count('J') == 1: # Now full house
            return 4 * 10000000000 + ordering
        if hand.count('J') == 2: # Now four of a kind
            return 5 * 10000000000 + ordering
        return 2 * 10000000000 + ordering
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if len(set(hand)) == 4:
        if 'J' in hand: # Now three of a kind
            return 3 * 10000000000 + ordering
        return 10000000000 + ordering
    # High card, where all cards' labels are distinct: 23456
    if 'J' in hand: # Now pair
        return 10000000000 + ordering
    return ordering


for idx, key in enumerate(sorted(hands, key=hand_value)):
    print(idx+1, key, hands[key])
    output += (idx+1)* hands[key]

print(output)