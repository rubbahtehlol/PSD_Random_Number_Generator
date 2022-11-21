import random

class NumberGenerator:
    def __init__(self):
        pass

    def num_gen(self, amount: int, minRange: int, maxRange: int): # first precondition: all inputs must be integers
        assert minRange < maxRange  # second precondition: minRange must be lower than maxRange

        self.amount = amount
        self.minRange = minRange
        self.maxRange = maxRange

        return [random.randint(minRange, maxRange) for x in range(amount)]

gen = NumberGenerator()
random_numbers = gen.num_gen(10,1,5)
print(random_numbers)