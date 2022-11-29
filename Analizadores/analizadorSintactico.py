from RecursosPly import yacc
from analizadorLexico import tokens
from datetime import datetime
# Crear las siguientes reglas

resultado = ""
arreglo = []
def p_bloque(p):
    '''bloque : cuerpo SALTO_DE_LINEA cuerpo
                 | cuerpo SALTO_DE_LINEA bloque
                 '''

# 6. Cuerpo
def p_cuerpo(p):
    '''cuerpo : cuerpoF
    | tiposfuncion
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
    '''

def p_tiposfuncion(p):
    '''tiposfuncion : funcionparametro
    | funcionsinparametro
    | funcionreturn
    '''


def p_estructuradatos(p):
    '''estructuradatos : array
    | conjunto
    | estructurahash
     '''
    #

def p_estructuracontrol(p):
    '''estructuracontrol : ifelse
       | sentencias_while
       | estructuracase
        '''



def p_tipodato(p):
    '''tipodato : ENTERO
    | STRING
    | FLOAT
    | BOOLEAN
    '''

# ___________________________Asignación de variables- (Alcivar) _______________________

def p_asignacion(p):
    '''asignacion : variable IGUAL tipodato
    | variable IGUAL estructuradatos
    | variable IGUAL operacionesmate'''
    global resultado
    resultado += f'\n Se ha hecho una asignacion, con variable igual a {p[1].value} y valor {p[3].value}'

def p_variable(p):
    '''variable : TOKEN_VARIABLE_GLOBAL
    | TOKEN_VARIABLE_INSTANCIA
    | TOKEN_VARIABLE_LOCAL
    | TOKEN_CONSTANTE
    | TOKEN_VARIABLE_DE_CLASE'''


#___________________________ Operaciones matemáticas (Dennisse Aguirre)_______________________________
def p_valormate(p):
    '''valormate : tipodato
    | variable
    '''
def p_valornum(p):
    '''valornum : ENTERO
    | FLOAT
    '''
    #p[0] = p[1] = p[3]


def p_signosmate(p):
    '''signosmate : MAS
    | MENOS
    | MULTIPLICACION
    | DIVISION
    | MODULO
    | POTENCIA
    '''

def p_expresionesmate(p):
    '''expresionesmate : valornum MAS valornum
    | valornum MENOS valornum
    | valornum MULTIPLICACION valornum
    | valornum DIVISION valornum
    | valornum MODULO valornum
    | valornum POTENCIA valornum
    '''
    # Regla semantica con operaciones aritmeticas - (Dennisse Aguirre)
    #if p[2] == '+':
    # p[0] = p[1] + p[3]
    #elif p[2] == '-':
    #  p[0] = p[1] - p[3]
    #elif p[2] == '*':
    # p[0] = p[1] * p[3]
    #elif p[2] == '/':
    #  p[0] = p[1] / p[3]
    #elif p[2] == '%':
    #  p[0] = p[1] % p[3]
    #elif p[2] == '**':
    #  p[0] = p[1] + p[2] + p[3]

def p_operacionesmate(p):
    '''operacionesmate : expresionesmate
                       | expresionesmate signosmate operacionesmate
    '''
    print("operaciones matematicas")

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
def p_tiporeturn(p):
    '''tiporeturn : RETURN TOKEN_VARIABLE_LOCAL
        | RETURN tipodato
        '''

def p_funcionreturn(p):
    '''funcionreturn : DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER cuerpoF tiporeturn END
            | DEF TOKEN_NOMBRE_FUNCION cuerpoF tiporeturn END
            | DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA tiporeturn SALTO_DE_LINEA END
            | DEF TOKEN_NOMBRE_FUNCION SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA  tiporeturn SALTO_DE_LINEA END
            '''
    print("funcion con retorno")

def p_funcionparametro(p):
    '''funcionparametro : DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER cuerpoF END
     | DEF TOKEN_NOMBRE_FUNCION PAREN_IZQ parametro PAREN_DER SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA END
    '''
    print("funcion con parametro")

def p_funcionsinparametro(p):
    '''funcionsinparametro : DEF TOKEN_NOMBRE_FUNCION cuerpoF END
    | DEF TOKEN_NOMBRE_FUNCION SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA END
    '''
    print("funcion sin parametro ")

def p_parametro(p):
    '''parametro : tipopar
    | tipopar COMA parametro
    '''

def p_tipopar(p):
    '''tipopar : tipodato
    | variable
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
            | IF cond SALTO_DE_LINEA ELSE SALTO_DE_LINEA END
            | IF multicond SALTO_DE_LINEA ELSE SALTO_DE_LINEA END
            | IF multicond SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA ELSE SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA END
            | IF cond SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA ELSE SALTO_DE_LINEA cuerpoF SALTO_DE_LINEA END
             '''
    print("if else")

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
    #print("arreglo")
    #p[0] = arreglo

def p_elemento(p):
    '''elemento : tipodato
        | tipodato COMA elemento
    '''
    #p[0] = p[1]

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
   array :  TOKEN_VARIABLE_LOCAL CORCHETE_IZQ ENTERO CORCHETE_DER
    '''
    # Regla semantica para obtener elemento de un array - (Dennisse Aguirre)
    #arreglo[p[2]]
    #p[0] = p[1]
    print("obtener elemento")

 #array : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ ENTERO CORCHETE_DER
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
    print("estructuracase")

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
    global resultado
    resultado += "Se ha definido un HASH\n"

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


#------funciones HASH (Jose Alcivar)------

def p_retornarvalorhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ clavehash CORCHETE_DER'
    print("retornar valor de clave")

def p_agregarclavehash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL CORCHETE_IZQ clavehash CORCHETE_DER IGUAL valorhash'
    print("agregar clave valor al hash")

def p_borrarclavehash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO DELETE PAREN_IZQ clavehash PAREN_DER'
    print("borrar clave del hash")

def p_clavesdelhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO KEYS'
    print("extraer claves del hash")

def p_valoresdelhash(p):
    'estructurahash : TOKEN_VARIABLE_LOCAL PUNTO VALUES'
    print("extraer valores del hash")

#------------------------------PEDIR DATOS TECLADO------------------------------
#------pedir datos por teclado (Jose Alcivar)------
def p_pedirporteclado(p):
    '''pedirporteclado : variable IGUAL GETS
    | variable IGUAL GETS PUNTO CHOMP'''
    print("pedir por teclado")


#________IMPRIMIR DATOS______(Allison Recalde)
def p_impresion(p):
    '''impresion : PRINT tipodato
                  | PUTS tipodato
                  | PRINT PAREN_IZQ tipodato PAREN_DER
                  | PUTS PAREN_IZQ tipodato PAREN_DER
    '''
    print("impresion")

def p_error(p):
    global resultado
    if p:
        resultado += f'Error de sintaxis, tipo {str(p.type)} con valor: {str(p.value)}\n'
    else:
        resultado += 'Fin de lectura!\n'

# Build the parser
parser = yacc.yacc()

'''def validaRegla(s):
    result = parser.parse(s)
    print(result)'''


'''ruta = "../ArchivosPrueba/"
archivos = ["Aguirreprueba.txt", "Recaldeprueba.txt", "AlcivarPrueba.txt"]

a = ruta + archivos[0] ##reemplazar el indice del archivo
file = open(a)
archivo = file.readlines()
file.close()

archivolog=open(ruta + "log.txt","a")
fechahora=str(datetime.now())
archivolog.write("\n"+fechahora+" "+ a)
archivolog.close()'''


#archivos = ["Aguirreprueba.txt", "Recaldeprueba.txt", "AlcivarPrueba.txt", "hola.txt"]
#file = open(a)
#archivo = file.readlines()
#file.close()
#for linea in archivo:
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
def obtenerSintactico(info):
    global resultado
    resultado += ""
    lineas = info.split("\n")

    for line in lineas:
        while True:
            try:
                s = line
                print(s)
                print("uno")
            except EOFError:
                break
            if not s: continue
            result = parser.parse(s)
            print(result)
            print("dos")
            break
    print(len(resultado))
    print(str(resultado))
    print("tres")
    return resultado
