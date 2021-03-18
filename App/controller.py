"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos
def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipo)
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategorias(catalog)
    

def loadVideos(catalog):
    """
    Carga los videos del archivo.  
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategorias(catalog):
    """
    Carga todos las categorias del archivo.
    """
    catefile = cf.data_dir + 'category-id.csv'
    catfil = open(catefile)
    csvin = csv.reader(catfil, delimiter='\t')
    data = [row for row in csvin]
    header = data.pop(0)
    for row in data:
        rowdict = dict(zip(header, row))
        model.addCategorias(catalog, rowdict)

# Funciones de consulta sobre el catálogo

def requerimiento1(catalog, size, tipodeorden, categ, pais, tipo ):

    return model.requerimiento1(catalog,size,tipodeorden, categ, pais, tipo)
    
def requerimiento2(catalog,pais,tipodeorden,tipo):

    return model.requerimiento2(catalog, pais, tipodeorden,tipo)

def requerimiento3(catalog,categor,tipodeorden,tipo):

    return model.requerimiento3(catalog,categor,tipodeorden,tipo)


def requerimiento4(catalog, size, tipodeorden, tagg, tipo ):

    return model.requerimiento4(catalog,size,tipodeorden, tagg, tipo)
