import logging



def setup_logging(script_name):
    logger = logging.getLogger('CustomerChurn')
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the script
    handler = logging.FileHandler(f'C:\\Users\\AUTODESIGN\\Desktop\\DataScience Projects\\CustomerChurnPrediction\\logs\\{script_name}.log',mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
