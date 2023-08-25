from web_scraping.basket import fiba

import pandas as pd

def fiba_historico(year):
    juego = fiba(year)
    del juego[:1]

    new_lista = []
    if year[0] == 1950:
        for i in range(len(juego)):
            if i!=4 or i!=6:
                new_lista.append(juego[i])
    else:
        if year[0] in range(1963, 1983):
            for i in range(len(juego)):    
                if i<9 and i%2==0:
                    pass
                else:
                    new_lista.append(juego[i])
            
        elif year[0] == 1954 or year[0]==1986 or year[0] in range(1998, 2003):
            for i in range(len(juego)):    
                if i<11 and i%2==0:
                    pass
                else:
                    new_lista.append(juego[i])
            
        elif year[0] in range(2006, 2015):
            for i in range(len(juego)):    
                if i < 7 and i%2==0:
                    pass
                else:
                    new_lista.append(juego[i])
                  
        elif year[0] in range(1990, 1995):
            for i in range(len(juego)):    
                if i < 15 and i%2==0:
                    pass
                else:
                    new_lista.append(juego[i])
                  
        elif year[0] == 1959:
            for i in range(len(juego)):    
                if (i < 9 and i%2==0) or (i==11):
                    pass
                else:
                    new_lista.append(juego[i])
        else:
            for i in range(len(juego)):
                new_lista.append(juego[i])
                       

    new_lista2 = []
    for match in new_lista:
        for element in match:
            if '-' in element:
                new_lista2.append(element)


    new_lista3 = []
    for match in new_lista2:
        aux = match.split(' ')
        if aux!='-':
            new_lista3.append(aux)

    if year[0]==2019:
        bola = []
        for lista in new_lista3:
            lista = [
                elemento for elemento in lista if elemento!='-' and\
                elemento!='ap.' and '(' not in elemento and ')' not in elemento\
                and ',' not in elemento and 'h0' not in elemento\
                and 'h3' not in elemento and elemento!='Shanghai'\
                and elemento!='Dongguan'
            ]
            bola.append(lista)

        lista_nova=[]
        for lista in bola:
            if '-' not in lista[-1]:
                lista_nova.append(lista)
        
        partido = []
        for i in range(len(lista_nova)):
            if(lista_nova[i][-1].isdigit()):
                partido.append(lista_nova[i] + lista_nova[i+1])
            elif lista_nova[i][-1].isalpha():
                cont = 0
                for j in range(len(lista_nova[i])):
                    if (lista_nova[i][j].isdigit()):
                        cont += 1
                if cont == 2:
                    partido.append(lista_nova[i])
                

        lista_partidos = []
        for match in partido:
            new = []
            for i in range(len(match)):
                if match[i].isdigit() and match[i+1].isdigit():
                    new = [
                        ' '.join(match[:i]),
                        match[i],
                        match[i+1],
                        ' '.join(match[i+2:])
                    ]
            lista_partidos.append(new)

        
        
            

    else:               
        
        listado = []
        for lista in new_lista3:
            lista = [elemento for elemento in lista if elemento!='-' and elemento!='ap.'\
                     and 'h3' not in elemento and 'h0' not in elemento]
            new = []
            for i in range(len(lista)):
                if (lista[i].isdigit() and lista[i+1].isdigit()):
                    new =[
                        ' '.join(lista[:i]),
                        lista[i],
                        lista[i+1],
                        ' '.join(lista[i+2:])
                        ]

            listado.append(new)
        
        lista_partidos = []
        for lista in listado:
            if '-' not in lista[-1]:
                lista_partidos.append(lista)


    
    dic = {}        
    TeamA = []
    TeamB = []
    ScoreA = []
    ScoreB = []
    for lista in lista_partidos:
        for i in range(0,len(lista),4):
            TeamA.append(lista[i])
            ScoreA.append(lista[i+1])
            ScoreB.append(lista[i+2])
            TeamB.append(lista[i+3]) 

    dic = {
            'Team A': TeamA,
            'Score A': ScoreA,
            'Score B': ScoreB,
            'Team B': TeamB
        }     
    

    df = pd.DataFrame(dic)
    df['Year'] = year[0]
    print(df)
    return df
    