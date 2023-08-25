
from web_scraping.basket import fiba
import pandas as pd








    

def partidos_2023(year):
    juego = fiba(year)
    new_lista = []
    for i in range(len(juego)):
        if (i < 16 and i%2!=0):
            new_lista.append(juego[i])


    new_lista2 = []
    for partido in new_lista:
        for i in range(len(partido)):
            if 'Agosto' not in partido[i]:
                new_lista2.append(partido[i])    
    
    lista_partidos = []
    for partido in new_lista2:
        lista_partidos.append(partido.split(' - '))

    dic = {}
    teamA = []
    teamB = []
    for partido in lista_partidos:
        teamA.append(partido[0])
        teamB.append(partido[1])      

    
    dic = {
         'Team A': teamA,
         'Team B': teamB
    }

    df = pd.DataFrame(dic)
    df['Year'] = 2023
    return df



    