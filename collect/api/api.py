import sys
import math
from .json_request import json_request
from urllib.parse import urlencode
from datetime import datetime


TOUR_URL_ENDPOINT = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
ED_URL_ENDPOINT = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

def pd_gen_url(endpoint, service_key, **params):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), service_key)
    return url



def pd_fetch_foreign_visitor(
        country_code=0,
        year=0,
        month=0,
        service_key=''):

    url = pd_gen_url(
        ED_URL_ENDPOINT,
        service_key,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        ED_CD = 'E',
        numOfRows=10,
        _type='json',
        pageNo=1
    )
    json_result = json_request(url=url)
    resHeader = json_result.get('response').get('header')
    if resHeader.get('resultMsg') != "OK" :
        print("%s Error[%s] for request %s" % (datetime.now(), resHeader.get('resultMsg'), url))
        return None
    resBody = json_result.get('response').get('body')
    items = None if resBody is None else resBody.get('items')

    yield items.get('item') if isinstance(items, dict) else None


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0,
        service_key=''):

    # v1.1 use pageno, hasnext
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageno = 1
    hasnext = True

    while hasnext:
        url = pd_gen_url(
            endpoint,
            service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=100,
            _type='json',
            pageNo=pageno)

        json_result = json_request(url=url)
        if json_result is None:
            break

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')

        if 'OK' != result_message:
            print('%s : Error[%s] for Request(%s)' % (datetime.now(), result_message, url), file=sys.stderr)
            break

        json_body = json_response.get('body')

        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')

        if totalcount == 0:
            break

        last_pageno = math.ceil(totalcount / numofrows)
        if pageno == last_pageno:
            hasnext = False
        else:
            pageno += 1

        json_items = json_body.get('items')
        yield json_items.get('item') if isinstance(json_items, dict) else None



    # # v 1.0
    # url = pd_gen_url(
    #     TOUR_URL_ENDPOINT,
    #     service_key,
    #     YM='{0:04d}{1:02d}'.format(year, month),
    #     SIDO=district1,
    #     GUNSU=district2,
    #     RES_NM=tourspot,
    #     _type='json',
    #     numOfRows=50, pageNo=1)
    #
    # json_result = json_request(url=url)
    #
    # resHeader = json_result.get('response').get('header')
    # if resHeader.get('resultMsg') != "OK" :
    #     print("%s Error[%s] for request %s" % (datetime.now(), resHeader.get('resultMsg'), url))
    #     return None
    # resBody = json_result.get('response').get('body')
    # items = None if resBody is None else resBody.get('items')
    # try:
    #     item = None if items is None else items.get('item')
    #     yield item
    # except AttributeError:
    #     pass