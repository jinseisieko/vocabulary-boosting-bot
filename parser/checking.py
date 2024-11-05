import logging

from .functional import get_general_data
from .structures import SResponse

logger = logging.getLogger(__name__)


def main() -> None:
    """the main method for checking the parser's performance"""
    logger.info("Parser tests have started")
    response: SResponse = get_general_data()
    if len(response.data.values()) == 0:
        logger.warning("taking general data failed")
    else:
        logger.info("taking general data completed: %r", response.data)
    logger.info("Parser tests have completed correctly")
