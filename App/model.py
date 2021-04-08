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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
                'categoriasid': None,
                'categorias': None
               }

    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideosid)

    catalog['categoriasid'] = mp.newMap(10000,
                                   maptype = 'CHAINING',
                                   loadfactor = 4.0,
                                   comparefunction = compareMapVideocatid)

    catalog['categorias'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    v = newVid(video['title'], video['channel_title'], video['trending_date'],video['publish_time'],video['views'],video['likes'],video['dislikes'],video['category_id'],video['country'],video['tags'])
    lt.addLast(catalog['videos'], v)
    mp.put(catalog['categoriasid'],v['category_id'], v)

def addCategorias(catalog, categoria):
    c = newCat(categoria['name'], categoria['id'])
    lt.addLast(catalog['categorias'], c)
   
# Funciones para creacion de datos

def newVid(title, channel_title,trending_date,publish_time,views,likes,dislikes,category_id,country,tags):
    vid={'title':'','channel_title':'','trending_date':'','publish_time':'','views':'','likes':'','dislikes':'','category_id':'','country':'','tags':''}
    vid['title']=title
    vid['channel_title']=channel_title
    vid['trending_date']=trending_date
    vid['publish_time']=publish_time
    vid['views']=views
    vid['likes']=likes
    vid['dislikes']=dislikes
    vid['category_id']=category_id
    vid['country']=country
    vid['tags']=tags
    return vid

def newCat(name, id):


    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat


# Funciones utilizadas para comparar elementos dentro de una lista

def videosSize(catalog):

    return lt.size(catalog['videos'])

def categoSize(catalog):

    return lt.size(catalog['categorias'])

def compareVideosid(ca1, ca2):
    """
    Compara dos ids de dos libros
    """
    if (ca1 == ca2):
        return 0
    elif ca1 > ca2:
        return 1
    else:
        return -1

def compareMapVideocatid(id, entry):
    
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def cmpVideosByViews(video1, video2): 

    return (float(video1['views']) > float(video2['views']))

def cmpVideosBytiempo(video1, video2):
   return (float(video1['dias']) > float(video2['dias']))

def cmpVideosByLikes(video1, video2):
   return (float(video1['likes']) > float(video2['likes']))

# Funciones de ordenamiento

def requerimiento1(catalog, size, tipodeorden, categ, pais, tipo): 
    nueva= lt.newList(tipo)
    for i in range(0, lt.size(catalog['videos'])):
        ele=lt.getElement(catalog['videos'],i)
        if ele['category_id'] == categ and ele['country'] == pais:
            lt.addLast(nueva,ele)
    sublista = nueva.copy() 
    start_time = time.process_time() 
    if(tipodeorden=="shell"):
        sorted_list = sa.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="insertion"):
        sorted_list = si.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="selection"):
        sorted_list = ss.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="quick"):
        sorted_list = sq.sort(sublista, cmpVideosByViews)
    elif (tipodeorden=="merge"):
        sorted_list = sm.sort(sublista, cmpVideosByViews)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return elapsed_time_mseg, sorted_list

def requerimiento2(catalog,pais,tipodeorden,tipo):
    nueva= lt.newList(tipo)
    listaesta={}
    for i in range(0, lt.size(catalog['videos'])):
        ele=lt.getElement(catalog['videos'],i)
        if ele['country'] == pais and not(ele['title'] in listaesta.keys()):
            listaesta[ele['title']]=1
            ele['dias'] = 1 
            lt.addLast(nueva,ele)
        elif ele['country'] == pais and (  ele['title'] in listaesta.keys()):
            listaesta[ele['title']]=listaesta[ele['title']]+1
            ele['dias'] = listaesta[ele['title']]
            lt.addLast(nueva,ele)
    sublista = nueva.copy() 
    start_time = time.process_time()
    if(tipodeorden=="shell"):
        sorted_list = sa.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="insertion"):
        sorted_list = si.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="selection"):
        sorted_list = ss.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="quick"):
        sorted_list = sq.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="merge"):
        sorted_list = sm.sort(sublista, cmpVideosBytiempo)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return sorted_list 

def requerimiento3(catalog,categor,tipodeorden,tipo):
    nueva= lt.newList(tipo)
    listae={}
    for i in range(0, lt.size(catalog['videos'])):
        ele=lt.getElement(catalog['videos'],i)
        if ele['category_id'] == categor and not(ele['title'] in listae.keys()):
            listae[ele['title']]=1
            ele['dias'] = 1 
            lt.addLast(nueva,ele)
        elif ele['category_id'] == categor and (  ele['title'] in listae.keys()):
            listae[ele['title']]=listae[ele['title']]+1
            ele['dias'] = listae[ele['title']]
            lt.addLast(nueva,ele)
    sublista = nueva.copy() 
    start_time = time.process_time()
    if(tipodeorden=="shell"):
        sorted_list = sa.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="insertion"):
        sorted_list = si.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="selection"):
        sorted_list = ss.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="quick"):
        sorted_list = sq.sort(sublista, cmpVideosBytiempo)
    elif (tipodeorden=="merge"):
        sorted_list = sm.sort(sublista, cmpVideosBytiempo)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 
    return sorted_list

def requerimiento4(catalog, size, tipodeorden, tagg, tipo): 
    nueva = lt.newList(tipo)
    final = lt.newList(tipo)
    listaee=[]
    for i in range(0, lt.size(catalog['videos'])):
        ele=lt.getElement(catalog['videos'],i)
        
        if tagg in ele['tags'] :
            lt.addLast(nueva,ele)
    sublista = nueva.copy() 
    start_time = time.process_time() 
    if(tipodeorden=="shell"):
        sorted_list = sa.sort(sublista, cmpVideosByLikes)
    elif (tipodeorden=="insertion"):
        sorted_list = si.sort(sublista, cmpVideosByLikes)
    elif (tipodeorden=="selection"):
        sorted_list = ss.sort(sublista, cmpVideosByLikes)
    elif (tipodeorden=="quick"):
        sorted_list = sq.sort(sublista, cmpVideosByLikes)
    elif (tipodeorden=="merge"):
        sorted_list = sm.sort(sublista, cmpVideosByLikes)
    stop_time = time.process_time() 
    elapsed_time_mseg = (stop_time - start_time)*1000 

    for i in range(0, lt.size(sorted_list)):
        ete=lt.getElement(sorted_list,i)
        if not(ete['title'] in listaee) :
            listaee.append(ete['title'])
            lt.addLast(final,ete)

    return elapsed_time_mseg, final