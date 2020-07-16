from Parser import Parser
import numpy as np
import math


class Integration:
    def __init__(self, func, a, b, n):
        self.input_string = func
        self.N = n
        self.h = (b - a) / n
        self.x = np.linspace(a, b, n)
        # for i in range(self.N):
        #     self.x.append(a + i * self.h)

    def evaluation(self, token, x):
        arguments = token.arguments
        if token.type == 'Operation':
            if token.value == '*':
                return self.evaluation(arguments[0], x) * self.evaluation(arguments[1], x)
            elif token.value == '+':
                return self.evaluation(arguments[0], x) + self.evaluation(arguments[1], x)
            elif token.value == '-':
                return self.evaluation(arguments[0], x) - self.evaluation(arguments[1], x)
            elif token.value == '/':
                return self.evaluation(arguments[0], x) / self.evaluation(arguments[1], x)
            elif token.value == '^':
                return self.evaluation(arguments[0], x) ** self.evaluation(arguments[1], x)
            else:
                raise Exception('Bad operation token')
        elif token.type == 'Function':
            if token.value == 'sin':
                return math.sin(x)
            elif token.value == 'cos':
                return math.cos(x)
            elif token.value == 'log':
                return math.log(x)
            elif token.value == 'tan':
                return math.tan(x)
            elif token.value == 'ctan':
                return 1 / math.tan(x)
            elif token.value == 'exp':
                return math.exp(x)
            else:
                raise Exception('Bad function token')
        elif token.type == 'Number':
            return float(token.value)
        elif token.type == 'Variable':
            return x
        else:
            raise Exception('Bad token type')

    def function(self, x):
        p = Parser(self.input_string)
        result = p.parse()
        return self.evaluation(result, x)

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
