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
    results = analyze.analysis_correlation(resultfiles=resultfiles)

    # visualize
    for result in results :
        print(result)
    visualize.graph_scatter(results, showgraph=False)


    # 2. analysis & vsualization
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles=resultfiles)
    print(result_analysis)
    visualize.graph_bar(result_analysis, showgraph=True)




