from FuncAcao import WebScrappingAcao
from FuncBDR import WebScrappingBDR
from FuncFII import WebScrappingFII
import pandas as pd
import numpy as np

AllStocks=[]
with open("CodAcoesYahoo.txt","r") as Data:
    Linhas = Data.read().split("\n")
    for n in Linhas:
        AllStocks.append(WebScrappingAcao(n))
    Data.close()

df = pd.DataFrame(AllStocks)
df.columns=["Cod Acao","Capitalizacao de Mercado(1 Dia)","Valor da Empresa",
"P/L Passado","P/L Estimado","Indice PEG (expectativa de 5 anos)",
"Preco/Vendas (ttm)","Preco/Livro (mrq)","Valor da Empresa/Receita",
"Valor da Empresa/EBITDA","Beta (mensalmente por 5 anos)",
"Variacao de 52 Semanas","Variacao de 52 Semanas de S&P 500","Alta de 52 Semanas",
"Baixa de 52 Semanas","Media Movel de 50 Dias","Media Movel de 200 Dias",
"Volume Medio (3 meses)","Volume Medio (10 dias)","Acoes Em Circulacao","Flutuacao",
"Porcentagem de Propriedade de insiders","Porcentagem de Propriedade de Instituicoes",
"Acoes a descoberto","Indice a descoberto","Porcentagem de baixa de flutuacao",
"Porcentagem de baixa de acoes em circulacao","Acoes a descoberto (mes anterior)",
"Taxa Anual de Dividendos Futuros","Rendimento Anual de Dividendos Futuros",
"Taxa Anual de Dividendos Passados","Rendimento Anual de Dividendos Passados",
"Rendimento do Dividendo Medio de 5 Anos","Indice de Payout","Data do Dividendo",
"Data do Ex-Dividendo","Fator do ultimo desdobramento","Ultima Data do Desdobramento",
"Fim do Ano Fiscal","Ultimo Trimestre (mrq)","Margem de Lucro","Margem Operacional (ttm)",
"Rentabilidade do Ativo (ttm)","Retorno Sobre o Patrimonio Liquido (ttm)","Receita (ttm)",
"Receita por Acao (ttm)","Aumento de Receita Trimestral (yoy)","Lucro Bruto (ttm)",
"Lajida","Lucro Liquido Med. a Comum (ttm)","Lucro pro Acao Diluido (ttm)",
"Aumento de Ganhos Trimestral (yoy)","Fluxo de Caixa Total (mrq)",
"Fluxo de Caixa Total por Acao (mrq)","Debito Total (mrq)",
"Debito Total/Patrimonio Liquido (mrq)","Indice de Liquidez (mrq)",
"Valor Contabil Por Acao (mrq)","Fluxo de Caixa Operacional (ttm)",
"Fluxo de Caixa Livre Alavancado (ttm)","Despesa Financeira","Nopat",
"Total de Ativos Circulantes","Total de Passivos Circulantes ",
"Bens do ativo imobilizado ultimo ano","Bens do ativo imobilizado penultimo ano",
"Depreciacao acumulada","Depreciação e amortizacao"]

df = df.drop(columns=["Data do Ex-Dividendo","Fator do ultimo desdobramento","Ultima Data do Desdobramento",
"Fim do Ano Fiscal","Ultimo Trimestre (mrq)"])

for col in df.columns[1:]:
    print(df[col])  
    df[col] = df[col].str.replace('.','',regex=True)
    df[col] = (df[col].str.replace(',','.').replace('N/A','0').replace(r'[kMBT%]+$', '', regex=True).astype(float) * df[col].str.extract(r'[\d\.]+([kMBT%]+)', expand=False).fillna(1).replace(['k','M','B','T',"%"], [10**3, 10**6, 10**9, 10**12,1]).astype(float))
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace('.',',',regex=True)

df.to_csv(r"C:\Users\gmone\Desktop\EstudoAcoes\BancodeDadosYahoo\BancoDadosAcoes.csv",index=False)