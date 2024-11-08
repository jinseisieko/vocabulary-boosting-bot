from collections import defaultdict
from pprint import pprint

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

    dict_response = {
        "request": request.data['request'],
        "all": [],
        "gen": [],
        "category": defaultdict(list)
    }

    bootstrap_data = [elm.find_all("a", title=False) for elm in soup.find_all(class_='trans')]
    for _as in bootstrap_data:
        words = [a.text for a in _as]
        for word in words:
            word.strip()
            if not (word in dict_response["all"]):
                dict_response["all"].append(word)

    bootstrap_data = [elm.find_parent("tr").find(class_="trans").find_all("a", title=False) for elm
                      in soup.find_all("nobr", text="gen.")]
    for _as in bootstrap_data:
        words = [a.text for a in _as]
        for word in words:
            word.strip()
            if not (word in dict_response["gen"]):
                dict_response["gen"].append(word)

    bootstrap_data = [(elm.find_parent("tr").find(class_="trans").find_all("a", title=False), elm.find_next("a").text)
                      for elm
                      in soup.find_all(class_="subj")]
    for _as, subj in bootstrap_data:
        words = [a.text for a in _as]
        for word in words:
            word.strip()
            if not (word in dict_response["gen"]):
                dict_response["category"][subj].append(word)
    dict_response["category"] = dict(dict_response["category"])

    return SResponse(dict_response)


def get_general_data() -> SResponse:
    """Using the website getip.ir scrapes information about the browser, for example, IP"""
    response = requests.get("https://getip.ir/")
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    info = soup.find_all("div", class_="info")
    dict_response = dict()
    for name, *values in [elm.text.split() for elm in info]:
        dict_response[name[:-1]] = " ".join(values)
    s_response = SResponse(dict_response)
    return s_response
