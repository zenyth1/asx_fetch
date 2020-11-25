import urllib.request, json

asx_base_url = "https://asx.api.markitdigital.com/asx-research/1.0/companies/"


def get_header_path(ticker: str) -> str:
    """Returns the request url for the 'header' information for a given ticker."""
    return asx_base_url + "/" + ticker + "/header"

def get_current_price(ticker: str) -> str:
    response = urllib.request.urlopen(get_header_path(ticker)).read().decode()
    data = json.loads(response)
    return data['data']['priceLast']

if __name__ == "__main__":
    print(get_current_price("VDHG"))
    print(get_current_price("MSB"))