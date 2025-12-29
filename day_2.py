def createRange(range_input):
    lwr, upr = range_input.split("-")
    lwr = int(lwr)
    upr = int(upr)
    current_range = range(lwr, upr +1)

    return current_range


def detectDub(current_id, invalid_ids):

    id_list = list(map(int, str(current_id)))
    mid = len(id_list)//2
    fst = id_list[:mid]
    lst = id_list[mid:]

    if fst == lst:
        invalid_ids.append(int(current_id))

    return invalid_ids


def getAllRanges():
    with open('day_2_id_ranges', 'r') as raw:
        # Remove \n and whitespaces before split
        id_ranges = raw.read().strip().split(",")
        invalid_ids = []

    for r in id_ranges:
        current_range = createRange(r)
        for curr_r in current_range:
            invalid_ids = detectDub(curr_r, invalid_ids)

    return sum(invalid_ids)


print(getAllRanges())



