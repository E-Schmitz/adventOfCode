import numpy as np

# Read all rotations from a txt file saved from the website
with open('day_1_rotations', 'r') as raw:
    rotation_list = raw.read().splitlines()

test_rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

def calculateIdx(start_idx, rotation, dial):
    direction, amount = rotation [0], int(rotation[1:])
    count = amount // dial
    rest = amount % dial

    if direction == "L":
        # Modulo ensures no runtime overhead for large inputs
        idx = (start_idx - rest) % dial
        # Avoid edge cases where landing on 0 is counted twice
        if (rest > 0 and start_idx != 0 and rest >= start_idx):
            count +=1

        return idx, count
    
    elif direction == "R":
        idx = (start_idx + rest) % dial

        if (rest > 0 and start_idx != 0 and(start_idx + rest >= dial)):
            count +=1

        return idx, count
    else:
        print("Rotation direction is neither L or R")

 
def obtainPasscode(_rotations):
    # No actual array needed, just the length
    dial = 100
    # Starting index is given inside instructions (50)
    current_idx = 50
    # Counter for occurrences of 0
    total_count : int = 0

    for rot in _rotations:
        current_idx, temp_counter = calculateIdx(current_idx, rot, dial)
        total_count += temp_counter
        
    return total_count
    
print(obtainPasscode(rotation_list))
#print(obtainPasscode(test_rotations))

