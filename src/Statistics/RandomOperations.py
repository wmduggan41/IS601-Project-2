import random


def getRandIntRange(start, end):
    return random.randrange(start, end)


def getRandIntRangeWithSeed(start, end, seed):
    random.seed(seed)
    return random.randrange(start, end)


def getRandFloatRange(start, end):
    return random.uniform(start, end)


def getRandFloatRangeWithSeed(start, end, seed):
    random.seed(seed)
    return random.uniform(start, end)


def getRandIntListWithSeed(start, end, size, seed):
    rand_list = []
    i = 0
    while i < size:
        rand_list.append(getRandIntRangeWithSeed(start, end, seed))
        i += 1
    return rand_list


def getRandFloatListWithSeed(start, end, size, seed):
    rand_list = []
    i = 0
    while i < size:
        rand_list.append(getRandFloatRangeWithSeed(start, end, seed))
        i += 1
    return rand_list
