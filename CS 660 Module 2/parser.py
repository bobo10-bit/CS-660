"""
Simple Arithmetic Interpreter
TODO: Define grammar rules for arithmetic expressions with +, -, *, and parentheses
"""

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Parser:
    def __init__(self, expression):
        self.expr = expression.replace(' ', '')
        self.pos = 0
        self.current_char = self.expr[0] if self.expr else None

    def advance(self):
        self.pos += 1
        self.current_char = self.expr[self.pos] if self.pos < len(self.expr) else None

    def parse_number(self):
        # TODO: Parse integer and return NumberNode
        # Parse consecutive digits into a complete integer
        number = ""
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        # Return the integer value as a NumberNode
        return NumberNode(int(number))

    def parse_factor(self):
        # TODO: Implement factor parsing
        # if the current character is a digit, parse it as a number
        if self.current_char.isdigit():
            return self.parse_number()

        # if the current character is an opening parenthesis, parse the expression inside the parentheses
        elif self.current_char == "(":
            self.advance()
            node = self.parse_expression()

            # skip the closing parenthesis
            if self.current_char == ")":
                self.advance()

            return node

        # If there is a invalid input such as letters or symbols, raise an exception
        raise Exception("Invalid factor")

    def parse_term(self):
        # TODO: Implement term parsing  
        # parse the first factor
        node = self.parse_factor()

        # Contiue parsing while the current character is a multiplication operator
        while self.current_char == "*":
            op = self.current_char
            self.advance()
            right = self.parse_factor()
            # Buils a binary operation node for each multiplication operation
            node = BinaryOpNode(node, op, right)

        return node

    def parse_expression(self):
        # TODO: Implement expression parsing
        # parse the first term
        node = self.parse_term()

        # Continue parsing while the current character is an addition or subtraction operator
        while self.current_char in ("+", "-"):
            op = self.current_char
            self.advance()
            right = self.parse_term()
            # build a binary operation node for each addition or subtraction operation
            node = BinaryOpNode(node, op, right)

        return node

def evaluate(node):
    # TODO: Evaluate AST node recursively
    # return the value if the node is a number
    if isinstance(node, NumberNode):
        return node.value
    # evaluate the left and right sides of the operation
    elif isinstance(node, BinaryOpNode):
        left = evaluate(node.left)
        right = evaluate(node.right)

        # Do the operation based on the operator
        if node.op == "+":
            return left + right
        elif node.op == "-":
            return left - right
        elif node.op == "*":
            return left * right

    # raise an exception if the node type is invalid
    raise Exception("Invalid AST")

def interpret(expression):
    parser = Parser(expression)
    ast = parser.parse_expression()
    return evaluate(ast)

# Test cases
if __name__ == "__main__":
    test_expressions = [
        "42",
        "2 + 3",
        "10 - 4",
        "3 * 7",
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "1 + 2 + 3",
        "10 - 5 - 2",
        "((1 + 2) * 3) - 4",
    ]

    # TODO: Change Name to your name
    print("Christopher Wilson")
    print("Arithmetic Interpreter Test")
    for expr in test_expressions:
        try:
            result = interpret(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"Error interpreting '{expr}': {e}")
