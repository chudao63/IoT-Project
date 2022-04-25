import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, message, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    """
    Lưu lại log vào file log 
    """
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.info(message)

# setup_logger(name = 'log', log_file= 'logs/log.log', message= "hello")
