import math


class Integration:
    def __init__(self, a, b, n):
        self.N = n
        self.h = (b - a) / n
        self.x = []
        for i in range(self.N):
            self.x.append(a + i * self.h)

    def function(self, x):
        # TODO: create function input
        return math.sin(x)

    def integrate(self, rule):
        if rule == 'Rectangle':
            return self.rectangle_rule()
        elif rule == 'Trapezoidal':
            return self.trapezoidal_rule()

    def rectangle_rule(self):
        result = 0
        for i in range(self.N - 1):
            result = result + self.function((self.x[i] + self.x[i + 1]) / 2) * self.h
        return result

    def trapezoidal_rule(self):
        result = 0
        for i in range(self.N - 1):
            result = result + (self.function(self.x[i]) + self.function(self.x[i + 1])) / 2 * self.h
        return result
