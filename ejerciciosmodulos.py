#################  Modulo1
#Problema1
""" print("Hola\n¿Cual es tu nombre?")
nombre=input()
print(f"Hola,{nombre}") """
#Problema2 "SUBSTITUCION
abecedario="abcdefghijklmnñopqrstuvwxyz"
abecedario1="YTNSHKVEFXRBAUQZCLWDMIPGJO"
abecedario2="VCHPRZGJNTLSKFBDQWAXEUYMOI"
mensajecifrado=str()
print("Ingrese un mensaje a cifrar")
mensaje=input()
print("Hay dos tipo de cifrado ¿Cual desea usar?\n1\n2")
cifrado=int(input())
if cifrado==1:
    cifrado=abecedario1
else:
    cifrado=abecedario2
for i in mensaje:
    busqueda=abecedario.find(i.lower())
    if busqueda!=-1: #excluso a los q no son letras
        busqueda2=abecedario.find(i)
        if busqueda2!=-1:   #diferencio mayusculas y minusculas
            mensajecifrado=mensajecifrado+cifrado[busqueda2].lower()
        else:
            mensajecifrado=mensajecifrado+cifrado[abecedario.find(i.upper())]
    else:
        mensajecifrado=mensajecifrado+i
print(mensajecifrado)
#ProblemaDiversos
#  1
print("Ingrese la cantidad de ahorros a analizar")
ahorros=int(input())
analisis_anual1=ahorros*1.04
analisis_anual2=analisis_anual1*1.04
analisis_anual3=analisis_anual2*1.04
print(f'Ahorros en el año 1 a una tasa de 4%:{analisis_anual1}')
print(f'Ahorros en el año 2 a una tasa de 4%:{analisis_anual2}')
print(f'Ahorros en el año 3 a una tasa de 4%:{analisis_anual3}')
# 2
import math

print("Ingrese los 3 coeficientes de la ecuacion de segundo grado:")
a=int(input())
b=int(input())
c=int(input())
discriminante=b*b-4*a*c
if discriminante<0:
    print("La ecuacion no tiene solucion en los numeros reales")
elif discriminante>0:
    solucion1=(-b+math.sqrt(discriminante))/(2*a)
    solucion2=(-b-math.sqrt(discriminante))/(2*a)
    print(f'La Solucion 1 es : {solucion1} La Solucion 2 es : {solucion2}')
else:
    solucion=-b/(2*a)
    print(f'La unica solucion es {solucion}')
#Modulo2
#Problema1
altura=int()
valor=False
while valor==False:
    print("Ingrese un numero entre el 1 y el 8 para crear la piramide")
    altura=int(input())
    valor=(bool(altura<9)*bool(altura>=1))
    if valor==True:
        for i in range(altura):
            print(f'{" "*(altura-i)}{"#"*(i+1)}')
#Probelma2
texto_cifrado=str()
abecedario="abcdefghijklmnñopqrstuvwxyz"
print("Ingrese su mensaje a cifrar")
mensaje=input()
print("Ingrese la clave para el cifrado")
try:
    k=int(input())
    for i in mensaje:

        if i in abecedario:
            p=abecedario.index(i)
            c=(p+k)%27   #use 27 en vez de 26 porque mi abecedario contiene la ñ
            texto_cifrado=texto_cifrado+abecedario[c]
        elif i.lower() in abecedario:
            p=abecedario.index(i.lower())
            c=(p+k)%26 
            texto_cifrado=texto_cifrado+abecedario[c].upper()
        else:
            texto_cifrado=texto_cifrado+i
    print("Su texto sin formato es:",mensaje)
    print("Su texto cifrado es:",texto_cifrado)
except ValueError :
    print("ErrorDatux2021:La clave de cifrado solo puede ser un valor entero positivo")
#Problemas diversos1
""" Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas.
Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos. """
lista_alumnos=[]
print("Ingrese la cantidad de alumnos: ")
n_alumnos=int(input())
for i in range(n_alumnos):
    nota1=-1
    nota2=-1
    nota3=-1
    print(f'Ingrese el nombre del alumno {i+1}')
    nombre=input()
    print(f'Ingrese las tres notas (entre 0 y 10) del alumno {i+1}:')
    while nota1>10 or nota1<0:
        print("Ingrese nota 1")
        nota1=int(input())
    while nota2>10 or nota2<0:
        print("Ingrese nota 2")
        nota2=int(input())
    while nota3>10 or nota3<0:
        print("Ingrese nota 3")
        nota3=int(input())
    alumno=[nombre,nota1,nota2,nota3]
    lista_alumnos.append(alumno)
print('La lista de los alumnos es:')
print(lista_alumnos)
""" Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuántos desaprobaron,
 teniendo en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno. """
aprobados=0
desaprobados=0
for i in range(len(lista_alumnos)):
    promedio=(lista_alumnos[i][1]+lista_alumnos[i][2]+lista_alumnos[i][3])/3
    (lista_alumnos[i]).append(promedio)
    if promedio>=4:
        aprobados+=1
    else:
        desaprobados+=1
print(f'Cantidad de aprobados : {aprobados}')
print(f'Cantidad de desaprobados : {desaprobados}')
""" Informar el promedio de nota del curso total. """
for i in range(n_alumnos):
    print(f'El promedio del alumno {lista_alumnos[i][0]} es {lista_alumnos[i][4]}')
""" Realizar una función que indique quién tuvo el promedio más alto y quién tuvo la nota promedio más baja. """
def primer_ultimo_lugar(a):
    promedios=[]
    for i in range(len(a)):
        promedios.append(a[i][4])
    maximo_valor=max(promedios)
    minimo_valor=min(promedios)
    primer_lugar=promedios.index(maximo_valor)
    ultimo_lugar=promedios.index(minimo_valor)
    print(f'El el promedio mas alto es de :{a[primer_lugar][0]}')
    print(f'El el promedio mas bajo es de :{a[ultimo_lugar][0]}')
primer_ultimo_lugar(lista_alumnos)
def buscar(nombre,a):
    nombres=[]
    busqueda=[]
    for i in range(len(a)):
        nombres.append(a[i][0])
    for i in range(len(a)):
        encontrar=nombres[i].find(nombre)
        if encontrar!=-1:
            busqueda.append(a[i])
    print(f'Resultados de la busqueda:{busqueda}')
print("Ingrese los nombre completo o parcial para buscar:")
nombre_busqueda=input()
buscar(nombre_busqueda,lista_alumnos)
""" Modulo3:Ejercicio1 Credit """
print("Ingrese un numero de tarjeda de credito")
tarjeta_credito=int(input())
analisis=str(tarjeta_credito)[::-1]
sumapor2=int()
suma=int()
analisis[::]
for i in analisis[1::2]:
    n=int(i)
    if (n*2)>=10:
        sumapor2+=int(str((n*2))[0])+int(str((n*2))[1])
    else:
        sumapor2+=n*2
for i in analisis[0::2]:
    suma+=int(i)
total=suma+sumapor2
if len(str(tarjeta_credito))==15:
    if str(tarjeta_credito)[0:2]=='34' or str(tarjeta_credito)[0:2]=='37':
        print("AMEX")
elif len(str(tarjeta_credito))==16 and str(tarjeta_credito)[0:2] in ['51','52','53','54','55']:
       print("MasterCard")
elif len(str(tarjeta_credito))==16 or len(str(tarjeta_credito))==13 and int(str(tarjeta_credito)[0])==4:
        print("VISA")
if int(str(total)[-1])==0:
    print("La tarjeta es legitima")
else:
    print("INVALID")

