import collect
import analyze
import visualize
from config import CONFIG

if __name__ == '__main__':
    # collection
    collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common'])

    for country in CONFIG['countries']:
        collect.crawling_foreign_visitor(country, **CONFIG['common'])

