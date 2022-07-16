import logging

logging.basicConfig(filename="inheritance_ex2.log", level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')

class parent:
    try:
        def father(self):
            logging.info('I am Your Father')
    except Exception as e:
        logging.info(e)
class uncle:
    try:
        def uncle(self):
            logging.info('I am Your Uncle')
    except Exception as e:
        logging.info(e)
class child(parent,uncle):
    try:
        def children(self):
            logging.info('I am your son')
    except Exception as e:
        logging.info(e)
obj = child()
obj.father()
obj.uncle()