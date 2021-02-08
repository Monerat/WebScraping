import requests
from bs4 import BeautifulSoup

def WebScrappingAcao(Codigo):
    Indicadores=[]
    Indicadores.append(Codigo)
    Codigo = Codigo + ".SA"
    URL = "https://br.financas.yahoo.com/quote/"+Codigo+"/key-statistics?p="+Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    Valores = Soup.find_all("td", {"class": "Fw(500) Ta(end) Pstart(10px) Miw(60px)"})
    
    for Valor in Valores:
        Indicadores.append(Valor.text)
    
    URL = "https://br.financas.yahoo.com/quote/"+Codigo+"/financials?p="+Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")
    
    if Soup.find(string="Despesa de Juros") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Despesa de Juros").find_next('span').contents[0]+"k")
    
    if Soup.find(string="Despesa de Juros") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Lucro de Operações em Andamento").find_next('span').contents[0]+"k")
        
    URL = "https://br.financas.yahoo.com/quote/"+Codigo+"/balance-sheet?p="+Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")
    
    if Soup.find(string="Total de Ativos Circulantes") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Total de Ativos Circulantes").find_next('span').contents[0]+"k")
    
    if Soup.find(string="Total de Passivos Circulantes") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Total de Passivos Circulantes").find_next('span').contents[0]+"k")

    if Soup.find(string="Bens do ativo imobilizado") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Bens do ativo imobilizado").find_next('span').contents[0]+"k")

    if Soup.find(string="Bens do ativo imobilizado") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Bens do ativo imobilizado").find_next('span').find_next('span').contents[0]+"k")
    
    if Soup.find(string="Depreciação acumulada") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Depreciação acumulada").find_next('span').contents[0]+"k")
   
    
    URL = "https://br.financas.yahoo.com/quote/"+Codigo+"/cash-flow?p="+Codigo
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.content, "html.parser")

    if Soup.find(string="Depreciação e amortização") == None:
        Indicadores.append("0")
    else:
        Indicadores.append(Soup.find(string="Depreciação e amortização").find_next('span').contents[0]+"k")
    
    return Indicadores

'''
Estrutura da lista Indicadores
Codigo da Ação 0
------------Medidas de Avaliação------------
Capitalização de Mercado (em um dia) 1
Valor da Empresa 2
P/L Passado	3
P/L Estimado 4
Índice PEG (expectativa de 5 anos) 5
Preço/Vendas (ttm)  6
Preço/Livro (mrq)   7
Valor da Empresa/Receita    8
Valor da Empresa/EBITDA     9
------------Histórico de Preço de Ações------------
Beta (mensalmente por 5 anos)   10
Variação de 52 Semanas      11
Variação de 52 Semanas de S&P 500   12
Alta de 52 Semanas      13
Baixa de 52 Semanas     14
Média Móvel de 50 Dias  15
Média Móvel de 200 Dias 16
------------Estatísticas de Ações------------
Volume Médio (3 meses)  17
Volume Médio (10 dias)  18
Ações Em Circulação     19
Flutuação   20
% de Propriedade de insiders    21
% de Propriedade de Instituições    22
Ações a descoberto      23
Índice a descoberto     24
% de baixa de flutuação 25
% de baixa de ações em circulação   26
Ações a descoberto (mês anterior )  27
------------Dividendos e Desdobramentos------------
Taxa Anual de Dividendos Futuros 28
Rendimento Anual de Dividendos Futuros 29
Taxa Anual de Dividendos Passados 30
Rendimento Anual de Dividendos Passados 31
Rendimento do Dividendo Médio de 5 Anos 32
Índice de Payout 33
Data do Dividendo 34
Data do Ex-Dividendo 35
Fator do último desdobramento 36
Última Data do Desdobramento 37
________Destaques de Finanças________
------------Ano Fiscal------------
Fim do Ano Fiscal   38
Último Trimestre (mrq)	39
------------Rentabilidade------------
Margem de Lucro	40
Margem Operacional (ttm)    41
------------Efetividade do Gerenciamento------------
Rentabilidade do Ativo (ttm)    42
Retorno Sobre o Patrimônio Líquido (ttm) 43
------------Demonstração de Resultados------------
Receita (ttm)   44
Receita por Ação (ttm)	45
Aumento de Receita Trimestral (yoy)	46
Lucro Bruto (ttm)	47
Lajida	48
Lucro Líquido Méd. a Comum (ttm)	49
Lucro pro Ação Diluído (ttm)	50
Aumento de Ganhos Trimestral (yoy)	51
------------Balanço------------
Fluxo de Caixa Total (mrq)	52
Fluxo de Caixa Total por Ação (mrq)	53
Débito Total (mrq)	54
Débito Total/Patrimônio Líquido (mrq)	55
Índice de Liquidez (mrq)	56
Valor Contábil Por Ação (mrq)	57
------------Demonstração do Fluxo de Caixa------------
Fluxo de Caixa Operacional (ttm)	58
Fluxo de Caixa Livre Alavancado (ttm)	59
Despesa de Juros(Despesa Finaceira)    60
Lucro de Operações em Andamento (Nopat)    61
Total de Ativos Circulantes     62
Total de Passivos Circulantes   63
Bens do ativo imobilizado ultimo ano    64
Bens do ativo imobilizado penultimo ano 65
Depreciação acumulada   66
Depreciação e amortização 67
'''