import random

class NumberGenerator:
    def __init__(self):
        pass

    # first precondition: all inputs must be integers
    def num_gen(self, amount: int, minRange: int, maxRange: int): 

        # second precondition: minRange must be lower than maxRange
        assert minRange < maxRange  

        self.amount = amount
        self.minRange = minRange
        self.maxRange = maxRange
        self.num_list = []

        # code produces random numbers according to given parameters
        self.num_list = [random.randint(minRange, maxRange) for x in range(amount)] 

        # first postcondition: check if the variable num_list has the correct type
        assert isinstance(self.num_list, list)

        # second postcondition: check if the correct amount of numbers is represented in the list 
        assert len(self.num_list) == self.amount 

        return self.num_list

gen = NumberGenerator()
random_numbers = gen.num_gen(10,1,5)
print(random_numbers)