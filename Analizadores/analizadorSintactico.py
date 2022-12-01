from RecursosPly import yacc
from analizadorLexico import tokens
from datetime import datetime

# Crear las siguientes reglas

resultado = ""

# ----------------Para el semantico del Hash (Jose Alcivar)---------------------
esHash = False
variableActualHash = ""
clavesActualesHash = []
valoresActualesHash = []
clavesHash = {}
valoresHash = {}

# 6. Cuerpo
def p_cuerpo(p):
    '''cuerpo : cuerpoF
    | definicionfunciones
    | llamada_funciones
    | estructuradatos
    | pedirporteclado
    | estructuracontrol
    | usocase
    '''


def p_cuerpoF(p):
    '''cuerpoF : asignacion
    | operacionesmate
    | comparaciones
    | impresion
    | estructuracontrol
    | pedirporteclado
    '''


def p_estructuradatos(p):
    '''estructuradatos : array
    | conjunto
    | estructurahash
     '''
    p[0] = p[1]


def p_estructuracontrol(p):
    '''estructuracontrol :  sentencias_while
       | ifelse
       | estructuracase
        '''


def p_tipodato(p):
    '''tipodato : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    '''
    p[0] = p[1]


# ___________________________Asignación de variables- (Alcivar) _______________________

def p_asignacion(p):
    '''asignacion : variable IGUAL tipodato
    | variable IGUAL estructuradatos
    | variable IGUAL operacionesmate'''
    hayHash(p[1])
    global resultado
    resultado += f'Se ha hecho una asignacion\n'


#def p_variable(p):
#    '''variable : TOKEN_VARIABLE_GLOBAL
#    | TOKEN_VARIABLE_INSTANCIA
#    | TOKEN_VARIABLE_LOCAL
#    | TOKEN_CONSTANTE
#    | TOKEN_VARIABLE_DE_CLASE'''
#    p[0] = p[1]

def p_variable(p):
    'variable : TOKEN_VARIABLE_LOCAL'
    p[0] = p[1]


# ___________________________ Operaciones matemáticas (Dennisse Aguirre)_______________________________

def p_valormate(p):
    '''valormate : tipodato
    | variable
    '''

def p_valornum(p):
    '''valornum : ENTERO
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


#  regla semántica para operaciones matemáticas que solo deben ser números - Dennisse
def p_operacionesmate(p):
    '''operacionesmate : valornum  signosmate valornum
                       | valornum  signosmate operacionesmate
    '''
    global resultado
    resultado += f'Se ha hecho una operación matemática \n'


# __________________________ Comparaciones (Allison Recalde)_______
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



# _________________________ Estructura de control______________
# BUCLE WHILE____ (Allison Recalde)
def p_condicion(p):
    '''
    condicion : BOOLEAN
                 | comparaciones
    '''


def p_mas_cuerpoF(p):
    '''
        mas_cuerpoF : cuerpoF
                     | cuerpoF mas_cuerpoF
    '''


def p_sentencias_while(p):
    '''
    sentencias_while : WHILE condicion DO mas_cuerpoF END
               | WHILE condicion mas_cuerpoF END
               | WHILE PAREN_IZQ condicion PAREN_DER DO mas_cuerpoF END
               | WHILE PAREN_IZQ condicion PAREN_DER mas_cuerpoF END
    '''
    global resultado
    resultado += "Estructura while\n"




# IF ELSE ____ _____(Dennisse Aguirre)_________________________________________

def p_ifelse(p):
    '''
            ifelse :  IF multicond mas_cuerpoF ELSE mas_cuerpoF END
             | IF cond mas_cuerpoF ELSE mas_cuerpoF END
            | IF PAREN_IZQ cond PAREN_DER mas_cuerpoF ELSE mas_cuerpoF END
            | IF PAREN_IZQ multicond PAREN_DER mas_cuerpoF ELSE mas_cuerpoF END
             '''
    global resultado
    resultado += f"Estructura if-else\n"



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

# Definicion de funciones (Dennisse Aguirre)-----------------------------

def p_tiporeturn(p):
    '''tiporeturn : RETURN TOKEN_VARIABLE_LOCAL
        | RETURN tipodato
        '''

def p_definicionfunciones(p):
    '''definicionfunciones : DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER mas_cuerpoF tiporeturn END
            | DEF TOKEN_NOMBRE_FUNCION mas_cuerpoF tiporeturn END
            | DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER mas_cuerpoF END
             | DEF TOKEN_NOMBRE_FUNCION mas_cuerpoF END
            '''
    global resultado
    resultado += f'Se ha hecho una función \n'


def p_parametro(p):
    '''parametro : tipopar
    | tipopar COMA parametro
    '''

def p_tipopar(p):
    '''tipopar : tipodato
    | variable
    '''
#_____________Llamada a funciones con n argumentos (Allison Recalde)______
def p_llamada_funciones(p):
    '''llamada_funciones : TOKEN_VARIABLE_LOCAL PAREN_IZQ parametro PAREN_DER
        | TOKEN_VARIABLE_LOCAL PAREN_IZQ  PAREN_DER
    '''
    global resultado
    resultado += f'Llamada a funciones \n'


#__________________________ Estructura de datos  ______________________________________________
#Array____________ (Dennisse Aguirre)__________________________________


def p_array(p):
    "array : CORCHETE_IZQ elemento CORCHETE_DER"
    global resultado
    resultado += f"Se ha definido un ARRAY\n"

def p_elemento(p):
    '''elemento : tipodato
        | tipodato COMA elemento
    '''
    # p[0] = p[1]


def p_funcion_length(p):
    '''
    array : TOKEN_VARIABLE_LOCAL PUNTO LENGTH
    '''
    global resultado
    resultado += f"Uso de length para array\n"

def p_funcion_push(p):
    '''
   array : TOKEN_VARIABLE_LOCAL PUNTO PUSH PAREN_IZQ ENTERO PAREN_DER
    '''
    global resultado
    resultado += f"Uso de push para array\n"

# regla semántica acerca del indice  que debe ser entero - Dennisse
def p_obtener_elemento(p):
    '''
   array : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ ENTERO CORCHETE_DER
    '''
    global resultado
    resultado += f"obtener elemento de un array\n"


# array : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ ENTERO CORCHETE_DER
def p_funcion_first(p):
    '''
    array : TOKEN_VARIABLE_LOCAL PUNTO FIRST PAREN_IZQ PAREN_DER
    '''
    global resultado
    resultado += f"Uso de first para array\n"


# Set ______________(Allison Recalde)_____________________________________________
def p_conjunto(p):
    'conjunto : SET CORCHETE_IZQ elemento CORCHETE_DER'
    global resultado
    resultado += f"Estructura de datos: Conjunto\n"

# Metodos de la estructura SET (Allison Recalde)
def p_funcion_clear(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO CLEAR PAREN_IZQ PAREN_DER
    | TOKEN_VARIABLE_LOCAL PUNTO CLEAR
    '''
    global resultado
    resultado += f"Función clear para Conjunto\n"


def p_funcion_size(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO SIZE PAREN_IZQ PAREN_DER
    '''
    global resultado
    resultado += f"Función size para Conjunto\n"


def p_funcion_add(p):
    '''
    conjunto : TOKEN_VARIABLE_LOCAL PUNTO ADD PAREN_IZQ tipodato PAREN_DER
    '''
    global resultado
    resultado += f"Función add para Conjunto\n"

def p_funcion_intersect(p):
    '''
    conjunto : conjunto PUNTO INTERSECT SIGNO_INTERROGACION  conjunto
    '''


# ------------------------------ESTRUCTURA DE CONTROL------------------------------
# ------estructura case (Jose Alcivar)------
def p_estructuracase(p):
    'estructuracase : CASE variable usocase END'
    global resultado
    resultado += f'Se ha creado una estructura case\n'


def p_opcioncase(p):
    '''opcioncase : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    | rango'''


def p_rango(p):
    'rango : PAREN_IZQ ENTERO PUNTO PUNTO ENTERO PAREN_DER'


def p_usocase(p):
    '''usocase : WHEN opcioncase cuerpoF
    | WHEN opcioncase cuerpoF usocase
    '''


# ------------------------------ESTRUCTURA DE DATOS------------------------------
# ------estructura HASH (Jose Alcivar)------
def p_estructurahash(p):
    '''estructurahash : LLAVE_IZQ elementohash LLAVE_DER
    | LLAVE_IZQ LLAVE_DER'''
    global esHash
    esHash = True
    global resultado
    resultado += "Se ha definido un HASH\n"


def p_elementohash(p):
    '''elementohash : parhash
    | parhash COMA elementohash'''


def p_parhash(p):
    'parhash : clavehash ASIGNACION_HASH valorhash'
    agregarClaveHash(p[1])
    agregarValorHash(p[3])


def p_clavehash(p):
    '''clavehash : STRING
    | ENTERO'''
    p[0] = p[1]


def p_valorhash(p):
    'valorhash : tipodato'
    p[0] = p[1]


# ------funciones HASH (Jose Alcivar)------

'''def p_retornarvalorhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ clavehash CORCHETE_DER'
    print("retornar valor de clave")'''

def p_agregarclavehash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ clavehash CORCHETE_DER IGUAL valorhash'
    print("agregar clave valor al hash")


def p_borrarclavehash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO DELETE PAREN_IZQ clavehash PAREN_DER'
    print("borrar clave del hash")


# ------------------------------PEDIR DATOS TECLADO------------------------------
# ------pedir datos por teclado (Jose Alcivar)------
def p_pedirporteclado(p):
    '''pedirporteclado : variable IGUAL GETS
    | variable IGUAL GETS PUNTO CHOMP'''
    global resultado
    resultado += f"pedir por teclado\n"


# ________IMPRIMIR DATOS______(Allison Recalde)
def p_impresion(p):
    '''impresion : PRINT tipodato
                  | PUTS tipodato
                  | PRINT PAREN_IZQ tipodato PAREN_DER
                  | PUTS PAREN_IZQ tipodato PAREN_DER
    '''
    global resultado
    resultado += "Se ha realizado una impresion\n"


# Build the parser



# -------------------------------Reglas sematicas (Jose Alcivar)-------------------------------
# -----reconocer la creacion de un arreglo
def hayHash(dato):
    global esHash
    if (esHash == True):
        global variableActualHash
        global clavesHash
        global valoresHash
        global valoresActualesHash
        global clavesActualesHash
        variableActualHash = dato
        clavesHash[variableActualHash] = clavesActualesHash
        valoresHash[variableActualHash] = valoresActualesHash
        valoresActualesHash = []
        clavesActualesHash = []
        variableActualHash = ""
        esHash = False


def limpiarControlHash():
    global esHash
    global variableActualHash
    global clavesHash
    global valoresHash
    global valoresActualesHash
    global clavesActualesHash

    valoresActualesHash = []
    clavesActualesHash = []
    variableActualHash = ""
    clavesHash = {}
    valoresHash = {}
    esHash = False


# controlar las claves de los hash
def agregarClaveHash(clave):
    global clavesActualesHash
    clavesActualesHash.append(clave)


# controlar los valores de los hash
def agregarValorHash(valor):
    global valoresActualesHash
    valoresActualesHash.append(valor)


# -----obtener las claves de un hash (regla semantica)-----
def p_retornarclavesdelhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO KEYS'
    probar = p[1]
    cadena = ""
    global resultado

    if ( probar in clavesHash ):
        resultado += f'funcion keys\n'
        arreglo = clavesHash[probar]
        for clave in arreglo:
            cadena += str(clave) + " "
    else:
        cadena = ("Error semantico, la variable " + p[1] + " no existe o no es un diccionario\n")

    resultado += f"{cadena}\n"

# -----obtener los valores de un hash (regla semantica)-----
def p_retornarvaloresdelhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO VALUES'
    var = p[1]
    concatenar = ""
    global resultado
    if ( var in valoresHash ):
        concatenar += f'funcion values\n'
        array = valoresHash[var]
        for valor in array:
            concatenar += str(valor) + " "
    else:
        concatenar = ("Error semantico, la variable " + p[1] + " no existe o no es un diccionario\n")
    resultado += f"{concatenar}\n"

# -------------------------------Fin Reglas sematicas (Jose Alcivar)-------------------------------

def p_error(p):
    global resultado
    if p:
        resultado += f'Error de sintaxis, tipo {str(p.type)} con valor: {str(p.value)}\n'
    else:
        resultado += 'Fin de lectura!\n'

parser = yacc.yacc()

'''def validaRegla(s):
    result = parser.parse(s)
    print(result)'''

# ruta = "../ArchivosPrueba/"
# archivos = ["Aguirreprueba.txt", "Recaldeprueba.txt", "AlcivarPrueba.txt"]

# a = ruta + archivos[0] ##reemplazar el indice del archivo
'''file = open(a)
archivo = file.readlines()
file.close()'''

# archivolog=open(ruta + "log.txt", "a")
# fechahora=str(datetime.now())
# archivolog.write("\n"+fechahora+" "+ "GUI.py")
# archivolog.close()


# archivos = ["Aguirreprueba.txt", "Recaldeprueba.txt", "AlcivarPrueba.txt", "hola.txt"]
# file = open(a)
# archivo = file.readlines()
# file.close()
# for linea in archivo:
#  validaRegla(linea)


'''while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    validaRegla(s)'''


def Limpiar():
    global resultado
    resultado = ""
    limpiarControlHash()


def obtenerSintactico(info):
    ruta = "../ArchivosPrueba/"
    archivolog = open(ruta + "log.txt", "a")
    fechahora = str(datetime.now())
    archivolog.write("\n" + fechahora + " " + "GUI.py")
    archivolog.close()
    Limpiar()
    global resultado
    resultado += ""
    lineas = info.split("\n")
    for line in lineas:
        while True:
            try:
                s = line
            except EOFError:
                break
            if not s: continue
            result = parser.parse(s)
            break
    return resultado
