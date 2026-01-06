data_source = 'day_2_id_ranges'
#data_source = 'test_ids'

def createRange(range_input):
    lwr, upr = map(int, range_input.split("-"))
    return range(lwr, upr +1)


def isInvalidId(current_range, part):
    s = str(current_range)
    length = len(s)

    if part == 1:
        if length % 2 != 0:
            return False
        mid = length // 2
        return s[:mid] == s[mid:]

    # Check for paterns of arbitrary length
    for n in range(1, length // 2 + 1):
        if length % n == 0:
            if s[:n] * (length // n) == s:
                return True
    return False


def getAllRanges(part):
    with open(data_source, 'r') as raw:
        id_ranges = raw.read().strip().split(",")

    total = 0
    for r in id_ranges:
        for curr_id in createRange(r):
            if isInvalidId(curr_id, part):
                total += curr_id

    return total


print("Result for part 1: ", getAllRanges(part=1))
print("Result for part 2: ", getAllRanges(part=2))



