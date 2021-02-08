from FuncAcao import WebScrappingAcao
from FuncBDR import WebScrappingBDR
from FuncFII import WebScrappingFII
import pandas as pd
import numpy as np

AllStocks=[]
with open("CodAcoes.txt","r") as Data:
    Linhas = Data.read().split("\n")
    for n in Linhas:
        AllStocks.append(WebScrappingAcao(n))
    Data.close()

df = pd.DataFrame(AllStocks)
df.columns=["Cod Acao","Cotacao Atual","MIN 52 Semanas",
"MAX 52 Semanas","DY 12 Meses","Valorizacao 12 Meses",
"Tipo","Tag Along","Liquidez Media Diaria",
"Participacao no IBOV","Mercado de Opcoes","D.Y","P/L","PEG RATIO","P/VP","EV/EBITDA",
"EV/EBIT","P/EBITDA","P/EBIT","VPA","P/ATIVO","LPA","P/SR",
"P/CAP.GIRO","P/ATIVO CIRC LIQ","DIV LIQUIDA/PL","DIV LIQUIDA/EBITDA",
"DIV LIQUIDA/EBIT","PL/ATIVOS","PASSIVO/ATIVOS","LQ CORRENTE",
"Margem Bruta","Margem EBTIDA","Margem EBIT","Margem Liquida",
"ROE","ROA","ROIC","GIRO ATIVOS","CAGR RECEITAS 5 ANOS","CAGR LUCROS 5 ANOS",
"Tomador (Media)","Doador (Media)","Numero de Acoes","Volume",
"Proventos Ano Passado","Proventos Ano Atual","Proventos Comparacao",
"Proventos Provisionado","Proventos Comparacao+Provisionado",
"Patrimonio Liquido","Ativos","Ativos Ciculante","Divida Bruta",
"Disponibilidade","Divida Liquida","Valor de Mercado","Valor de Firma","Numero Total de Papeis"]

df = df.drop(columns=["Mercado de Opcoes","Tomador (Media)","Doador (Media)","Numero de Acoes","Volume",
"Proventos Ano Passado","Proventos Ano Atual","Proventos Comparacao",
"Proventos Provisionado","Proventos Comparacao+Provisionado"])
df.to_csv(r"C:\Users\gmone\Desktop\EstudoAcoes\BancodeDados\BancoDadosAcoes.csv",index=False)

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
