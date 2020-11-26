import urllib.request, json

asx_base_url = "https://asx.api.markitdigital.com/asx-research/1.0/companies/"


def get_header_path(ticker: str) -> str:
    """Returns the request url for the 'header' information for a given ticker."""
    return asx_base_url + "/" + ticker + "/header"

def get_key_stats_path(ticker: str) -> str:
    """Returns the request url for the 'key statistics' information for a given ticker."""
    return asx_base_url + "/" + ticker + "/key-statistics"

def get_last_price(ticker: str) -> float:
    """Returns the last price for a given ticker."""
    response = urllib.request.urlopen(get_header_path(ticker)).read().decode()
    data = json.loads(response)
    return float(data['data']['priceLast'])

def get_key_stats(ticker: str) -> object:
    response = urllib.request.urlopen(get_key_stats_path(ticker)).read().decode()
    data = json.loads(response)
    return data

if __name__ == "__main__":
    print(get_key_stats("VDHG"))