import logging
import os

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def main():
    print(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(
        filename='.log',
        level=logging.NOTSET,
        format='%(asctime)s.%(msecs)03d [%(levelname)s] :%(name)s.%(funcName)s.%(lineno)d: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    import parser as pr

    main()
