from RandomOperations import *


class RandomGenerator:
    # Initialization:
    def __init__(self):
        pass

    # Object Methods:
    def getRandIntRange(self, start, end):
        return getRandIntRange(start, end)

    def getRandIntRangeWithSeed(self, start, end, seed):
        return getRandIntRangeWithSeed(start, end, seed)

    def getRandFloatRange(self, start, end):
        return getRandFloatRange(start, end)

    def getRandFloatRangeWithSeed(self, start, end, seed):
        return getRandFloatRangeWithSeed(start, end, seed)

    def getRandIntListWithSeed(self, start, end, size, seed):
        return getRandIntListWithSeed(start, end, size, seed)

    def getRandFloatListWithSeed(self, start, end, size, seed):
        return getRandFloatListWithSeed(start, end, size, seed)