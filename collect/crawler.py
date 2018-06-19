import json
from .api import api

def preprocess_foreign_visitor(data):
    if 'natKorNm' in data:
        data['country_name'] = data.pop('natKorNm')
    if 'natCd' in data:
        data['country_code'] = data.pop('natCd')
    if 'ym' in data:
        data['date'] = data.pop('ym')
    if 'num' in data:
        data['visit_count'] = data.pop('num')
    if 'ed' in data:
        data.pop('ed')
    if 'edCD' in data:
        data.pop('edCD')
    if 'rnum' in data:
        data.pop('rnum')

def preprocess_tourspot_visitor(post):
    if 'csNatCnt' in post:
        post['count_locals'] = post.pop('csNatCnt')
    if 'csForCnt' in post:
        post['count_foreigner'] = post.pop('csForCnt')
    if 'resNm' in post:
        post['tourist_spot'] = post.pop('resNm')
    if 'sido' in post:
        post['restrict1'] = post.pop('sido')
    if 'gungu' in post:
        post['restrict2'] = post.pop('gungu')
    if 'ym' in post:
        post['date'] = post.pop('ym')
    if 'addrCd' in post:
        post.pop('addrCd')
    if 'rnum' in post:
        post.pop('rnum')



def crawling_foreign_visitor(
        country,
        start_year,
        end_year,
        fetch=True,
        restore_dir='',
        service_key=''):

    results = []
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (restore_dir, country[0], country[1], start_year, end_year)

    if fetch:
        for i in range(start_year, end_year+1):
            for j in range(1, 13):
                for posts in api.pd_fetch_foreign_visitor(country_code=country[1], year=i, month=j, service_key=service_key):
                    if type(posts) is dict:
                        posts = [posts]
                    for post in posts:
                        preprocess_foreign_visitor(post)
                    # print(posts)
                    # print(type(posts), posts)
                    results += posts

        # save data to file
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename

def crawling_tourspot_visitor(
        district,
        start_year,
        end_year,
        fetch=True,
        restore_dir='',
        service_key=''):

    results = []
    filename = '%s/%s_tourspot_%s_%s.json' % (restore_dir, district, start_year, end_year)

    if fetch:
        for i in range(start_year, end_year+1):
            for j in range(1, 13):
                # retuned posts type is two cases, if posts have a one value, type is Dictinary, else if posts have several values, type is List
                # EX) busan,  12y --> list 13y --> None 14y --> dict
                for posts in api.pd_fetch_tourspot_visitor(district1=district, year=i, month=j, service_key=service_key):
                    if type(posts) is dict:
                        posts = [posts]
                        # print(type(posts), posts)
                    for post in posts:
                        preprocess_tourspot_visitor(post)
                    results += posts
                    # print(type(results), results)
        # save results to file(저장, 적재)
        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename
