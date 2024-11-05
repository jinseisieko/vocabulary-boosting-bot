from .structures import SResponse, SRequest
import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_data_from_multitran(request: SRequest) -> SResponse:
    """THIS MAIN METHOD
    It needs in order to scrape information from translator which is called "multitran"
    """


def get_general_data(request: SRequest = SRequest()) -> SResponse:
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
