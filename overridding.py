import logging

logging.basicConfig(filename="inheritance_ex2.log", level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')

class train:
    try:
        def engineOne(self,cond):
            logging.info('Switch to %s',cond)
    except Exception as e:
        logging.info(e)
class station(train):
    def engineOne(self,cond):
        logging.info('Switch to diesel')

obj = station()
obj.engineOne('electic')

