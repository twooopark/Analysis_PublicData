import analysis_pd.collection.api as pdapi

# test for pd_gen_url
# url = pdapi.pd_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
#     YM='{0:04d}{1:02d}'.format(2017, 1),
#     SIDO='서울특별시',
#     GUNSU='',
#     RES_NM='',
#     numOfRows=10,
#     _type='json',
#     pageNo=1
# )
# print(url)
#
# test for pd_fetch_tourspot_visitor
for items in pdapi.pd_fetch_tourspot_visitor(district1='부산광역시', year=2012, month=7):
    print(items)

# test for pd_fetch_foreign_visitor
# for items in pdapi.pd_fetch_foreign_visitor(country_code=112, year=2012, month=7):
#     print(items)