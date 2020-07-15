from Token import Token

class Parser:
    #TODO: fix expressions with one ); 1)+); Bad things with )
    def __init__(self, input_string):
        self.input_string = input_string
        self.variable = 'x'
        self.tokens = ["+", "-", "*", "/", "^", "(", ")", "sin", "cos", "log", "tan", "atan", "exp", "ctan"]
        self.unary_operations = ["-", "sin", "cos", "log", "tan", "atan", "exp", "ctan"]
        self.binary_operations = ["+", "-", "*", "/", "^", ")"]

    def parse(self):
        return self.parse_binary_operations(0)

    def parse_token(self):
        if not self.input_string:
            return ''
        if self.input_string[0].isdigit():
            number = ''
            i = 0
            while i < len(self.input_string) and (self.input_string[i].isdigit() or self.input_string[i] == '.'):
                number = number + self.input_string[i]
                i = i + 1
            self.input_string = self.input_string[i:]
            return number
        elif self.input_string[0] == self.variable:
            self.input_string = self.input_string[1:]
            return self.variable
        else:
            for token in self.tokens:
                if len(token) <= len(self.input_string):
                    substr = self.input_string[:len(token)]
                    if substr == token:
                        self.input_string = self.input_string[len(token):]
                        return token
            return ''

    def is_digit(self, str):
        if str.isdigit():
            return True
        else:
            try:
                float(str)
                return True
            except ValueError:
                return False

    def parse_simple_expression(self):
        token = self.parse_token()
        if not token:
            raise Exception('Input error')
        if self.is_digit(token):
            return Token(token, 'Number', [])
        if token == self.variable:
            return Token(token, 'Variable', [])
        if token == '(':
            result = self.parse()
            next_token = self.parse_token()
            if next_token != ')':
                raise Exception('Expected )')
            return result
        if token not in self.unary_operations:
            raise Exception('Input error')
        arguments = [self.parse_simple_expression()]
        return Token(token, 'Function', arguments)

    def get_priority(self, token):
        if token == "+":
            return 1
        elif token == "-":
            return 1
        elif token == "*":
            return 2
        elif token == "/":
            return 2
        elif token == "^":
            return 3
        else:
            return 0

    def parse_binary_operations(self, priority):
        left_operand = self.parse_simple_expression()
        while True:
            operation = self.parse_token()
            if self.input_string and operation not in self.binary_operations:
                raise Exception('Input error')
            operation_priority = self.get_priority(operation)
            if operation_priority <= priority:
                self.input_string = operation + self.input_string
                return left_operand
            right_operand = self.parse_binary_operations(operation_priority)
            left_operand = Token(operation, 'Operation', [left_operand, right_operand])
