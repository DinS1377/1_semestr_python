nmb = ["0", "1", '2', '3', '4', '5', '6', '7', '8']

def aa(nmb):
    nmb_2 = []
    for i in range(0, len(nmb)-1):
        nmb_2.append(nmb(i))
    return nmb_2

print(aa(nmb))

