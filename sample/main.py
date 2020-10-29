import logging, time, sys, os
from pythonjsonlogger import jsonlogger

"""Our sample log producing application."""

# we're going to set our logger configuration
# in our development instance, we want to produce logs in the native logging format
# in our production instance, we want to produce JSON logs for Graylog stream 
level = logging.DEBUG
if os.environ.get('LOG_TYPE') == 'production':
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        jsonlogger.JsonFormatter('%(message)%(levelname)%(name)%(asctime)')
    )
    logging.basicConfig(level=level, handlers=[handler])
else:
    logging.basicConfig(stream=sys.stdout, level=level)

logging.info('Running logger %s', os.environ.get('LOG_TYPE'))

count = 1
while True:
    # do some contextual logging
    try:
        if count % 10 == 0:
            raise ValueError('An example traceback')

        logging.info(f'Just an info log with count {count}')
    
    except ValueError as e:
        count = 1
        
        logging.error('Something bad happened', exc_info=True) # or logging.exception(e)
        
    time.sleep(2)
    count += 1
