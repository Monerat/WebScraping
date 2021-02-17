from FuncAcao import WebScrappingAcao
from FuncAcao2 import WebScrappingAcao2
from FuncBDR import WebScrappingBDR
from FuncFII import WebScrappingFII
from FormulasValuation import GrahamRev
import pandas as pd
import numpy as np

AllStocks=[]
with open("CodAcoes.txt","r") as Data:
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
df['Valuation Graham'] = df['Valuation Graham'].astype(str).str.replace('.',',')
print(df)
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
