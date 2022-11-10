class NegativeSumError(Exception):
    def __init__(self):
        self.message = "The sum of the numbers is negative"
        super().__init__(self.message)
def sum_with_exceptions(a, b):
    totalSum = a + b
    if totalSum < 0:
        raise NegativeSumError()
    return totalSum