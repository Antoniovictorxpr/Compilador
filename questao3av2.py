import random

# Classe Token
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Classe Lexer
class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.pos = 0
        self.current_char = self.input_string[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.input_string):
            self.current_char = self.input_string[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_number(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token("NUMBER", self.get_number())
            if self.current_char == "+":
                self.advance()
                return Token("PLUS", "+")
            if self.current_char == "-":
                self.advance()
                return Token("MINUS", "-")
            if self.current_char == "*":
                self.advance()
                return Token("TIMES", "*")
            if self.current_char == "/":
                self.advance()
                return Token("DIVIDE", "/")
            if self.current_char == "(":
                self.advance()
                return Token("LPAREN", "(")
            if self.current_char == ")":
                self.advance()
                return Token("RPAREN", ")")
            if self.current_char.isalpha():
                token = Token("ID", self.current_char)
                self.advance()
                return token
            raise Exception("Caractere inválido: " + self.current_char)
        return Token("EOF", None)

# Classe Parser
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception("Erro de sintaxe: Esperado token do tipo " + token_type)

    def factor(self):
        token = self.current_token
        if token.type == "LPAREN":
            self.eat("LPAREN")
            result = self.expression()
            self.eat("RPAREN")
        elif token.type == "MINUS":
            self.eat("MINUS")
            result = -self.factor()
        elif token.type == "NUMBER":
            self.eat("NUMBER")
            result = token.value
        elif token.type == "ID":
            self.eat("ID")
            result = get_variable_value(token.value)
        else:
            raise Exception("Erro de sintaxe: Token inesperado " + token.type)
        return result

    def term(self):
        result = self.factor()
        while self.current_token.type in ["TIMES", "DIVIDE"]:
            token = self.current_token
            if token.type == "TIMES":
                self.eat("TIMES")
                result *= self.factor()
            elif token.type == "DIVIDE":
                self.eat("DIVIDE")
                divisor = self.factor()
                if divisor == 0:
                    raise Exception("Erro: Divisão por zero")
                result /= divisor
        return result

    def expression(self):
        result = self.term()
        while self.current_token.type in ["PLUS", "MINUS"]:
            token = self.current_token
            if token.type == "PLUS":
                self.eat("PLUS")
                result += self.term()
            elif token.type == "MINUS":
                self.eat("MINUS")
                result -= self.term()
        return result

    def parse(self):
        return self.expression()

# Função auxiliar para obter o valor de uma variável
def get_variable_value(variable):
    # Implemente a lógica para obter o valor da variável
    # Aqui você pode acessar uma tabela de símbolos, um dicionário, etc.
    variables = {'x': random.randint(1, 10), 'y': random.randint(1, 10), 'z': random.randint(1, 10),
                 'a': random.randint(1, 10), 'b': random.randint(1, 10)}
    return variables.get(variable, 0)

# Função para obter a entrada do usuário
def get_user_input():
    return input("Digite uma expressão matemática: ")

# Loop principal
while True:
    input_string = get_user_input()
    if input_string == "exit":
        break
    lexer = Lexer(input_string)
    parser = Parser(lexer)
    result = parser.parse()
    print("Resultado:", result)
