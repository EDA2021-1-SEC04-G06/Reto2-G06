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
               'cate': None,
               'pais': None
               }

    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideosid)

    catalog['categoriasid'] = mp.newMap(200,
                                   maptype = 'CHAINING',
                                   loadfactor = 4.0,
                                   comparefunction = compareMapVideocatid)
    
    catalog['pais'] = mp.newMap(200,
                                   maptype = 'CHAINING',
                                   loadfactor = 4.0,
                                   comparefunction = comparepais)

    catalog['cate'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    v = newVid(video['title'], video['channel_title'], video['trending_date'],video['publish_time'],video['views'],video['likes'],video['dislikes'],video['category_id'],video['country'],video['tags'])
    lt.addLast(catalog['videos'], v)
    addVideoCate(catalog, v)
    addpaais(catalog, v)


def addpaais(catalog, v):

    paises = catalog['pais']

    paiss = v['country'].strip()
    existp = mp.contains(paises, paiss)
    if existp:
        entry = mp.get(paises, paiss)
        pa = me.getValue(entry)
    else:
        entry = {'country': "", 'videos': None}
        entry['country'] = str(paiss)
        entry['videos'] = lt.newList('ARRAY_LIST')
        pa = entry
        mp.put(paises, paiss, pa)
    lt.addLast(pa['videos'], v)

def addVideoCate(catalog, v):

    cates = catalog['categoriasid']

    cateid = v['category_id']
    existid = mp.contains(cates, cateid)
    if existid:
        entry = mp.get(cates, cateid)
        cat = me.getValue(entry)
    else:
        entry = {'category_id': "", 'videos': None}
        entry['category_id'] = str(cateid)
        entry['videos'] = lt.newList('ARRAY_LIST')
        cat = entry
        mp.put(cates, cateid, cat)
    lt.addLast(cat['videos'], v)


def addCategorias(catalog, categoria):
    c = newCat(categoria['name'], categoria['id'])
    lt.addLast(catalog['cate'], c)
    
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

    return lt.size(catalog['cate'])

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

def comparepais(id, entry):
    
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1

def cmpVideosByViews(video1, video2): 

    return (float(video1['views']) > float(video2['views']))

def cmpVideosBytiempo(video1, video2):
   return (float(video1['dias']) > float(video2['dias']))

def cmpVideosByLikes(video1, video2):
   return (float(video1['likes']) > float(video2['likes']))

def buscarcateporname(categg, catalog):
    for i in range(0, lt.size(catalog['cate'])):
            cate = lt.getElement(catalog['cate'], i)
            if categg in str(cate['name']):
                return cate['id']
    return "ERROR"

# Funciones de ordenamiento

def requerimiento1(catalog, siz, categ, pais): 
    final = None
    nueva = lt.newList("ARRAY_LIST")
    porcate = mp.get(catalog['categoriasid'], str(categ))
    if porcate:
        catevideos = me.getValue(porcate)['videos']
       
        for v in lt.iterator(catevideos):
            if v['country'] == pais:
                lt.addLast(nueva, v)
    
        sublista = nueva.copy()
        sorted_list = sa.sort(sublista, cmpVideosByViews)
        final = lt.subList(sorted_list, 1, siz)
    return final


def requerimiento2(catalog,pais):
    final = None
    nueva = lt.newList("ARRAY_LIST")
    listaesta = {}
    paisess = mp.get(catalog['pais'], pais.strip())
    if paisess:
        pavideos = me.getValue(paisess)['videos']
        for v in lt.iterator(pavideos):
            if not(v['title'] in listaesta.keys()):
                listaesta[v['title']] = 1
                v['dias'] = 1
                lt.addLast(nueva, v)
            elif (v['title'] in listaesta.keys()):
                listaesta[v['title']] = listaesta[v['title']]+1
                v['dias'] = listaesta[v['title']]
                lt.addLast(nueva, v)
        sublista = nueva.copy()
        sorted_list = sa.sort(sublista, cmpVideosBytiempo)
        final = lt.subList(sorted_list, 1, 1)
    return final

def requerimiento3(catalog, categor):
    final = None
    nueva = lt.newList("ARRAY_LIST")
    listaesta = {}
    cates = mp.get(catalog['categoriasid'], categor)
    if cates:
        cavideos = me.getValue(cates)['videos']
        for v in lt.iterator(cavideos):
            if not(v['title'] in listaesta.keys()):
                listaesta[v['title']] = 1
                v['dias'] = 1
                lt.addLast(nueva, v)
            elif (v['title'] in listaesta.keys()):
                listaesta[v['title']] = listaesta[v['title']]+1
                v['dias'] = listaesta[v['title']]
                lt.addLast(nueva, v)
        sublista = nueva.copy()
        sorted_list = sa.sort(sublista, cmpVideosBytiempo)
        final = lt.subList(sorted_list, 1, 1)
    return final

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