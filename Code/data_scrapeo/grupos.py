

from web_scraping.basket import fiba
import pandas as pd






def grupos(year):
    listas = fiba(year)
    grupos = []
    for i in range(len(listas)):
        if i<15 and i%2==0:
            grupos.append(listas[i])

    
    
    teams = []
    for grupo in grupos:
        teams.append(grupo[1:])

    elementos = []
    for team in teams:
        for ele in team:
            elementos.append(ele.split(' '))

    lista_equipos = []
    for elemento in elementos:
        new = []
        for i in range(len(elemento)):
            if elemento[i].isalpha() and elemento[i+1].isdigit():
                new = [
                    ' '.join(elemento[1:i+1]),
                    elemento[i+1],
                    elemento[i+2],
                    elemento[i+3],
                    elemento[i+4],
                    elemento[i+5],
                    elemento[i+6],
                    elemento[i+7]
                ]
        lista_equipos.append(new)

    dic_table = {}
    groupA = []
    groupB = []
    groupC = []
    groupD = []
    groupE = []
    groupF = []
    groupG = []
    groupH = []
    groupA= [
        lista_equipos[0],
        lista_equipos[1],
        lista_equipos[2],
        lista_equipos[3]
    ]
    
    groupB= [
        lista_equipos[4],
        lista_equipos[5],
        lista_equipos[6],
        lista_equipos[7]
    ]

    groupC= [
        lista_equipos[8],
        lista_equipos[9],
        lista_equipos[10],
        lista_equipos[11]
    ]

    groupD = [
        lista_equipos[12],
        lista_equipos[13],
        lista_equipos[14],
        lista_equipos[15]
    ]

    groupE= [
        lista_equipos[16],
        lista_equipos[17],
        lista_equipos[18],
        lista_equipos[19]
    ]

    groupF= [
        lista_equipos[20],
        lista_equipos[21],
        lista_equipos[22],
        lista_equipos[23]
    ]

    groupG= [
        lista_equipos[24],
        lista_equipos[25],
        lista_equipos[26],
        lista_equipos[27]
    ]

    groupH = [
        lista_equipos[28],
        lista_equipos[29],
        lista_equipos[30],
        lista_equipos[31]
    ]
    
    headers = ['Team', 'Pts', 'J', 'W', 'L', 'P+', 'P-', 'DF']
    df_a = pd.DataFrame(groupA)
    df_a.columns=headers
    df_b = pd.DataFrame(groupB)
    df_b.columns=headers
    df_c = pd.DataFrame(groupC)
    df_c.columns=headers
    df_d = pd.DataFrame(groupD)
    df_d.columns=headers
    df_e = pd.DataFrame(groupE)
    df_e.columns=headers
    df_f = pd.DataFrame(groupF)
    df_f.columns=headers
    df_g = pd.DataFrame(groupG)
    df_g.columns=headers
    df_h = pd.DataFrame(groupH)
    df_h.columns=headers


    dic_table['Group A'] = df_a
    dic_table['Group B'] = df_b
    dic_table['Group C'] = df_c
    dic_table['Group D'] = df_d
    dic_table['Group E'] = df_e
    dic_table['Group F'] = df_f
    dic_table['Group G'] = df_g
    dic_table['Group H'] = df_h

    return dic_table