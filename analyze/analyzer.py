import pandas as pd
from scipy import stats as ss
import json
import math

def analysis_correlation(resultfiles):
    result = []
    for filename in resultfiles['tourspot_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
        # print(tourspot_table)

        temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('date')['count_foreigner'].sum())
        # print(temp_tourspot_table)

    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());
        foreign_visitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])

        # merge를 위해 date를 인덱스로 지정한다.
        temp_foreign_visitor_table = foreign_visitor_table.set_index('date')
        # print(temp_foreign_visitor_table)

        # 두 데이터셋을 date를 기준으로 합친다.
        mergeTable = pd.merge(temp_tourspot_table, temp_foreign_visitor_table, on='date') #, left_index=True, right_index=True)
        # print(mergeTable)

        # 1. 나라별, 월별 입국자 수 : visit_count
        # 2. 월별 서울의 관광지 외국인 입장 수 총합 : count_foreigner
        # 이 두 데이터셋의 상관관계를 분석한다.
        x = list(mergeTable['visit_count'])
        y = list(mergeTable['count_foreigner'])

        # columns=['country_name', 'date', 'visit_count'] 이 데이터셋에서 나라명을 중복없이 가져온다.
        country_name = temp_foreign_visitor_table['country_name'].unique().item(0).replace(' ', '')

        # 상관계수 r을 구한다.
        # 피어슨 상관 계수(Pearson correlation coefficient 또는 Pearson's r)

        r = ss.pearsonr(x, y)[0]

        # r = correlation_coefficient(x, y)

        data = { 'x': x, 'y': y, 'country_name': country_name, 'r' : r}

        # 나라별 결과값을 리스트에 추가한다.
        result.append(data)

    return result

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r


def analysis_correlation_by_tourspot(resultfiles):

    result = []
    r_list = {}

    for filename in resultfiles['tourspot_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read());

        tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
        # print("tourspot_table: ", tourspot_table)

        # 서울특별시 관광지 리스트
        tourspot_list = tourspot_table['tourist_spot'].unique()
        print("tourspot_list: ", tourspot_list)

        # # 경복궁의 월별 외국인 입장객 수
        # temp_tourspot_table = pd.DataFrame(tourspot_table[tourspot_table['tourist_spot'] == '경복궁'])
        # print("temp_tourspot_table: ",temp_tourspot_table)
        #
        # temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('tourist_spot')['count_foreigner'].sum())
        # print("temp_tourspot_table: ",temp_tourspot_table)


    for tourspot in tourspot_list:
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read());
            foreign_visitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])

            temp_tourspot_table = pd.DataFrame(tourspot_table[tourspot_table['tourist_spot'] == tourspot])
            # print("temp_tourspot_table: ",temp_tourspot_table)

            # merge를 위해 date를 인덱스로 지정한다.
            temp_foreign_visitor_table = pd.DataFrame(foreign_visitor_table.groupby('date')['visit_count'].sum())
            # print("temp_foreign_visitor_table: ",temp_foreign_visitor_table)

            # 두 데이터셋을 date를 기준으로 합친다.
            mergeTable = pd.merge(temp_tourspot_table, temp_foreign_visitor_table, on='date')
            # print("mergeTable: ", mergeTable)



            # 1. 나라별, 월별 입국자 수 : visit_count
            # 2. 월별 서울의 관광지 외국인 입장 수 총합 : count_foreigner
            # 이 두 데이터셋의 상관관계를 분석한다.
            x = mergeTable['visit_count']
            y = mergeTable['count_foreigner']

            # columns=['count_foreigner', 'date', 'tourist_spot', 'visit_count'] 이 데이터셋에서 tourist_spot을 중복없이 가져온다.
            country_name = foreign_visitor_table['country_name'].unique().item(0).replace(' ', '')
            tourspot = temp_tourspot_table['tourist_spot'].unique().item(0)

            # 상관계수 r을 구한다.
            # 피어슨 상관 계수(Pearson correlation coefficient 또는 Pearson's r)
            # r = ss.pearsonr(x, y)[0]
            r_list[country_name] = correlation_coefficient(x, y)

        data = {'tourspot': tourspot, 'r_중국': r_list['중국'], 'r_일본': r_list['일본'], 'r_미국' : r_list['미국']}

        # 나라별 결과값을 리스트에 추가한다.
        result.append(data)

    return result


# 결과물 예시
# [{'tourspot': '창덕궁', 'r_중국': -0.05787996838309703, 'r_일본': 0.18113398877560832, 'r_미국': 0.15157690000865773},


