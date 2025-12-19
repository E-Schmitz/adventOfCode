import numpy as np

# Read all rotations from a txt file saved from the website
with open('day_1_rotations', 'r') as raw:
    rotation_list = raw.read().splitlines()


def performRotation(start_idx, rotation, dial):
    direction, amount = rotation [0], int(rotation[1:])

    current_idx = calculateIdx(start_idx, direction, amount, dial)

    return current_idx


def calculateIdx(start_idx, direction, amount, dial):
    temp = start_idx

    if direction == "L":
        # Modulo ensures no runtime overhead for large inputs
        temp = (temp -amount) % len(dial)
        return temp
    
    elif direction == "R":
        temp = (temp + amount) % len(dial)
        return temp
    else:
        print("Rotation direction is neither L or R")


#### Summary 
# Takes a list of rotation inputs and returns the amount of times the index pointed to 0
####    
def obtainPasscode(_rotations):
    # Range set to 100, to include all int 0 to 99
    dial = np.arange(0,100)
    # Starting index is given inside instructions (50)
    current_idx = 50
    # Counter for occurrences of 0
    counter : int = 0

    for rot in _rotations:
        current_idx = performRotation(current_idx, rot, dial)
        if current_idx == 0:
            counter += 1

    return counter
    
print(obtainPasscode(rotation_list))

