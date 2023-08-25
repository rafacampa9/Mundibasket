import pandas as pd
from Constantes.years import YEARS
from data_scrapeo.historico_partidos import fiba_historico
from data_scrapeo.partidos_para_predecir import partidos_2023
from data_scrapeo.grupos import grupos
import pickle


# MAIN ####################################################################################################
if __name__=='__main__':

    n = int(input('Introduce un número:\n\n1: Data histórica.\n2: Partidos este año.\n3: Grupos este año.\n\n'))
      
    if (n == 1):
        mundiales = [fiba_historico(year) for year in YEARS if year[0]!=2023]                 
        df_mundial = pd.concat(mundiales, ignore_index = True)
        print(df_mundial)
        df_mundial.to_json('/home/zaraki/Escritorio/Proyectos/Proyecto mundibasket/Data/historico_data.json')
        print('DATA DE PARTIDOS HISTÓRICOS ALMACENADA.')        

    elif n == 2:
        partidos = partidos_2023(YEARS[-1])
        df_partidos = pd.DataFrame(partidos)
        print(df_partidos)
        df_partidos.to_json('/home/zaraki/Escritorio/Proyectos/Proyecto mundibasket/Data/partidos_2023.json')
        print('PARTIDOS 2023 ALMACENADOS.')
    elif n == 3:
        dic = grupos(YEARS[-1])
        pickle.dump(dic,open('/home/zaraki/Escritorio/Proyectos/Proyecto mundibasket/Data/dic_table', 'wb'))
        print('GRUPOS 2023 ALMACENADOS.')
        print(dic)
    else:
        print('Que te den.')