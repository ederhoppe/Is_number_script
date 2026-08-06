"""10. Escribe un programa que te permita ingresar una cadena de texto y 
 el programa indique si la cadena esta formada por caracteres numéricos"""

string = input('Ingresa una clave alfanumerica: ')
numero = False 

for caracter in string:
    if caracter.isdigit():
        numero = True
        break #si ya encontramos uno, no hay que seguir buscando 

if numero: 
    print(f'Tu clave {string} tiene numeros')

else:
    print(f'ERROR, la clave no contiene numeros')