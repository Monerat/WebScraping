import requests
from bs4 import BeautifulSoup
from FormulasValuation import GrahamRev
import re
import pandas as pd
import numpy as np

def farejadorStrong(Soup,Codigo):
    if(Soup.find(string=Codigo).find_next("strong").contents[0] == None):
        return "Valor not found"
    else:
        return Soup.find(string=Codigo).find_next("strong").contents[0]

def WebScrappingAcao2(Codigo):
    
    URL = "https://statusinvest.com.br/acoes/"+ Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    Indicadores=[]
    Indicadores.append(Codigo)
    with open("AtributoStrong.txt","r",encoding='utf8') as Data:
        Linhas = Data.read().split("\n")
        for n in Linhas:
            Indicadores.append(farejadorStrong(Soup,n))
        Data.close()

    return Indicadores

def dfAcoes(Nometxt):
    AllStocks=[]
    with open(Nometxt,"r") as Data:
        Linhas = Data.read().split("\n")
        for n in Linhas:
            AllStocks.append(WebScrappingAcao2(n))
        Data.close()

    df = pd.DataFrame(AllStocks)
    df.columns=["Cod Acao","Valor atual","D.Y","P/L","PEG Ratio","P/VP","EV/EBITDA","EV/EBIT","P/EBITDA",
    "P/EBIT","VPA","P/Ativo","LPA","P/SR","P/Cap. Giro","P/Ativo Circ. Liq.","Dív. líquida/PL",
    "Dív. líquida/EBITDA","Dív. líquida/EBIT","PL/Ativos","Passivo/Ativos","Liq. corrente","M. Bruta",
    "M. EBITDA","M. EBITDA","M. Líquida","ROE","ROA","ROIC","Giro ativos","CAGR Receitas 5 anos",
    "CAGR Lucros 5 anos","Patrimônio líquido","Ativos","Ativo circulante","Dívida bruta","Disponibilidade",
    "Dívida líquida","Valor de mercado","Valor de firma","Nº total de papeis"]

    valuation=[]
    Selic = 2

    for linha in range(0, len(df.index), 4):
        
        valuation.append(GrahamRev(df.iloc[linha,12],df.iloc[linha,31],Selic))
        valuation.append(GrahamRev(df.iloc[linha+1,12],df.iloc[linha+1,31],Selic))
        valuation.append(GrahamRev(df.iloc[linha+2,12],df.iloc[linha+2,31],Selic))
        valuation.append(GrahamRev(df.iloc[linha+3,12],df.iloc[linha+3,31],Selic))

    df['Valuation Graham'] = valuation
    df['Valuation Graham'] = df['Valuation Graham'].astype(str).str.replace('.',',',regex=True)
    
    return df


'''
acao =[]
acao.append(WebScrappingAcao2("ITSA4"))
acao.append(WebScrappingAcao2("WEGE3"))
acao.append(WebScrappingAcao2("EGIE3"))
acao.append(WebScrappingAcao2("ENBR3"))

df = pd.DataFrame(acao)
df.columns=["Cod Acao","Valor atual","D.Y","P/L","PEG Ratio","P/VP","EV/EBITDA","EV/EBIT","P/EBITDA",
"P/EBIT","VPA","P/Ativo","LPA","P/SR","P/Cap. Giro","P/Ativo Circ. Liq.","Dív. líquida/PL",
"Dív. líquida/EBITDA","Dív. líquida/EBIT","PL/Ativos","Passivo/Ativos","Liq. corrente","M. Bruta",
"M. EBITDA","M. EBITDA","M. Líquida","ROE","ROA","ROIC","Giro ativos","CAGR Receitas 5 anos",
"CAGR Lucros 5 anos","Patrimônio líquido","Ativos","Ativo circulante","Dívida bruta","Disponibilidade",
"Dívida líquida","Valor de mercado","Valor de firma","Nº total de papeis"]

'''

'''
Valor atual
D.Y
P/L
PEG Ratio
P/VP
EV/EBITDA
EV/EBIT
P/EBITDA
P/EBIT
VPA
P/Ativo
LPA
P/SR
P/Cap. Giro
P/Ativo Circ. Liq.
Dív. líquida/PL
Dív. líquida/EBITDA
Dív. líquida/EBIT
PL/Ativos
Passivo/Ativos
Liq. corrente
M. Bruta
M. EBITDA
M. EBITDA
M. Líquida
ROE
ROA
ROIC
Giro ativos
CAGR Receitas 5 anos
CAGR Lucros 5 anos
Patrimônio líquido
Ativos
Ativo circulante
Dívida bruta
Disponibilidade
Dívida líquida
Valor de mercado
Valor de firma
Nº total de papeis
'''