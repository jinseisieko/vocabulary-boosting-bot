import logging
import os

import requests
from dotenv import load_dotenv

from parser.structures import SMRequest

logger = logging.getLogger(__name__)


def main():
    print(os.getenv("BOT_TOKEN"))
    parser.get_data_from_multitran(SMRequest("can"))


if __name__ == "__main__":
    logging.basicConfig(
        filename='.log',
        level=logging.NOTSET,
        format='%(asctime)s.%(msecs)03d [%(levelname)s] :%(name)s.%(funcName)s.%(lineno)d: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logger.info("start")
    load_dotenv()
    import parser

    parser.test()
    main()
