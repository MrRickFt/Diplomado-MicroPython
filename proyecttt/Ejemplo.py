'''Capturando un dato y comparando 
n = int(input("Enter a number: "))
print (n>=100)'''

###ejemplo de IF

'''
#lee dos numeros
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
#Elegir el numero mas grande
if numero1>numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2
print("el numero más grande es: ", nmasGrande) 
'''

###Funcion max
'''
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largestNumber = max(number1, number2, number3)
print ("The largest number is: ", largestNumber) '''

###Ejemplo de if con elif
'''
x = 1
y = 1.0
z = "1"

if x == y:
    print ("uno")
if y == int(z):
    print ("Dos")
elif x == y:
    print("tres")
else:
    print ("Cuatro") '''


'''
while True: 
    print ("estoy atrapado en un loop")'''
    
    ##Ejemplo While
'''largestNumber = -999999999
number = int(input("Introduzca un numero o escriba -1 para detener: "))
while number != -1:
    if number > largestNumber:
        largestNumber = number
    number=int(input("Introduzca un numero o escriba -1 para detener: "))
print ("El numero mas grande es: ", largestNumber)'''

##Ejemplo for
'''
for i in range (100):
    print ("El valor de i actualmente es: ", i)'''
    
#Ejemplo fijando rangos de operación
'''
for i in range (2, 8,):
    print ("El valor de i actualmente es: ", i) '''
    
#Ejemplo incremento empieza en dos, incrementa en 2 y va hasta 7 porque se detiene 1 antes del 8
'''for i in range (2, 8, 2):
    print ("El valor de i actualmente es: ", i)'''

#Ejemplo de four con potencias
'''
pow = 1
for exp in range (16):
    print ("2 a la potencia de ", exp, "es", pow)
    pow *= 2'''
  
##Ejemplo break  
'''for i in range (1, 6):
    if i ==3:
        break
    print ("Inside the loop.", i)
    
print("outside the loop")
'''
  ##Ejemplo continue  
'''
for i in range (1, 6):
    if i ==3:
        continue
    print ("Inside the loop.", i)
    
print("outside the loop") '''

###Corriendo bit a bit, agragando 0 a la derecha o 0 a la izquierda
'''var = 16
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)'''

##evaluando && bit a bit esos 2 numeros y arrojando resultado
'''
print (22&15)'''

'''
x = 4
y = 1
a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2

print (a, b, c, d, e, f)
'''

'''
for i in range (1, 6):
    if i == 5:
        print ("Listos o no, ahí voy")
    else:
        print("Missisipi ", i)'''
    
##While con condiciones y break    
'''texto = input("Ingrese una palabra por favor ")
while (texto!="Cisco"):
    
    if (texto == "Cisco") | (texto =="cisco"):
        print("Ha salido correctamente")
        break
        
    elif texto == "aguacate":
        print ("Bye Bye Nub")
        break
        
    else :
        texto = input("Ingrese una palabra por favor ")  '''
        

########################## CAPITULO DE LISTAS #####################
##Creando una lista, las posiciones arrancan desde 0
'''myList = [25, 18, 3, "Agua", 7.0, False, True]
print (myList[3])'''

##Cambiando un valor de un indice en la lista
'''myList [1] = "Change"
print (myList)
'''
#Cambiar de posición el valor
'''myList [0] =  myList [3]
print (myList [1] )'''

##Eliminando elementos de una lista
'''del myList [1]
print (myList)'''

##Imprimiendo la lista en negativo (-1 sería el ultimo valor de la lista)
'''print (myList[-1])
print (myList[-4])
print (myList[-2])'''

##Ejemplo de laboratorio
'''listExample = [1, 2, 3, 4, 5]
reempNumb = int(input("Por favor ingrese un numero para reemplazar: "))
listExample [3] = reempNumb
print (listExample)

del listExample [4]
print (listExample)'''

##Metodos para listas, meotodo append(), agrega a la lista un valor que querramos y lo agrega al final
'''myList = [25, 18, 3, "Agua", 7.0, False, True]
print(myList)
myList.append(8)
print(myList)
myList.append("Bocachico")
print(myList)'''

##Metodo Extend() colocar elementos dentro de un rango ejemplo los numeros 10, 11, 12
'''print(myList)
myList.extend(range(10, 13))
print(myList)'''

##Metodo count(), contar cuantas veces está un elemento
'''conteo = myList.count(3)
print(conteo)'''

#metodo Insert()
'''print(myList)
print("######################")
myList.insert(2, True)
print(myList)'''

#Metodo Remove() elimina el contenido del indice
'''print(myList)
print("######################")
myList.remove(0)
print(myList)
'''
##Agregar elementos a una lista elementos por medio del ciclo for
'''myList = [] #Creating a list
for i in range (6):
    myList.append(i+1)
print (myList)'''

##metodo reverse() para invertir el contenido numerico de la lista
'''myList.reverse()
print(myList)'''

##Metodo sort() ordena de mayor a menor en los numeros o letras alfabeticamente
'''''myList.sort()
print(myList)''
'''
##Buscar el indice de un objeto
'''ubicacion = myList.index(5)
print(ubicacion)'''

##Metodo pop() elimina cualquier indice
'''myList.pop()
print(myList)
myList.pop(0)
print(myList)'''

##Cambiando las posiciones de los indices sin perder la información
'''myList [0], myList[1] = myList[1], myList[0]
print(myList)'''

## Obteniendo el ID de memoria de cada lista
'''myList1 = [1,2,3,4]
myList2 = [1,2,3,4]
myList3 = myList1, [1,2,3,4]'''

'''print(myList1)
print(myList2)'''

'''print (id(myList1))
print (id(myList2))
print (id(myList3))'''

##slices  trae pedazos de alguna lista y los copia en otra
'''myList = [10, 8, 6, 4, 2]
newList = myList [:] 
print(id(newList))
print(id(myList))'''

##Otro metodo para clonar sería
'''myList = [10, 8, 6, 4, 2]
newList =list(myList)
print (newList)
print(id(newList))
print(id(myList))'''

##Cambio de indice en mis listas
'''myList = [10, 8, 6, 4, 2]
print (myList)
myList [0], myList[4] = myList [4], myList[0]
print (myList)'''

##Método short con letras
'''ist = ["D","F","A","Z"]
ist.sort()
print(ist)'''

################## FUNCTIONS ################
##¿como se crean las funciones? def + nombrefunción ():
'''def wasabi_motel():
    print("Enter a value: ")'''

##Otra función
'''def mensaje():
    print("Este es un mensaje inicial")

print ("Inicio")
mensaje()
mensaje = "Agua"

print (mensaje)'''

###Parametrización de funciones 
'''def saludo (nombre):
    print ("bienvenido al curso ", nombre)

saludo ("Andrés")'''

'''def saludo (cosa, otra):
    print("palabra: ", cosa,  "otra palabra: ", otra)

saludo("Celular", "Cargador")'''


##Argumentos ejercicios
'''def sum (a, b, c):
    print (a, "+", b, "+", c, "=", a+b+c)

sum (1,2,3)
sum (c = 1, a = 2, b = 3)
sum (3, c = 1, b = 2)
sum (c = 3, a = 1, b =2)
sum (4, 3, c =2)
sum (4, b = 3, c = 2)'''

#Python completando argumentos cuando no se escriben
'''def introduction (firstName, LastName="Smith"):
    print("Hello, my name is ", firstName, LastName)
introduction("John", "Doe")
introduction("John")'''


##Funciones con boleanos
'''def felizAñoNuevo (deseos = True):
    print ("Tres ...")
    print ("Dos ...")
    print ("Uno ...")
    if not deseos:
        return
    print ("¡Feliz Año Nuevo!")
    
felizAñoNuevo(True)'''

##Función con return expresión
'''def saludo():
    print ("Bienvenidos al curso")
    return 57+9, "Hola", 4.0, True
x = saludo() #se guarda en una variable para poder imp´rimir el retorno de la función

print ("El retorno de la función es: ", x)'''

##Aqui se pierde el retorno por no usar una variable que se guarde
'''def saludo():
    print ("Bienvenidos al curso")
    return 57+9, "Hola", 4.0, True
saludo() #se guarda en una variable para poder imp´rimir el retorno de la función

print ("El retorno de la función es: ")
'''
##"None" es una palabra reservada que nos permite decir que no hay nada, que no hay valores, puede estar en condicionales también
'''valor = None
if valor == None:
    print ("No hay nada")
print (valor)'''

#numeros pares
'''def fC(n):
    if(n%2==0):
        return "es par"
    
print(fC(7))'''

##Sumando una lista
'''def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum

print (sumOfList([5,4,3])) 
print (sumOfList([5]))'''

##Listas con funciones y for
'''def strangeListFunction (n):
    sTrangeList = []
    for i in range (0, n):
        sTrangeList.insert(0,i)
    return sTrangeList
print (strangeListFunction(8))'''

##La función reconoce variables que están por fuera de ella
'''def miFuncion():
    print ("¿Conozco a la variable? ", var)

var =1
miFuncion()
print(var)'''

##Una variable dentro de la función si tiene el mismo nombre  que una por fuera excluye la por fuera
'''def miFuncion():
    var = 2
    print ("¿Conozco a la variable? ", var)

var =1
miFuncion()
print(var)'''

#Global es una palabra reservada que extiende el alcance de las variables en lectura y modificación
'''def miFuncion():
    global  var ##Aquí se usa el global
    var = 2
    print ("¿Conozco a la variable? ", var)

var =1
miFuncion()
print(var)'''

##Ejemplo de respeto de variables en funciones
'''def mifuncion(n):
    print ("yo obtuve", n)
    n+= 1
    print ("Ahora yo tengo ", n)
    
var = 1
mifuncion(var)
print (var)'''

#Ejemplo de NONE
'''def hola():
    return
    print("Hola")
hola()'''

##Definiendo tipo de dato con funcion, if y elif, return
'''def isInt(data):
    if type(data)==int:
        return True
    elif type(data) == float:
        return False'''
    
##Funciones con dos o mas parametros
'''def indice (peso, altura):
    return peso/ altura ** 2
print (indice(52.5, 1.65))'''

##triangulo ejempo
'''def triangulo (a,b,c):
    if (a + b <= c) |(b + c <= a) | (c + a <= b):
        return False
    return True
print(triangulo(1,1,1))
print(triangulo(1,1,3))'''

##pendiente realizar XXXXXX
'''number = int(input("Ingrese el primer numero"))
number2 = int(input("Ingrese el segundo numero"))
number3 = int(input("Ingrese el tercer numero"))
number4 = int(input("Ingrese el cuarto numero"))
number5 = int(input("Ingrese el quinto numero"))

MyList = [number, number2, number3, number4, number5]
print (MyList)

def Mult():
    for i in range (MyList):
        m *=  MyList[:]
        print (m)
    return m

Mult()
'''

#################TUPLAS#################
##SECUENCIA: ALMACENA MÁS DE UN VALOR O NINGUNO SI ESTÁ VACÍO
##MUTABILIDAD: PROPIEDAD DE MUTABILIDAD DE DATOS 
##TUPAS: SON DATOS QUE BASICAMENTE SON INMUTABLES, SE COMPORTAN COMO LISTAS PERO NO PUEDEN SER MODIFICADOS UTLIZAN () EN VEZ DE []
##Len da la cantidad de elementos que están dentro de una lisa o de una tupla
'''myTupla = (1, 2, 3)
print (myTupla[:])
print (type(myTupla[0]))'''

##Uniendo tuplas, multiplicando tuplas
'''miTupla = (1, 10, 100)
t1 = miTupla + (1000, 10000)
t2 = miTupla * 3

print (len(t2))
print (t1)
print (t2)'''

#####DICCIONARIOS####
##Son mutables, un diccionario en python es como en la vida real
##Tiene una estructura de pares (las claves y los valores)
##Cada clave debe ser unica, la clave puede ser de cualquier tipo (int, float, boolean, string)
##No es una lista, almacenan pares de valores que identifican el valor al que se está recurriendo


###Creando un diccionario###
'''dict = {"Gixxer" : "Suzuki", 
        "Boxer" : "Auteco",
        "NKD": "Akt",
        "MotorG5" : 150}
print (len(dict))
print(type(dict))
print (dict)
print (dict["Gixxer"])
print (dict.keys())##Arroja la cantidad de claves que están en nuestro diccionario
print (sorted(dict.keys()))##Ordenar diccionario, ¡no soporta numeros enteros!
print (dict.items()) ## Trae los elementos a manera de tuplas
print (dict.values()) ## Valores que están en cada una de las llaves en el orden que se encuentren

### Asignando valores
dict [4] = {"Hero": "Honda"}
print(dict)

##Cambiando valores
dict ["MotorG5"] = "Duke"
print (dict)

#Eliminando valores de un diccionario
del dict ["MotorG5"]
print (dict)

print(dict.popitem()) #Eliminamos el ultimo elemento, no acepta argumentos
print (dict)'''

'''
dict = {}
salir = 0
precio = " "
x = ""'''


'''while (salir == 0):
   articulo = int(input(("Ingrese el precio del articulo")))
   precio = int(input(("Ingrese el precio del articulo")))
   dict [x] =  precio
   salir = input(print("Desea salir del listado? 1. SI   0. NO"))
   print (dict)'''
   
##Sumando    
'''var = 0
sumNumber = 0
while (var ==0):
    
    numberOne = int(input("Inserte un numero "))
    sumNumber = (numberOne + sumNumber)
    var = int(input("Desea continuar? 0. Si, 1. No "))
    print ("La Suma total es : ", sumNumber)'''


#############CHAPTER 5###########
####### MÓDULOS #######
##¿QUE ES UN MÓDULO?: es una pieza de software en piezas separadas pero cooperantes

'''import math
def sin(x):
    if 2 * x == pi:
        return 0.9999999
    else:
        return None
pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))'''

##Alias "as"
'''import math as m

print (m.sin(m.pi/2))'''

###Conociendo los elementos de un módulo
'''import math

for name in dir(math):
    print(name, end="\t")'''
    
'''from math import *
x =1.4
y=2.6
ad=90

print (pi)
print (sin(pi/2))
print (cos(ad))
print (tan(ad))
print (floor (x), floor (y))
print (ceil (x), ceil(y))
print (hypot(x,y))
print (sqrt(144))'''

'''## Función random numeros aleatorios diferentes siempre
from random import random
for i in range(5):
    print(random())'''

'''###Genera numeros aleatorios pero gracias a "seed" siempre serán los mismos numeros
from random import random, seed
seed (0)
for i in range (5):
    print (random())'''
    
'''from random import randint, random, randrange

for i in range (5):
    print (random())
    '''
'''from random import randrange, randint
print (randrange(4), end=' ')
print (randrange(0,10), end = ' ')
print (randrange(0,3,2), end=' ')
'''
##Funciones que nos ayudan a ver sistemas operativos caracteristicas
#función platform infomacion del SO 
#Processos devuelve una cadena con el nombre del procesador
#Función machine información general del sistema
'''from platform import platform
print ("Plataforma", platform())

from platform import system
print ("System", system())

from platform import machine
print ("machine", machine())

from platform import processor
print ("processor", processor())

from platform import version
print ("Version", version())'''

'''##función implementación de python, muestra 
from platform import python_implementation, python_version_tuple

print (python_implementation())
print(python_version_tuple())'''


'''##Traeer modulo de donde sera con sys y path
from sys import path

path.append('C:\\Andina\\proyecttt\\package')

import module
print (module.suma(2,7))
print (module.producto(4,7))
print (module)'''


######################################CADENAS##################################
##Ejemplo de cadenas
'''palabra = "por"
print (len(palabra))
'''

##Multilinea
##''multiLinea = '''Linea #1
##Linea #2'''
##print(len(multiLinea))''


####Concatenar cadenas o replicar
'''str1 = 'a'
str2 = 'b'

print (str1 + str2)
print (str2 + str1)
print (5 * 'a') ##Replicando
print ('b' * 4) ##Replicando'''

'''##Obtener el valor del codigo en utf8
ch1 = "@"
ch2 = '♣'
ch3 = '☺'

print (ord(ch1))
print (ord(ch2))
print (ord(ch3))

##Cadenas
print (chr(64))
print (chr(9827))
print (chr(9786))'''

'''##Obteniendo pedazos de cadenas
alpha = "abcdefghi"

print(alpha[1:3])
print(alpha[:3]) 
print(alpha[0:]) ##Obteniendo todo
print(alpha[::2]) #salto de 2
print(alpha[::3]) ##salto de 3
print(alpha[1::2]) ##salto de 2 en dos desde el primer caracter'''

'''##Buscando algo especidfico en cadenas, arroja true o false
alphabeto = "abcdefghijklmnñopqrstuvwxyz"
print("f" in alphabeto)
print("F" in alphabeto)
print("1" in alphabeto)
print("ghi" in alphabeto)
print("XTh" in alphabeto)'''



'''###Agregando o uniendo cadenas

alphabeto = "bcdefghijklmnñopqrstuvwxy"

alphabeto = "a" + alphabeto
alphabeto = alphabeto + "z"
print(alphabeto)'''

'''##Minimo elemento de la secuencia pasando como argumento
print (min("aAbByYzZ"))
t= [0, 12.1,12 ]
print (min(t))'''

##Elemento máximo de la cadena
'''print (max("aAbByYzZ"))
t= 'Los Caballeros Que Dicen "¡Ni!"'
print ('[' + max (t)+ ']')

t= [0,1,2]
print (max(t))
print(type(t))'''

'''###Metodo index busca desde el inicio hasta el fin para ubicar la posición del argumento
print ("aAbByYzZaA".index("b"))
print ("aAbByYzZaA".index("A"))
print ("aAbByYzZaA".index("Z"))

#Metodo list, toma los elementos de una cadena y lo pasa a lista
print (list("aAbByYzZaA"))

#Count cuenta las apariciones dentro de la secuencia
print ("aAbByYzZaA".count("b"))

#Capitalize toma la cadena evalua si no hay ningun caracter que tenga evaluado como 0, toma las letras restantes en una cadena donde todas serán minusculas menos la primera
print ("aAbByYzZaA".capitalize())'''

'''#Center
print('['+ 'Beta'.center(2) + ']')
print('['+ 'Beta'.center(20)+ ']')
print('['+ 'Beta'.center(7)+ ']')
print('['+ 'Beta'.center(2, '*') + ']')
'''
'''#Endswith, evalua si la cadena termina con el dato especificado. Arroja true o false
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))'''

'''#starswith comprueba si la cadena empieza con lo especificado
print ("omega".startswith("meg"))
print ("omega".startswith("om"))
'''
''''##Find busca un indice donde aparece numericamente
t = 'alfabeto'
print(t.find('eto'))
print(t.find('et'))
print(t.find('fa'))
print(t.find('e'))'''

'''#isalnum evalua si la cadena tiene numeros o letras 
print ('lambda30'.isalnum())
print ('lambda'.isalnum())
print ('30'.isalnum())
print ('@'.isalnum())'''

'''#Isalphaverifica si han ingresado solamente letras
print ("mooo".isalpha())
print ("Cr72021".isalpha())

#isdigit verifica si han ingresado solamente numeros
print ("Cr72021".isdigit())
print ("2021".isdigit())'''

'''#Islower evalua solamente letras minusculas
print ("Moooo".islower())
print ("moooo".islower())

#isespace evalua espacios en blanco solamente
print (" \n".isspace())
print (" ".isspace())
print ("Jorge A Ricardo".isspace())

#isuper evalua solamente si hay mayusculas
print ("Moooo".isupper())
print ("moooo".isupper())
print ("MOOOOO".isupper())'''

'''#Lower reemplaza las mayusculas por minusculas y las devuelve como una cadena
print ("SiGmA=60".lower())'''

'''#Replace, reemplaza todos los elementos de la cadena
print ("www.netacad.com".replace("netacad.com", "pythoninstitute.com"))
print ("This is it!".replace("is", "are")) ##reemplaza especifico
'''

'''#split divide la cadena y crea una lista con lo que contine la cadena
print ("jorge                      Andres  Ricardo".split())

#swapcase primera minuscula y el resto mayuscula
print("Yo soy el red".swapcase())

#title la primera en mayuscula tipo fara
print ("había un lago cerca al rio. Parte 8".title())

#Todo mayuscula
print ("Yo sé que nada sé. Parte 38".upper())'''


'''#sort () ordena la lista 
seconGreek = ['omega', 'alfa', 'pi', 'gama']
print (seconGreek)

seconGreek.sort()
print (seconGreek)'''

