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

def printResults1(ord_vid, sample): 
    size = lt.size(ord_vid) 
    if size >= float(sample): 
        print("Los  ", sample, " videos con mas views son:") 
        i=1 
        while i <= float(sample): 
            videoo = lt.getElement(ord_vid,i) 
            print('Fecha de popularidad: '+videoo['trending_date'] +' Titulo: ' + videoo['title'] + ' Nombre del canal: '+videoo['channel_title']+' Fecha de publicacion: '+videoo['publish_time']+' Views: '+videoo['views']+' Likes: '+videoo['likes']+' Dislikes: '+videoo['dislikes']+"\n") 
            i+=1

def printResults4(ord_vid, sample): 
    size = lt.size(ord_vid) 
    if size >= float(sample): 
        print("Los  ", sample, " videos con mas likes son:") 
        i=2 
        while i <= float(sample)+1: 
            videoo = lt.getElement(ord_vid,i) 
            print('Fecha de popularidad: '+videoo['trending_date'] +' Titulo: ' + videoo['title'] + ' Nombre del canal: '+videoo['channel_title']+' Fecha de publicacion: '+videoo['publish_time']+' Views: '+videoo['views']+' Likes: '+videoo['likes']+' Dislikes: '+videoo['dislikes']+  ' Tags: '+videoo['tags'] +"\n") 
            i+=1

def buscarcateporname(categg):
    for i in range(0,lt.size(catalog['categorias'])):
            cate = lt.getElement(catalog['categorias'], i)
            if categg in str(cate['name']):
                return cate['id']
    return "ERROR"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        # TODO: modificaciones para observar el tiempo y memoria
        print("Cargando información de los archivos ....")
        answer = controller.loadData(cont)
        print('Videos cargados: ' + str(controller.videosSize(cont)))
        print('Categorias cargados: ' + str(controller.categoSize(cont)))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 3:
        categg = input("Indique la categoria: ")
        categ = buscarcateporname(categg)
        pais = input("Indique el pais: ")
        size = input("Indique tamaño de la muestra: ")
        tipodeorden = input("Indique el tipo de ordenamiento que quiere aplicar: ( selection, insertion, shell, quick o merge ) \n")
        result = controller.requerimiento1(catalog, int(size), tipodeorden, categ, pais, tipo)
        if lt.size(result[1])<=0:
            print("No hay sufiecientes videos que cumplan las condiciones ")
        else:
            printResults1(result[1], size)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))

    elif int(inputs[0]) == 4:
        
        pais = input("Indique el pais: ")
        tipodeorden = input("Indique el tipo de ordenamiento que quiere aplicar: ( selection, insertion, shell, quick o merge ) \n")
        repuesta = controller.requerimiento2(catalog,pais,tipodeorden,tipo)
        if lt.size(repuesta)<=0:
            print("No hay sufiecientes videos que cumplan las condiciones ")
        else:
            primero=lt.firstElement(repuesta)
            print(" El video con mas dias en tendencia de " + str(pais) +" es: ")
            print( " Titulo: "+ str(primero['title']))
            print( " Nombre del canal: "+ str(primero['channel_title']))
            print( " Pais: "+ str(primero['country']))
            print( " Dias: "+ str(primero['dias']))

    elif int(inputs[0]) == 5 :

        category_name= input("indique nombre de categoria: ")
        categor = buscarcateporname(category_name)
        tipodeorden = input("Indique el tipo de ordenamiento que quiere aplicar: ( selection, insertion, shell, quick o merge ) \n")
        repuesta = controller.requerimiento3(catalog,categor,tipodeorden,tipo)
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
        tagg = input("Indique el tag: ")
        size = input("Indique tamaño de la muestra: ")
        tipodeorden = input("Indique el tipo de ordenamiento que quiere aplicar: ( selection, insertion, shell, quick o merge ) \n")
        result = controller.requerimiento4(catalog, int(size), tipodeorden, tagg, tipo)
        if lt.size(result[1])<=0:
            print("No hay sufiecientes videos que cumplan las condiciones ")
        else:
            printResults4(result[1], size)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
    else: 
        sys.exit(0)
sys.exit(0)
sys.exit(0)
