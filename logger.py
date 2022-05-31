import logging

# create logger 
my_logger  = logging.getLogger(__name__) # inherits the name from the current module
my_logger.setLevel(logging.INFO) # set the logging level, change if needed

# set formatter
formatter= logging.Formatter('%(asctime)s _ %(message)s')

# set file handler for file configs
#fh=logging.FileHandler('C:\\Users\\user\\Desktop\\test\\sample_log.log')
fh=logging.FileHandler('sample_log.log')
fh.setFormatter(formatter)

my_logger.addHandler(fh)

# Write Code
def add(x,y):
    res=x+y

    my_logger.info('Result: {}'.format(res))

    return res

add(1,1)

