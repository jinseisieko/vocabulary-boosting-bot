from .structures import SResponse, SRequest
import logging

logger = logging.getLogger(__name__)


def get_data_from_multitran(request: SRequest) -> SResponse:
    """THIS MAIN METHOD
    It needs in order to scrape information from translator which is called "multitran"
    """
