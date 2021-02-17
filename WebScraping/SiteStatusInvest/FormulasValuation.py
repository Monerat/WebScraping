
def GrahamRev(EPS,g,Selic):
    EPS = float(EPS.replace(',','.'))
    if g == '-%':
        g = 0.03
    else:
        g = float(g.strip('%').replace(',','.'))/100 
    v = (EPS*(8.5+2*g)*4.4)/Selic
    return v
#EPS = (Earning per Share) ou LPA
#g = (Expected Growth Rate) ou CAGR lucro 5 anos
#Selic = taxa selic
#v = Valor justo da ação