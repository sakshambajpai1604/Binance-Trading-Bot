import logging

def get_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("bot.log")
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger