from RecursosPly import yacc
from analizadorLexico import tokens

# Crear las siguientes reglas

# 6. Cuerpo
def p_cuerpo(p):
    '''cuerpo : cuerpoF
    | tiposfuncion
    | estructuradatos
    | estructuracase
    | pedirporteclado
    | estructurahash
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
    '''estructuradatos : array
    | conjunto
     '''
    #

def p_estructuracontrol(p):
    '''estructuracontrol : ifelse
       | sentencias_while
        '''



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


#___________________________ Operaciones matemáticas (Dennisse Aguirre)_______________________________
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
    '''operacionesmate : valormate signosmate valormate
                       | valormate signosmate operacionesmate
    '''
#__________________________ Comparaciones (Allison Recalde)_______
def p_comparaciones(p):
    "comparaciones : valormate mas_comparaciones"


def p_mas_comparaciones(p):
    '''mas_comparaciones : operadores_comparacion valormate
                                   | operadores_comparacion valormate mas_comparaciones
    '''
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
#_________________________ Estructura de control______________
#BUCLE WHILE____ (Allison Recalde)
def p_condicion(p):
    '''
    condicion : BOOLEAN
                 | comparaciones
    '''


def p_sentencias_while(p):
    '''
    sentencias_while : WHILE condicion DO
               | WHILE condicion
               | WHILE PAREN_IZQ condicion PAREN_DER DO
               | WHILE PAREN_IZQ condicion PAREN_DER
    '''

#IF ELSE ____ _____(Dennisse Aguirre)_________________________________________
def p_ifelse(p):
    '''
            ifelse : IF cond ELSE END
             | IF multicond ELSE END
             | IF multicond cuerpoF ELSE cuerpoF END
             | IF cond cuerpoF ELSE cuerpoF END
             '''

def p_valorencondiciones(p):
    '''
         valorencondiciones : valormate
          | TOKEN_VARIABLE_LOCAL
          '''

def p_cond(p):
    "cond : valorencondiciones operadores_comparacion valorencondiciones"

def p_operadoreslogicos(p):
    '''
          operadoreslogicos : AND_OP
          | OR_OP
          '''

def p_multicond(p):
    '''
            multicond : cond operadoreslogicos cond
             | cond operadoreslogicos multicond
             '''



#__________________________ Estructura de datos  ______________________________________________
#Array____________ (Dennisse Aguirre)__________________________________
def p_array(p):
    "array : CORCHETE_IZQ elemento CORCHETE_DER"

def p_elemento(p):
    '''elemento : tipodato
        | tipodato COMA elemento
    '''

def p_funcion_length(p):
    '''
    array : TOKEN_VARIABLE_LOCAL PUNTO LENGTH
    '''
def p_funcion_push(p):
    '''
   array : TOKEN_VARIABLE_LOCAL PUNTO PUSH PAREN_IZQ ENTERO PAREN_DER
    '''

def p_obtener_elemento(p):
    '''
   array : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ ENTERO CORCHETE_DER
    '''

def p_funcion_first(p):
    '''
    array : TOKEN_VARIABLE_LOCAL PUNTO FIRST PAREN_IZQ PAREN_DER
    '''


#Set ______________(Allison Recalde)_____________________________________________
def p_conjunto(p):
    'conjunto : SET CORCHETE_IZQ elemento CORCHETE_DER'

#Metodos de la estructura SET (Allison Recalde)
def p_funcion_clear(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO CLEAR PAREN_IZQ PAREN_DER
    | TOKEN_VARIABLE_LOCAL PUNTO CLEAR
    '''
def p_funcion_size(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO SIZE PAREN_IZQ PAREN_DER
    '''
def p_funcion_add(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO ADD PAREN_IZQ tipodato PAREN_DER
    '''


def p_funcion_intersect(p):
    '''
    conjunto : conjunto PUNTO INTERSECT SIGNO_INTERROGACION  conjunto
    '''

#------------------------------ESTRUCTURA DE CONTROL------------------------------
#------estructura case (Jose Alcivar)------
def p_estructuracase(p):
    'estructuracase : CASE variable usocase'

def p_opcioncase(p):
    '''opcioncase : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    | rango'''

def p_rango(p):
    'rango : PAREN_IZQ ENTERO PUNTO PUNTO ENTERO PAREN_DER'


def p_usocase(p):
    '''usocase : WHEN opcioncase
    | WHEN opcioncase usocase
    '''

#------------------------------ESTRUCTURA DE DATOS------------------------------
#------estructura HASH (Jose Alcivar)------
def p_estructurahash(p):
    '''estructurahash : LLAVE_IZQ elementohash LLAVE_DER
    | LLAVE_IZQ LLAVE_DER'''

def p_elementohash(p):
    '''elementohash : parhash
    | parhash COMA elementohash'''

def p_parhash(p):
    'parhash : clavehash ASIGNACION_HASH valorhash'

def p_clavehash(p):
    '''clavehash : STRING
    | ENTERO'''

def p_valorhash(p):
    'valorhash : tipodato'

#------------------------------PEDIR DATOS TECLADO------------------------------
#------pedir datos por teclado (Jose Alcivar)------
def p_pedirporteclado(p):
    '''pedirporteclado : variable IGUAL GETS
    | variable IGUAL GETS PUNTO CHOMP'''


#________IMPRIMIR DATOS______(Allison Recalde)
def p_impresion(p):
    '''cuerpoF : PRINT tipodato
                  | PUTS tipodato
                  | PRINT PAREN_IZQ tipodato PAREN_DER
                  | PUTS PAREN_IZQ tipodato PAREN_DER
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