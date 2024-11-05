import logging

from .functional import get_general_data
from .structures import SResponse

logger = logging.getLogger(__name__)


def main() -> None:
    """the main method for checking the parser's performance"""
    logger.info("Parser tests have started")
    response: SResponse = get_general_data()
    failed = False
    if len(response.data.values()) == 0:
        logger.warning("taking general data failed")
        failed = True
    else:
        logger.info("taking general data completed: %r", response.data)
    if not failed:
        logger.info("Parser tests have completed correctly")
    else:
        logger.warning("Parser tests have completed incorrectly")
