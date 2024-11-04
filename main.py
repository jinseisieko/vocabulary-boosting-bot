import logging

logger = logging.getLogger(__name__)


def main():
    print('hello world!!!')


if __name__ == "__main__":
    logging.basicConfig(
        filename='.log', level=logging.INFO,
        format='%(asctime)s.%(msecs)03d [%(levelname)s] :%(name)s.%(funcName)s.%(lineno)d: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    import parser as pr

    main()
