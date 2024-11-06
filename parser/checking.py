import logging

from .functional import get_general_data, get_data_from_multitran
from .structures import SMRequest

logger = logging.getLogger(__name__)


def main() -> None:
    """the main method for checking the parser's performance"""
    logger.info("Parser tests have started")
    failed = False

    response = get_general_data()
    assert len(response.data) != 0
    if not ("Ip" in response.data):
        logger.warning("taking general data failed")
        failed = True
    else:
        logger.info("taking general data completed: %r", response.data)

    response = get_data_from_multitran(SMRequest("clock"))
    assert len(response.data) != 0
    if not ("часы" in response.data["all"]):
        logger.warning("checking parser of multitran failed")
        failed = True
    else:
        logger.info("checking parser of multitran completed: %r", response.data)

    if not failed:
        logger.info("Parser tests have completed correctly")
    else:
        logger.warning("Parser tests have completed incorrectly")
