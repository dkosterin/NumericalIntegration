class Token:
    def __init__(self, value, type, arguments):
        self.value = value
        self.type = type
        self.arguments = arguments[:]