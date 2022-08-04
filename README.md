# GBI6_ExamenPython
Examen
JUAN CARLOS CARRERA BARONA 
Ambato- Ecuador
Tipo de sangre O+
CI: 1804391835
caracteristicas_key           Point_value
----------------------------  --------------------------------------------------------------------
Nombre del dispositivo        DESKTOP-P5CT13I
Procesador                    Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz   2.11 GHz
RAM instalada                 8,00 GB (7,83 GB usable)
Identificador de dispositivo  3D13C9C7-B526-4791-9A48-F063A1389C75
Id. del producto              00331-10000-00001-AA982
Tipo de sistema               Sistema operativo de 64 bits, procesador basado en x64
Lápiz y entrada táctil        La entrada táctil o manuscrita no está disponible para esta pantalla




















# Escriba aquí su código para el ejercicio 1
import Bio
from Bio.Seq import Seq
# cargar biopython o sus módulo, funciones
from Bio import Entrez
import re

def download_pubmed (keyword):
    """
    Funcion que pide como entrada la frase de busqueda en la base de datos del NCBI y como output crea un documento con  
    extension txt que contiene los datos de la busqueda
    """ 
    # Always tell NCBI who you are (edit the e-mail below!)
    Entrez.email = "juan.carrera@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term=keyword+"[Title]",
                        usehistory="y")
    record = Entrez.read(handle)

    #print (record)
    #generate a Python list with all Pubmed IDs of articles about Dengue Network
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text", 
                       retstart=0,
                       retmax=543, 
                       webenv=webenv,
                       query_key=query_key)

    out_handle = open(keyword+".txt", "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list 


import re 
import csv 
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from collections import Counter
def map_science(data):
    """
    Funcion que pide como entrada la data de busqueda anterior y como resultado muestra un grafico de dispersion de la 
    frecuencia en que se repetia la nacionalidad (x = longitud, y = latitud) de los articulos. 
    """ 
    with open(data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    unique_countries = list(set(countries_1))
    #return (unique_countries)
    #return (len(countries_1)) 
    conteo=Counter(countries_1)
    resultado={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    #return (resultado)
    geolocator = Nominatim(user_agent="my_user_agent")
    long = []
    lat = []
    count = []
    for i in resultado.keys():
        geolocator = Nominatim(user_agent="my_user_agent")
        loc = geolocator.geocode(i)
        long.append(loc.longitude)
        lat.append(loc.latitude)
    for i in resultado.values(): 
        count.append(i*100)
    #return (count)
    plt.scatter(long, lat, s = count, c=count)
    plt.colorbar()
    ## valores de referencia 
    ard = dict(arrowstyle="->")
    plt.annotate('Ecuador', xy = (-79.3666965, -1.3397668), 
               xytext = (-80.25, 20.05), arrowprops = ard)
    plt.annotate('Spain', xy = (-4.8379791, 39.3260685), 
               xytext = (-40, 37.4292), arrowprops= ard)
    plt.annotate('Canada', xy = (-107.991707, 61.0666922), 
               xytext = (-73.1106, 48.3736), arrowprops= ard)
    plt.annotate('Belgica', xy = ( 4.6667145, 50.6402809), 
               xytext = (-0.6847, 30.8369), arrowprops= ard)
    plt.annotate('Sweden', xy = (14.5208584, 59.6749712), 
               xytext = (-40.33, 47.61), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    return (plt.savefig(data +'.jpg', dpi=300, bbox_inches='tight'))
    plt.show()
