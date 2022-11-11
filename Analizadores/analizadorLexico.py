from RecursosPly.lex import lex

palabrasReservadas = {

}

tipoDatos = {

}

tokens = [
    #tokens de simbolos
    "MAS",
    "MENOS",
    "DIVISION",
    "MULTIPLICACION",
    "MODULO",
    "POTENCIA",
    "PAREN_DER",
    "PAREN_IZQ",
    "CORCHETE_DER",
    "CORCHETE_IZQ",
    "LLAVE_DER",
    "LLAVE_IZQ",
    "IGUAL_COMPARACION",
    "DIFERENTE",
    "MAYOR_QUE",
    "MENOR_QUE",
    "MAYOR_IGUAL",
    "MENOR_IGUAL",
    "IGUAL",
    "COMA",
    "PUNTO",

    #tokens de variables
    "TOKEN_VARIABLE_GLOBAL",
    "TOKEN_VARIABLE_INSTANCIA",
    "TOKEN_VARIABLE_LOCAL",
    "TOKEN_CONSTANTE",
    "TOKEN_VARIABLE_DE_CLASE"
] + list(palabrasReservadas.values()) + list(tipoDatos.values())

# --------------------Operadores aritmeticos --------------------
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_POTENCIA = r'\*\*'
# --------------------Simbolos de agrupacion--------------------
t_PAREN_DER = r'\)'
t_PAREN_IZQ = r'\('
t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_DER = r'\}'
t_LLAVE_IZQ = r'\{'

# --------------------Operadores de comparacion--------------------
t_IGUAL_COMPARACION = r'=='
t_DIFERENTE = r'!='
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='

# --------------------Simbolos--------------------
t_COMA = r','
t_PUNTO = r'\.'

# --------------------Operadores de asignacion--------------------
t_IGUAL = r'='

#--------------------Funciones de definir variable--------------------
def t_TOKEN_VARIABLE_GLOBAL(t):
    r'\$[a-z][a-zA-Z0-9]*'
    t.type = palabrasReservadas.get(t.value, tipoDatos.get(t.value, "TOKEN_VARIABLE_GLOBAL"))
    return t

def t_TOKEN_VARIABLE_DE_CLASE(t):
    r'@@[a-z_][a-zA-Z0-9]*'
    t.type = palabrasReservadas.get(t.value, tipoDatos.get(t.value, "TOKEN_VARIABLE_DE_CLASE"))
    return t

def t_TOKEN_VARIABLE_INSTANCIA(t):
    r'@[a-z][a-zA-Z0-9]*'
    t.type = palabrasReservadas.get(t.value, tipoDatos.get(t.value, "TOKEN_VARIABLE_INSTANCIA"))
    return t

def t_TOKEN_VARIABLE_LOCAL(t):
    r'([a-z][a-zA-Z0-9]*)|(_[a-zA-Z0-9]+)'
    t.type = palabrasReservadas.get(t.value, tipoDatos.get(t.value, "TOKEN_VARIABLE_LOCAL"))
    return t

def t_TOKEN_CONSTANTE(t):
    r'[A-Z]+'
    t.type = palabrasReservadas.get(t.value, tipoDatos.get(t.value, "TOKEN_CONSTANTE"))
    return t

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENTS(t):
  r'\#.*'
  pass
  
# Error handling rule
def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)
 
 # Build the lexer
lexer = lex()

def getTokens(lexer):
  for tok in lexer:
    print(tok)


linea = " "

while linea != "":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")