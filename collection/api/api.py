from .json_request import json_request
from urllib.parse import urlencode
from datetime import datetime


TOUR_URL_ENDPOINT = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
ED_URL_ENDPOINT = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

PD_SERVICE_KEY = '%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D'

def pd_gen_url(endpoint, **params):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), PD_SERVICE_KEY)
    return url



def pd_fetch_foreign_visitor(
        country_code=0,
        year=0,
        month=0):
    # pass
    url = pd_gen_url(
        ED_URL_ENDPOINT,
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
        month=0):
    url = pd_gen_url(
        TOUR_URL_ENDPOINT,
        YM='{0:04d}{1:02d}'.format(year, month),
        SIDO=district1,
        GUNSU=district2,
        RES_NM=tourspot,
        numOfRows=10,
        _type='json',
        pageNo=1
    )
    json_result = json_request(url=url)
    resHeader = json_result.get('response').get('header')
    resMsg = "OK" if resHeader.get('resultMsg') == "OK" else "Fail"
    print(resMsg)
    resBody = json_result.get('response').get('body')
    items = None if resBody is None else resBody.get('items')
    try:
        item = None if items is None else items.get('item')
        yield item
    except AttributeError:
        pass

