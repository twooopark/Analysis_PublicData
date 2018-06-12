from .json_request import json_request
from urllib.parse import urlencode

BASE_URL_ENDPOINT = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
PD_SERVICE_KEY = '7hWkC00kUAbX%2BnoncpJzicpWOSHkdCl3bch5Y87fYNlsZtt0T2naKVww2SaSbPlM336TK0%2BfivHG5WRukoEx0A%3D%3D'

def pd_gen_url(endpoint, **params):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), PD_SERVICE_KEY)
    return url



def pd_fetch_foreign_visitor(country_code=0, year=0, month=0, service_key=''):
    pass

def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0):
    url = pd_gen_url(
        BASE_URL_ENDPOINT,
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

