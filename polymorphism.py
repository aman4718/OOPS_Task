import logging

logging.basicConfig(filename="inheritance_ex2.log", level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')

class ineuron:
    try:
        def dataScience(self):
            logging.info('Data Science is Highly Paid Job In India')
    except exception as e:
        logging.info(e)

class company:
    try:
        def dataScience(self):
            logging.info('Inerone ptovide best practices to get highest paid job')
    except exception as e:
        logging.info(e)

obj = ineuron()
obj.dataScience()

obj1 = company()
obj1.dataScience()
