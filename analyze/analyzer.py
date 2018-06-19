import pandas as pd
import json

def anlysis_correlation(resultfiles):

    for filename in resultfiles['tourspot_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
        temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('date')['count_foreigner'].sum())
        # print(json_data)
        # print(filename)
        print(temp_tourspot_table)

    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        foreign_visitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        # temp_foreign_visitor_table = pd.DataFrame(foreign_visitor_table.groupby('date')['country_name'].sum())
        # print(filename)
        temp_foreign_visitor_table = foreign_visitor_table.set_index('date')
        print(temp_foreign_visitor_table)

    mergeTable = pd.merge(temp_tourspot_table, temp_foreign_visitor_table, left_index=True, right_index=True)
    print(mergeTable)


def anlysis_correlation_by_tourspot(resultfiles):
    pass


