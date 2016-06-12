from similarweb import TrafficClient


traffic_client = TrafficClient('63cefd48f8a7e97fc102df3922e4355b')


def get_traffic_data(url):
    print traffic_client.traffic(url)
