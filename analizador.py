import ply.lex as lex

# lista de tokens
tokens = (
    'NUMBERS','FLOAT',
    'OPMAS','OPMENOS','OPMULTIPLICAR','OPDIVISOR','OPIGUAL',
    'LPAREN','RPAREN','SEMICOLON'
)

reserved = {
    'while' : 'WHILE',
    'else' : 'ELSE',
    'if' : 'IF',
    'for' : 'FOR',
    'switch':'SWITCH',
    'case':'CASE',
    'do' : 'DO',
    'break': 'BREAK',
    'return' : 'RETURN',
    'int' : 'INT',
    'float' : 'FLOAT',
    'double' : 'DOUBLE',
    'continue' : 'CONTINUE',
    'struct' : 'STRUCT',
    'union' : 'UNION',
    'char' : 'CHAR',
    'alignas':'ALIGNAS',
    'alignof':'ALIGNOF',
    'and':'AND',
    'and_eq':'AND_EQ',
    'asm':'ASM',
    'auto':'AUTO',
    'bitand':'BITAND',
    'constinit':'CONSTINIT',
    'continue':'CONTINUE',
    'co_await':'CO_AWAIT',
    'co_return':'CO_RETURN',
    'co_yield':'CO_YIELD',
    'decltype':'DECLTYPE',
    'default':'DEFAULT',
    'long':'LONG',
    'mutable':'MUTABLE',
    'namespace':'NAMESPACE',
    'new':'NEW',
    'noexcept':'NOEXCEPT',
    'not':'NOT',
    'static_assert':'STATIC_ASSERT',
    'static_cast':'STATIC_CAST',
    'struct':'STRUCT',
    'switch':'SWITCH',
    'template':'TEMPLATE',
    'this':'THIS',
    'thread_local':'THREAD_LOCAL'
 }
# Regular expression rules for simple tokens
t_OPMAS = r'\+'
t_OPMENOS = r'-'
t_OPMULTIPLICAR = r'\*'
t_OPDIVISOR = r'/'
t_OPIGUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

def t_NUMBERS(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
23+2.5;
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)