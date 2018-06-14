import collection


if __name__ == '__main__':

    # collection
    # collection.crawling_tourspot_visitor(district='부산광역시', start_year=2012, end_year=2014)
    #
    for country in [('중국', 112) , ('일본', 130), ('미국', 275)]:
        collection.crawling_foreign_visitor(country, 2012, 2013)