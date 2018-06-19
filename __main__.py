import collect
import analyze
import visualize
from config import CONFIG

if __name__ == '__main__':
    resultfiles = {}
    resultfiles['tourspot_visitor']=[]
    resultfiles['foreign_visitor']=[]

    # collection
    returnedFilename = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common'])
    resultfiles['tourspot_visitor'].append(returnedFilename)

    for country in CONFIG['countries']:
        returnedFilename = collect.crawling_foreign_visitor(
            country=country,
            **CONFIG['common'])
        resultfiles['foreign_visitor'].append(returnedFilename)

    # analysis
    analyze.anlysis_correlation(resultfiles=resultfiles)

