from string import ascii_uppercase

AZ = dict(zip(' ' + ascii_uppercase, xrange(27)))


def quicksum(packet):
    result = 0
    for i, a in enumerate(packet, 1):
        try:
            result += AZ[a] * i
        except KeyError:
            return 0
    return result


assert quicksum('ACM') == 46
assert quicksum('A C M') == 75
assert quicksum('AbqTH #5') == 0
