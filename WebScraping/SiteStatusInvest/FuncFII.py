import requests
from bs4 import BeautifulSoup

def WebScrappingFII(Codigo):
    
    URL = "https://statusinvest.com.br/fundos-imobiliarios/"+ Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    Valores = Soup.find_all("strong", {"class": "value"})
    Indicadores=[]
    Indicadores.append(Codigo)
    count=0
    for Valor in Valores:
        Indicadores.append(Valor.text)
        count+=1
        if count==16:
            break
        
    return Indicadores
#Estrutura da lista Indicadores
#Codigo da Ação 0
#Cotação Atual 1
#MIN 52 Semanas 2
#MAX 52 Semanas 3
#Dividend Yield Ultimos 12 Meses (D.Y) 4
#Valorização Ultimos 12 Meses 5
#Valor Patrimonial por Cota (VPC) 6
#Preço/Valor Patrimonial (P/VP) 7
#Valor em Caixa 8
#DY CAGR 9
#Valor CAGR 10
#Numero de Cotistas 11
#Rendimento Mensal Médio 24 meses 12
#Taxas Adminstração 13
#Liquidez Média Diária 14
#Participação no IFIX 15
#Ultimo Rendimento 16
