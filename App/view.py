"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Requerimiento 1 : Consultar cuales son los n videos con mas views de determinado pais y categoria")
    print("4- Requerimiento 2 : Consultar video que mas dias ha sio trending para determinado pais")
    print("5- Requerimiento 3 : Consultar video que mas dias ha sio trending para determinada categoria")
    print("6- Requerimiento 4 : Consultar cuales son los n videos con mas likes en un pais con tag especifico")
    print("0- Salir")

catalog = None

def initCatalog(tipo):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printvieostop(vide):

    size = lt.size(vide)
    if size:
        for videoo in lt.iterator(vide):
            print('Fecha de popularidad: '+videoo['trending_date'] +' Titulo: ' + videoo['title'] + ' Nombre del canal: '+videoo['channel_title']+' Fecha de publicacion: '+videoo['publish_time']+' Views: '+videoo['views']+' Likes: '+videoo['likes']+' Dislikes: '+videoo['dislikes']) 
        print("\n")
    else:
        print('No se encontraron Videos.\n')

def printResults4(ord_vid, sample): 
    size = lt.size(ord_vid) 
    if size >= float(sample): 
        print("Los  ", sample, " videos con mas likes son:") 
        i=2 
        while i <= float(sample)+1: 
            videoo = lt.getElement(ord_vid,i) 
            print('Fecha de popularidad: '+videoo['trending_date'] +' Titulo: ' + videoo['title'] + ' Nombre del canal: '+videoo['channel_title']+' Fecha de publicacion: '+videoo['publish_time']+' Views: '+videoo['views']+' Likes: '+videoo['likes']+' Dislikes: '+videoo['dislikes']+  ' Tags: '+videoo['tags'] +"\n") 
            i+=1



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        answer = controller.loadData(catalog)
        print('Videos cargados: ' + str(controller.videosSize(catalog)))
        print('Categorias cargados: ' + str(controller.categoSize(catalog)))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
        
        

    elif int(inputs[0]) == 3:
        categg = input("Indique la categoria: ")
        categ = controller.buscarcateporname(categg, catalog)
        pais = input("Indique el pais: ")
        siz = input("Indique tamaño de la muestra: ")
        result = controller.requerimiento1(catalog, int(siz), categ, pais)
        print("Los  ", siz, " videos con mas likes son:")
        printvieostop(result)

    elif int(inputs[0]) == 4:
        
        pais = input("Indique el pais: ")
        repuesta = controller.requerimiento2(catalog, pais)
        if lt.size(repuesta)<=0:
            print("No hay sufiecientes videos que cumplan las condiciones ")
        else:
            primero=lt.firstElement(repuesta)
            print(" El video con mas dias en tendencia de " + str(pais) +" es: ")
            print( " Titulo: "+ str(primero['title']))
            print( " Nombre del canal: "+ str(primero['channel_title']))
            print( " Pais: "+ str(primero['country']))
            print( " Dias: "+ str(primero['dias']))

    elif int(inputs[0]) == 5:

        category_name= input("Indique nombre de categoria: ")
        categor = controller.buscarcateporname(category_name, catalog)
        repuesta = controller.requerimiento3(catalog, categor)
        if lt.size(repuesta)<=0:
            print("No hay sufiecientes videos que cumplan las condiciones ")
        else:
            primero=lt.firstElement(repuesta)
            print(" El video con mas dias en tendencia de " + str(category_name) +" es: ")
            print( " Titulo: "+ str(primero['title']))
            print( " Nombre del canal: "+ str(primero['channel_title']))
            print( " Categoria: "+ str(primero['category_id']))
            print( " Dias: "+ str(primero['dias']))

    elif int(inputs[0]) == 6 :
        pais = input("Indique el pais: ")
        tagg = input("Indique el tag: ")
        size = input("Indique tamaño de la muestra: ")
        result = controller.requerimiento4(catalog, int(size), tagg, pais)
        print("Los  ", size, " videos con mas likes son:")
        printvieostop(result)
    else: 
        sys.exit(0)
sys.exit(0)
sys.exit(0)
