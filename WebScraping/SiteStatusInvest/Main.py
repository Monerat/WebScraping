from FuncAcao2 import WebScrappingAcao2
from FuncAcao2 import dfAcoes
from FuncBDR import WebScrappingBDR
from FuncFII import WebScrappingFII
import pandas as pd
import numpy as np



with open("CodAcoesGeral.txt","r") as Data:
    Linhas = Data.read().split("\n")
    for n in Linhas:
        df = dfAcoes(n)
        df.to_csv(r"C:\Users\gmone\Desktop\EstudoAcoes\BancodeDados\BancoDadosAcoes"+n+r".csv",index=False)
    Data.close()

AllBDRs=[]
with open("CodBDRs.txt","r") as Data:
    Linhas = Data.read().split("\n")
    for n in Linhas:
        AllBDRs.append(WebScrappingBDR(n))
    Data.close()

df = pd.DataFrame(AllBDRs)
df.columns=["Cod Acao","Cotacao Atual","MIN 52 Semanas","MAX 52 Semanas",
"Dividend Yield Ultimos 12 Meses","Valorizacao Ultimos 12 Meses",
"Liquidez Media Diaria","Paridade inicial","Numero de Acoes"]

df.to_csv(r"C:\Users\gmone\Desktop\EstudoAcoes\BancodeDados\BancoDadosBDRs.csv",index=False)

AllFIIs=[]
with open("CodFIIs.txt","r") as Data:
    Linhas = Data.read().split("\n")
    for n in Linhas:
        AllFIIs.append(WebScrappingFII(n))
    Data.close()

df = pd.DataFrame(AllFIIs)
df.columns=["Cod Acao","Cotacao Atual","MIN 52 Semanas","MAX 52 Semanas",
"Dividend Yield Ultimos 12 Meses","Valorizacao Ultimos 12 Meses",
"Valor Patrimonial por Cota","Preco/Valor Patrimonial","Valor em Caixa",
"DY CAGR","Valor CAGR","Numero de Cotistas","Rendimento Mensal Medio 24 meses",
"Taxas Adminstração","Liquidez Media Diaria","Participacao no IFIX","Ultimo Rendimento"]

df.to_csv(r"C:\Users\gmone\Desktop\EstudoAcoes\BancodeDados\BancoDadosFIIs.csv",index=False)
