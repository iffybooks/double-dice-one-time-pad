# Double Dice One-Time Pad Encoder/Decoder Generator Script
# wtfpl 2025

import itertools

die_sides = ['1','2','3','4','5','6']

die_pairs = []

for num_1 in die_sides:
    for num_2 in die_sides:
        die_pairs.append(num_1+num_2)

## Encoder sheet

print("Encoder sheet:")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for i in range(len(characters)):
    print(str(die_pairs[i] + "  " + " ".join(characters[i:] + characters[:i])))

print('\n' * 2)


## Decoder sheet

print("Decoder sheet:")

for i in range(len(characters)):
    print((['11']+die_pairs[::-1])[i] + "  " + " ".join(characters[i:] + characters[:i]))

print('\n' * 2)

## Cursor strips

print("Cursor strips:\n\n")


for i in range(3):
    print(" ".join("  ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))

    print('\n' * 2)

