import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_tourspot_visitor(item):
    pass


def preprocess_foreign_visitor(data):
    pass


def crawling_foreign_visitor(
        country,
        start_year,
        end_year,
        restore_directory,
        service_key,
        fetch=True):
    pass
def preprocess_post(post):
    if 'csNatcnt' in post:
        post['count_locals'] = post.pop('csNatcnt')
    if 'csForcnt' in post:
        post['count_forigner'] = post.pop('csForcnt')
    if 'resNm' in post:
        post['tourist_spot'] = post.pop('resNm')
    if 'sido' in post:
        post['restrict1'] = post.pop('sido')
    if 'gungu' in post:
        post['restrict2'] = post.pop('gungu')
    if 'addrCd' in post:
        post.pop('addrCd')
    if 'rnum' in post:
        post.pop('rnum')
    if 'ym' in post:
        post.pop('ym')



def crawling_tourspot_visitor(
        district,
        start_year,
        end_year
        ):
    results = []
    filename = '%s/%s_tourspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    for i in range(start_year, end_year+1):
        for j in range(1, 13):
            for posts in api.pd_fetch_tourspot_visitor(district1=district, year=i, month=j):
                for post in posts:
                    preprocess_post(post)
                # print(posts)
                # print(results)
                results += posts
    # save results to file(저장, 적재)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

# 경로가 없으면 만들자
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
