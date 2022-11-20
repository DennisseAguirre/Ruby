from RecursosPly import yacc
from analizadorLexico import tokens


# Crear las siguientes reglas

# 6. Cuerpo

def p_cuerpo(p):
    '''cuerpo : cuerpoF
    | tiposfuncion
    | estructuracontrol
    '''


def p_cuerpoF(p):
    '''cuerpoF : asignacion
    | operacionesmate
    | comparaciones
    '''

def p_tiposfuncion(p):
    '''tiposfuncion : funcionparametro
    | funcionsinparametro

    '''


def p_estructuradatos(p):
    '''estructuracontrol : array
     '''
    #

def p_tipodato(p):
    '''tipodato : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    '''

# ___________________________Asignación de variables- (Alcivar) _______________________

def p_asignacion(p):
    "asignacion : variable IGUAL tipodato"


def p_variable(p):
    '''variable : TOKEN_VARIABLE_GLOBAL
    | TOKEN_VARIABLE_INSTANCIA
    | TOKEN_VARIABLE_LOCAL
    | TOKEN_CONSTANTE
    | TOKEN_VARIABLE_DE_CLASE'''




#___________________________ Operaciones matemáticas (Aguirre)_______________________________
def p_valormate(p):
    '''valormate : ENTERO
        | FLOAT
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
#__________________________ Comparaciones (Allison Recalde)_______
def p_comparaciones(p):
    "comparaciones : valormate operadores_comparacion valormate"
def p_operadores_comparacion(p):
    ''' operadores_comparacion : IGUAL_COMPARACION
    | DIFERENTE
    | MAYOR_QUE
    | MENOR_QUE
    | MAYOR_IGUAL
    | MENOR_IGUAL'''
# Definicion de funcion
#___________________________ Funciones que reciben 0 o n parámetros (Aguirre)_____________________

def p_funcionparametro(p):
    "funcionparametro : DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER cuerpoF END"

def p_funcionsinparametro(p):
    "funcionsinparametro : DEF TOKEN_NOMBRE_FUNCION cuerpoF END"

def p_parametro(p):
    '''parametro : variable
    | variable COMA parametro
    '''

#__________________________ Estructura de datos : Array (Aguirre)  ______________________________________________

def p_array(p):
    "array : CORCHETE_IZQ elemento CORCHETE_DER"

def p_elemento(p):
    '''elemento : tipodato
        | tipodato COMA elemento
    '''









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