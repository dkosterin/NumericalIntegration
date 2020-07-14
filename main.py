from Integration import Integration

integration = Integration(0, 3.14159, 10000)
result = integration.integrate('Trapezoidal')
print(result)
