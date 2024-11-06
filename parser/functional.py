from .structures import SResponse, SMRequest
import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_data_from_multitran(request: SMRequest) -> SResponse:
    """THIS MAIN METHOD
    It needs in order to scrape information from translator which is called "multitran"
    """
    response = requests.get(f"https://www.multitran.com/m.exe?ll1=1&ll2=2&s={request.data['request']}")
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    bootstrap_data = [elm.find_next("a").text for elm in soup.find_all(class_='trans')]
    dict_response = {
        "request": request.data['request'],
        "all_trans": [],
    }
    for word in bootstrap_data:
        word.strip()
        dict_response["all_trans"].append(word)
    return SResponse(dict_response)


def get_general_data() -> SResponse:
    """Using the website getip.ir scrapes information about the browser, for example, IP"""
    response = requests.get("https://getip.ir/")
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    info = soup.find_all("div", class_="info")
    if len(info) == 0:
        logger.warning("NOTHING")
    dict_response = dict()
    for name, *values in [elm.text.split() for elm in info]:
        dict_response[name[:-1]] = " ".join(values)
    s_response = SResponse(dict_response)
    return s_response
