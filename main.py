import numpy as np
import matplotlib.pyplot as plt
from Integration import Integration
from Parser import Parser

#TODO: add user interface
a = 0
b = 3.14159
integration = Integration('sin(x)', a, b, 10000)
result = integration.integrate('Trapezoidal')
print(result)
x = np.linspace(a - 0.25, b + 0.25, 50)
y = [integration.function(i) for i in x]
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
x = integration.x
y = [integration.function(i) for i in x]
plt.fill_between(x, 0, y, facecolor='g', alpha=0.5)
plt.show()
# s = '-3^(sin(x)+2*cos(2*x))+4'
# p = Parser(s)
# res = p.parse()
# print(res)