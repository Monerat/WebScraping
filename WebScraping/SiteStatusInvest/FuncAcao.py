import requests
from bs4 import BeautifulSoup

def WebScrappingAcao(Codigo):
    
    URL = "https://statusinvest.com.br/acoes/"+ Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    Valores = Soup.find_all("strong", {"class": "value"})
    Indicadores=[]
    Indicadores.append(Codigo)
    count=0
    for Valor in Valores:
        Indicadores.append(Valor.text)
        count+=1
        if count==58:
            break
    return Indicadores

#Estrutura da lista Indicadores
#Codigo da Ação 0
#Cotação Atual 1
#MIN 52 Semanas 2
#MAX 52 Semanas 3
#Dividend Yield Ultimos 12 Meses (D.Y) 4
#Valorização Ultimos 12 Meses 5
#Tipo 6
#Tag Along 7
#Liquidez Média Diária 8
#Participação no IBOV 9
#Mercado de Opcoes 10
#--------------Indicadores de Valuation--------------
#Dividend Yield (D.Y) 11
#Preço/Lucro (P/L) 12
#PEG RATIO 
#Preço/Valor Patrimonial (P/VP) 14
#Enterprise Value/Earnings Before Interest, Taxes, Depreciation and Amortization (EV/EBITDA) 13
#Enterprise Value/Earnings Before Interest and Taxes (EV/EBIT) 15
#Preço/Earnings Before Interest, Taxes, Depreciation and Amortization (P/EBITDA) 16
#Preço/Earnings Before Interest and Taxes (P/EBIT) 17
#Valor Patrimonial por Ação (VPA) 18
#Preço da Ação/Total de Ativos (P/ATIVO) 19
#Lucro por Ação (LPA) 20
#Preço Atual/Receita Líquida por Ação (P/SR) 21
#Preço Atual/(Ativo Circulante - Passivo Circulante) (P/CAP.GIRO) 22
#Preço Atual/ Ativos Circulantes Liquidos por Ação (P/ATIVO CIRC LIQ) 23
#--------------Indicadores de Endividamento--------------
#Divida Liquida/Patrimonio Liquido (DIV LIQUIDA/PL) 24
#Divida Liquida/Earnings Before Interest, Taxes, Depreciation and Amortization (DIV LIQUIDA/EBITDA) 25
#Divida Liquida/Earnings Before Interest and Taxes(DIV LIQUIDA/EBIT) 26
#Patrimonio Liquido/Ativos (PL/ATIVOS) 27
#(PASSIVO/ATIVOS) 28
#Ativo Circulante/Passivo Circulante (LQ CORRENTE) 29
#--------------Indicadores de Eficiencia--------------
#Lucro Bruto/Receita Liquida (Margem Bruta) 30
#EBITDA/Receita Liquida(Margem EBTIDA) 31
#EBIT/Receita Liquida(Margem EBIT) 32
#Lucro Liquido/Receita Liquida(Margem Liquida) 33
#--------------Indicadores de Rentabilidade--------------
#Return on Equity "Retorno sobre Patrimônio Líquido"(ROE) 34
#Return on Assets "Retorno sobre o Ativo"(ROA) 35
#Return Over Invested Capital (ROIC) 36
#(GIRO ATIVOS) 37
#--------------Indicadores de Crescimento--------------
#Compound Annual Growth Rate "Taxa de Crescimento Anual Composta"(CAGR RECEITAS 5 ANOS) 38
#Compound Annual Growth Rate(CAGR LUCROS 5 ANOS) 39
#--------------Aluguel de Açoes--------------
#Tomador (Média) 40
#Doador (Média) 41
#Numero de Acoes 42
#Volume 43
#--------------Proventos--------------
#Ano Passado 44
#Ano Atual 45
#Comparacao 46
#Provisionado 47
#Comparação+Provisionado 48
#--------------Balanço--------------
#Patrimonio Liquido (PL) 49
#Ativos 50
#Ativos Ciculante 51
#Divida Bruta (Divida Total) 52
#Disponibilidade 53
#Divida Liquida 54
#Valor de Mercado 55
#Valor de Firma 56
#Numero total de papeis 57