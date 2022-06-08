import pandas as pd
import random as rd

#!Lee el csv
def data(file1='variable_stars_database-small - copia.csv', file2="non_variable_stars_database-small - copia.csv"):
    variables = pd.read_csv(file1, delimiter=",")
    non_variables = pd.read_csv(file2, delimiter=",")
    return (variables, non_variables)

#!Crea un dict donde key es el id de la estrella y value un dict con su información donde cada llave es una variable
def filtered_data(stars):
    data = stars[0]
    size = (data.shape)[0]
    variables = {}
    for i in range(0,size):
        info = {}
        id = data.iloc[i]['source_id']
        for variable in data.columns:
            if variable != 'source_id' and variable != 'ruwe;;;;;':
                info[variable] = data.iloc[i][variable]
            elif variable == 'ruwe;;;;;':
                ruwe = data.iloc[i][variable]
                if len(ruwe) > 5:
                    info['ruwe'] = float((str(data.iloc[i][variable]))[:-5])
                else:
                    info['ruwe'] = 'nan'
            elif variable != 'source_id':
                info[variable] = data.iloc[i][variable]
        variables[id] = info
    data = stars[1]
    size = (data.shape)[0]
    non_variables = {}
    for i in range(0,size):
        info = {}
        id = data.iloc[i]['solution_id']
        for variable in data.columns:
            if variable != 'solution_id':
                if not data.iloc[i][variable] == '':
                    info[variable] = data.iloc[i][variable]
                else:
                    info[variable] = 'nan'
        non_variables[id] = info

    return (variables, non_variables)

#! Retornar un diccionario de estrellas combinadas
def combined_data(data):
    stars = {}
    num = min(len(data[0].keys()), len(data[1].keys()))
    if (num <= len(data[0].keys())) and (num <= len(data[1].keys())):
        rand = [rd.randint(0,num*2) for i in range(num//2)]
        n = 0
        for key in data[0].keys():
            if n in rand:
                stars[key] = data[0][key]
            n += 1
        if n%2 == 0:
            rand = [rd.randint(0,num*2) for i in range(num//2)]
        else:
            rand = [rd.randint(0,num*2) for i in range((num//2)+1)]
        n = 0
        for key in data[1].keys():
            if (n in rand):
                stars[key] = data[1][key]
            n += 1
    return stars

#!Retorna un dict de listas con los id de las estrellas previamente clasificadas en la base de datos
def previous_classified(data):
    rotational, delta_scuti, cepheid, mira, eclipsing_binary, irregular, semi_irregular, uncertain, lyrae, coronae_borealis, cataclysmic, flare, other_rotational, pulsating_white_dwarf, other = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    data = data[0]
    for i in data.keys():
        type = data[i]['variable_type']
        id = data[i]['id']
        if type == 'ROT':
            rotational.append(id)
        elif type in ['DSCT', 'HADS']:
            delta_scuti.append(id)
        elif type in ['CWA','CWB','DCEP','DCEPS','RVA']:
            cepheid.append(id)
        elif type == 'M':
            mira.append(id)
        elif type in ['EA', 'EB', 'EW', 'ELL']:
            eclipsing_binary.append(id)
        elif type in ['YSO', 'L', 'GCAS']:
            irregular.append(id)
        elif type in ['SR', 'SRD', 'LSP']:
            semi_irregular.append(id)
        elif type in ['GCAS:', 'ROT:', 'SR:', 'VAR:', 'RRAB:', 'DSCT:', 'M:']:
            uncertain.append(id)
        elif type in ['RRAB', 'RRC', 'RRD']:
            lyrae.append(id)
        elif type in ['RCB', 'RCB:', 'DYPer']:
            coronae_borealis.append(id)
        elif type in ['CV', 'CV+E', 'CV:', 'UG', 'UGER', 'UGSS', 'UGSU', 'UGSU+E', 'UGSU:', 'UGWZ', 'UGZ', 'AM', 'AM+E', 'AM:', 'DQ', 'DQ:']:
            cataclysmic.append(id)
        elif type in ['UV', 'UV:']:
            flare.append(id)
        elif type in ['SXARI', 'SXARI:', 'HB', 'R']:
            other_rotational.append(id)
        elif type in ['ZZ', 'ZZ:', 'ZZA', 'ZZB', 'ZZLep', 'ZZO']:
            pulsating_white_dwarf.append(id)
        else:
            other.append(id)
    classified = {'rotational':rotational,
                  'delta_scuti':delta_scuti,
                  'cepheid':cepheid,
                  'mira':mira,
                  'eclipsing_binary':eclipsing_binary,
                  'irregular':irregular,
                  'semi_irregular':semi_irregular,
                  'uncertain':uncertain,
                  'lyrae':lyrae,
                  'coronae_borealis':coronae_borealis,
                  'cataclysmic':cataclysmic,
                  'flare':flare,
                  'other_rotational':other_rotational,
                  'pulsating_white_dwarf':pulsating_white_dwarf,
                  'other':other
                  }
    return classified

#!Función que retorna la información de una estrella dado un id
def search_by_id(id, data):
    star = None
    for tup in data:
        for key in tup.keys():
            if 'id' in tup[key].keys():
                if tup[key]['id'] == str(id):
                    star = tup[key]
            else:
                if tup[key]['source_id'] == str(id):
                    star = tup[key]
    return star