from Calculator import Calculator
from StatsOperations import *


class StatsCalculator(Calculator):
    def __init__(self):
        Calculator.__init__(self)

    # Object Methods:
    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def variance(self, a):
        self.result = variance(a)
        return self.result

    def std_dev(self, a):
        self.result = std_dev(a)
        return self.result