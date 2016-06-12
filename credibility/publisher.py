from credibility.external.alexa import Alexa
from credibility.external.similar_web import get_traffic_data

ranker = Alexa()


def get_publisher_site_data(url):
    traffic_data = get_traffic_data(url)
    url_rank = ranker.getrank(url)
    if url_rank is -1:
        return False
    return True
