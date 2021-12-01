import logging.config
logging.config.fileConfig('logging.conf')

rootLoger = logging.getLogger()
rootLoger.debug('this is rott')
logger = logging.getLogger('applog')
logger.debug('this is applog')