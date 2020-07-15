from Integration import Integration
from Parser import Parser

integration = Integration('exp(x)-1', 0, 1, 10000)
result = integration.integrate('Trapezoidal')
print(result)
# s = '-3^(sin(x)+2*cos(2*x))+4'
# p = Parser(s)
# res = p.parse()
# print(res)