'''
Created on 29 nov. 2018

@author: aochi
'''
from _ast import If

def busquedaSecuencial(unaLista, datoBuscar):
    pos=0
    encontrado=False
    
    while pos < len(unaLista) and not encontrado:
        if unaLista[pos] == datoBuscar:
            encontrado=True
        else:
            pos=pos+1
    
    return encontrado

vector = list(range(0,100))
print(vector)
listaPrueba = [1,2,32,8,17,19,42,13,0]
print(busquedaSecuencial(listaPrueba, 3))
print(busquedaSecuencial(listaPrueba, 13))