import requests
from bs4 import BeautifulSoup

def WebScrappingBDR(Codigo):
    
    URL = "https://statusinvest.com.br/bdrs/"+ Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    Valores = Soup.find_all("strong", {"class": "value"})
    Indicadores=[]
    Indicadores.append(Codigo)
    count=0
    for Valor in Valores:
        Indicadores.append(Valor.text)
        count+=1
        if count==8:
            break
    return Indicadores
    
#Estrutura da lista Indicadores
#Codigo da Ação 0
#Cotação Atual 1
#MIN 52 Semanas 2
#MAX 52 Semanas 3
#Dividend Yield Ultimos 12 Meses (D.Y) 4
#Valorização Ultimos 12 Meses 5
#Liquidez Média Diária 6
#Paridade inicial 7
#Numero de Açoes 8
#--------------Aluguel de BDR--------------
#Tomador (Média) 9
#Doador (Média) 10
#Numero de Acoes 11
#Volume 12
#--------------Proventos--------------
#Ano Passado 13
#Ano Atual 14
#Comparação 15
#Provisionado 16
#Comparação + Provisionado 17
#Instituição Depositária 18
#Pais de Origem 19
#Mercado de Origem 20
#Codigo Original 21
#Setor de atuação 22