from RecursosPly import yacc
from analizadorLexico import tokens


# Crear las siguientes reglas

# 6. Cuerpo

def p_cuerpo(p):
    '''cuerpo : cuerpoF
    | funcionparametro'''


def p_cuerpoF(p):
    '''cuerpoF : asignacion
    | impresion
    | operacionesmate
    '''


# ___________________________Asignación de variables- (Alcivar) _______________________

def p_asignacion(p):
    "asignacion : variable IGUAL valor"


def p_variable(p):
    '''variable : TOKEN_VARIABLE_GLOBAL
    | TOKEN_VARIABLE_INSTANCIA
    | TOKEN_VARIABLE_LOCAL
    | TOKEN_CONSTANTE
    | TOKEN_VARIABLE_DE_CLASE'''


def p_valor(p):
    '''valor : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    | variable'''

#___________________________ Operaciones matemáticas (Aguirre)_______________________________
def p_valormate(p):
    '''valormate : ENTERO
        | FLOAT
        | variable
    '''

def p_signosmate(p):
    '''signosmate : MAS
    | MENOS
    | MULTIPLICACION
    | DIVISION
    | MODULO
    | POTENCIA
    '''

def p_operacionesmate(p):
    "operacionesmate : valormate signosmate valormate"


# Definicion de funcion
#___________________________ Funciones que reciben 0 o n parámetros (Aguirre)_____________________

def p_funcionparametro(p):
    "funcionparametro : DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER cuerpoF END"

def p_parametro(p):
    '''parametro : variable
    | variable COMA parametro
    '''


# 3. Impresion
def p_impresion(p):
    'impresion : PRINT valor'


# 4. Entrada de datos


# 5. Tipos de datos


def p_error(p):
    if p:
        print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        parser.errok()
    else:
        print("Error de sintaxis Fin de Linea")


# Build the parser
parser = yacc.yacc()


def validaRegla(s):
    result = parser.parse(s)
    print(result)


while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    validaRegla(s)