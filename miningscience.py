import re
from Bio import Entrez
import pandas as pd 

def download_pubmed(keyword):
    """Descarga la data de PubMed utilizando el ENTREZ de Biopython
    la funcion devuelve el # de articulos y los IDs""" 
    Entrez.email= "juan.carrera@est.ikiam.edu.ec"
    consulta = Entrez.esearch(db="pubmed", term= keyword, usehistory= "y", retmax= 100000, retmode = "text")
    datosl= Entrez.read(consulta)
    numart= datosl ["Count"]
    PMIDs = datosl ["IdList"]
    return numart, PMIDs

    
def mining_pubs(PMIDs,tipo ): 
    """esta función debe utilizar el módulo re y utilizar el párametro tipo para realizar lo siguiente:
    Si el tipo es "DP" recupera el año de publicación del artículo. El retorno es un dataframe con el PMID y el DP_year.
    Si el tipo es "AU" recupera el número de autores por PMID. El retorno es un dataframe con el PMID y el num_auth.
    Si el tipo es "AD" recupera el conteo de autores por país. El retorno es un dataframe con el country y el num_auth."""
    years=[]
    numbauts=[]
    countys=[]
    for art in PMIDs:
        regart= Entrez.efetch(db= "pubmed", retmode = "text", id= art, rettype= "medline")
        article= regart.read()
        yearart= re.findall(r'DP\s{2}-\s(\w{4})', article)[0]
        countryart= re.findall(r'PL\s{2}-\s(.*)', article)[0]
        numbau=len(re.findall(r'AU\s{2}-\s', article))
        years.append( yearart)
        numbauts.append(numbau)
        countys.append(countryart)
    if tipo== "DP": 
        finaltb= pd.DataFrame({"PMID":PMIDs, "year": years})
    elif tipo== "AU": 
        finaltb= pd.DataFrame({"PMID":PMIDs, "Autores": numbauts})
    elif tipo== "AD": 
        finaltb= pd.DataFrame({"Pais":countys, "Autores": numbauts})
    return finaltb 