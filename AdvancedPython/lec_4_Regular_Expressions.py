import re

email = "jose@techcloude.com"
expression = "[a-z]+"

matched = re.findall(expression, email)
print(matched)


import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    filename='logs.txt'
                    )
logger = logging.getLogger('books')

logger.info('This wil happen')
logger.warning('This will ')
logger.debug('This will ')
logger.critical('This will ')


# logger = logging.getLogger('books.database')