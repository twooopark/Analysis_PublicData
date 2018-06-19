import pandas as pd
from scipy import stats as ss #피어슨 상관 계수(Pearson correlation coefficient 또는 Pearson's r)
import json

def anlysis_correlation(resultfiles):
    result = []
    for filename in resultfiles['tourspot_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
        temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('date')['count_foreigner'].sum())
        # print(temp_tourspot_table)

    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        foreign_visitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])

        temp_foreign_visitor_table = foreign_visitor_table.set_index('date')
        mergeTable = pd.merge(temp_tourspot_table, temp_foreign_visitor_table, on='date') #, left_index=True, right_index=True)
        print(mergeTable)

        x = list(mergeTable['visit_count'])
        y = list(mergeTable['count_foreigner'])
        country_name = temp_foreign_visitor_table['country_name'].unique().item(0)
        r = ss.pearsonr(x, y)
        data = { 'x': x, 'y': y, 'country_name': country_name, 'r' : r[0]}
        result.append(data)
    return result

def anlysis_correlation_by_tourspot(resultfiles):
    pass


