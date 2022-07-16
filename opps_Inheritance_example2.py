import logging

logging.basicConfig(filename="inheritance_ex2.log", level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(name)s %(message)s')


class college:
    try:
        def students(self, age):
            self.age = age
            if (age == 26):
                try:
                    logging.info('my age is %s',age)
                except valueError:
                    raise valueError('Something went wrong')

    except SyntaxError as e:
        logging.info(e)


class department(college):
    try:
        def depart(self):
            logging.info('Welcome to Department of Science')
    except SyntaxError as e:
        logging.info(e)


class Fee(department):
    pass


c = Fee()
c.students(26)
c.depart()